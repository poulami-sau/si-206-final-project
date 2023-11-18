import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
db_filename = dir_path + '/zipCode_airQuality.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

zip_codes = [("Birmingham", "AL", 35211), ("Montgomery", "AL", 36117), ("Huntsville", "AL", 35810), ("Mobile", "AL", 36609), ("Tuscaloosa", "AL", 35401),
             ("Anchorage", "AK", 99504), ("Fairbanks", "AK", 99709), ("Juneau", "AK", 99801), ("Wasilla", "AK", 99654), ("Sitka", "AK", 99835),
             ("Phoenix", "AZ", 85032), ("Tucson", "AZ", 85710), ("Mesa", "AZ", 85204), ("Chandler", "AZ", 85225), ("Scottsdale", "AZ", 85255),
             ("Little Rock", "AR", 72204), ("Fort Smith", "AR", 72903), ("Fayetteville", "AR", 72701), ("Springdale", "AR", 72764), ("Jonesboro", "AR", 72401),
             ("Los Angeles", "CA", 90011), ("San Diego", "CA", 92154), ("San Jose", "CA", 95123), ("San Francisco", "CA", 94112), ("Fresno", "CA", 93722),
             ("Denver", "CO", 80219), ("Colorado Springs", "CO", 80918), ("Aurora", "CO", 80013), ("Fort Collins", "CO", 80525), ("Lakewood", "CO", 80228),
             ("Bridgeport", "CT", "06606"), ("New Haven", "CT", "06511"), ("Stamford", "CT", "06902"), ("Hartford", "CT", "06106"), ("Waterbury", "CT", "06704"),
             ("Wilmington", "DE", 19805), ("Dover", "DE", 19901), ("Newark", "DE", 19711), ("Middletown", "DE", 19709), ("Smyrna", "DE", 19977),
             ("Jacksonville", "FL", 32210), ("Miami", "FL", 33186), ("Tampa", "FL", 33647), ("Orlando", "FL", 32828), ("St. Petersburg", "FL", 33710),
             ("Atlanta", "GA", 30318), ("Augusta", "GA", 30906), ("Columbus", "GA", 31907), ("Macon", "GA", 31204), ("Savannah", "GA", 31419),
             ("Honolulu", "HI", 96815), ("Pearl City", "HI", 96782), ("Hilo", "HI", 96720), ("Kailua", "HI", 96734), ("Waipahu", "HI", 96797),
             ("Boise", "ID", 83709), ("Meridian", "ID", 83646), ("Nampa", "ID", 83687), ("Idaho Falls", "ID", 83404), ("Pocatello", "ID", 83201),
             ("Chicage", "IL", 60629), ("Aurora", "IL", 60506), ("Rockford", "IL", 61107), ("Joliet", "IL", 60435), ("Naperville", "IL", 60564),
             ("Indianapolis", "IN", 46227), ("Fort Wayne", "IN", 46815), ("Evansville", "IN", 47715), ("South Bend", "IN", 46614), ("Carmel", "IN", 46032),
             ("Des Moines", "IA", 50315), ("Cedar Rapids", "IA", 52402), ("Davenport", "IA", 52804), ("Sioux City", "IA", 51106), ("Iowa City", "IA", 52240),
             ("Wichita", "KS", 67212), ("Overland Park", "KS", 66212), ("Kansas City", "KS", 66102), ("Olathe", "KS", 66062), ("Topeka", "KS", 66614),
             ("Louisville", "KY", 40214), ("Lexington", "KY", 40517), ("Bowling Green", "KY", 42101), ("Owensboro", "KY", 42301), ("Covington", "KY", 41011),
             ("New Orleans", "LA", 70119), ("Baton Rouge", "LA", 70809), ("Shreveport", "LA", 71105), ("Lafayette", "LA", 70506), ("Lake Charles", "LA", 70605),
             ("Portland", "ME", "04101"), ("Lewiston", "ME", "04240"), ("Bangor", "ME", "04401"), ("South Portland", "ME", "04106"), ("Auburn", "ME", "04210"),
             ("Baltomore", "MD", 21215), ("Frederick", "MD", 21701), ("Rockville", "MD", 20850), ("Gaithersburg", "MD", 20878), ("Bowie", "MD", 20715),
             ("Boston", "MA", "02124"), ("Worcester", "MA", "01604"), ("Springfield", "MA", "01104"), ("Cambridge", "MA", "02139"), ("Lowell", "MA", "01852"),
             ("Detroit", "MI", 48219), ("Grand Rapids", "MI", 49504), ("Warren", "MI", 48089), ("Sterling Heights", "MI", 48310), ("Ann Arbor", "MI", 48103), 
             ("Minneapolis", "MN", 55407), ("Saint Paul", "MN", 55106), ("Duluth", "MN", 55807), ("Bloomington", "MN", 55420), ("Plymouth", "MN", 55441),
             ("Jackson", "MS", 39212), ("Gulfport", "MS", 39503), ("Southaven", "MS", 38671), ("Hattiesburg", "MS", 39402), ("Biloxi", "MS", 39531),
             ("Kansas City", "MO", 64118), ("Saint Louis", "MO", 63116), ("Springfield", "MO", 65807), ("Columbia", "MO", 65202), ("Independence", "MO", 64055),
             ("Billings", "MT", 59102), ("Missoula", "MT", 59801), ("Great Falls", "MT", 59405), ("Bozeman", "MT", 59715), ("Butte", "MT", 59701),
             ("Omaha", "NE", 68104), ("Lincoln", "NE", 68503), ("Bellevue", "NE", 68005), ("Grand Island", "NE", 68801), ("Kearney", "NE", 68845),
             ("Las Vegas", "NV", 89103), ("Henderson", "NV", 89014), ("Reno", "NV", 89502), ("North Las Vegas", "NV", 89030), ("Sparks", "NV", 89431),
             ("Manchester", "NH", "03101"), ("Nashua", "NH", "03060"), ("Concord", "NH", "03301"), ("Derry", "NH", "03038"), ("Rochester", "NH", "03867"),
             ("Newark", "NJ", "07102"), ("Jersey City", "NJ", "07302"), ("Paterson", "NJ", "07501"), ("Elizabeth", "NJ", "07201"), ("Edison", "NJ", "08817"),
             ("Albuquerque", "NM", 87102), ("Las Cruces", "NM", 88001), ("Rio Rancho", "NM", 87124), ("Santa Fe", "NM", 87505), ("Rosewell", "NM", 88201), 
             ("New York City", "NY", 10019), ("Buffalo", "NY", 14201), ("Rochester", "NY", 14604), ("Yonkers", "NY", 10701), ("Syracuse", "NY", 13202), 
             ("Charlotte", "NC", 28202), ("Raleigh", "NC", 27601), ("Greensboro", "NC", 27401), ("Durham", "NC", 27701), ("Winston-Salem", "NC", 27101), 
             ("Fargo", "ND", 58102), ("Bismarck", "ND", 58501), ("Grand Forks", "ND", 58201), ("Minot", "ND", 58701), ("West Fargo", "ND", 58078), 
             ("Columbus", "OH", 43215), ("Cleveland", "OH", 44113), ("Cincinnati", "OH", 45202), ("Toledo", "OH", 43604), ("Akron", "OH", 44308),
             ("Oklahoma City", "OK", 73102), ("Tulsa", "OK", 74103), ("Norman", "OK", 73069), ("Broken Arrow", "OK", 74012), ("Lawton", "OK", 73501),
             ("Portland", "OR", 97201), ("Salem", "OR", 97301), ("Eugene", "OR", 97401), ("Gresham", "OR", 97030), ("Hillsboro", "OR", 97124),
             ("Philadelphia", "PA", 19103), ("Pittsburgh", "PA", 15222), ("Harrisburg", "PA", 17101), ("Erie", "PA", 16501), ("Allentown", "PA", 18102),
             ("Providence", "RI", "02903"), ("Warwick", "RI", "02886"), ("Cranston", "RI", "02920"), ("Pawtucket", "RI", "02860"), ("East Providence", "RI", "02914"),
             ("Columbia", "SC", 29201), ("Charleston", "SC", 29401), ("North Charleston", "SC", 29405), ("Mount Pleasant", "SC", 29464), ("Rock Hill", "SC", 29730),
             ("Sioux Falls", "SD", 57104), ("Rapid City", "SD", 57701), ("Aberdeen", "SD", 57401),
             ("Nashville", "TN", 37203), ("Memphis", "TN", 38103), ("Knoxville", "TN", 37902),
             ("Houston", "TX", 77002), ("Dallas", "TX", 75201), ("Austin", "TX", 78701), ("San Antonio", "TX", 78205), ("Fort Worth", "TX", 76102),
             ("Salt Lake City", "UT", 84111), ("Provo", "UT", 84601), 
             ("Burlington", "VT", "05401"), ("Rutland", "VT", "05701"), 
             ("Virginia Beach", "VA", 23451), ("Richmond", "VA", 23220), ("Norfolk", "VA", 23510), ("Alexandria", "VA", 22314), ("Chesapeake", "VA", 23320),
             ("Seattle", "WA", 98101), ("Spokane", "WA", 99201), ("Tacoma", "WA", 98402), 
             ("Charleston", "WV", 25301), ("Huntington", "WV", 25701), 
             ("Milwaukee", "WI", 53202), ("Madison", "WI", 53703), ("Green Bay", "WI", 54301),
             ("Cheyenne", "WY", 82001), ("Casper", "WY", 82601)]

cur.execute("DROP TABLE IF EXISTS zip_code_data")
cur.execute("CREATE TABLE IF NOT EXISTS zip_code_data (city TEXT, state TEXT, zip_code TEXT)")

for city_val, state_val, zip_code_val in zip_codes:
    cur.execute("INSERT OR IGNORE INTO zip_code_data (city, state, zip_code) VALUES (?, ?, ?)",
               (city_val, state_val, zip_code_val))
conn.commit()

cur.close()
conn.close()