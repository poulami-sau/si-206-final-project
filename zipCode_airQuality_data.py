import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
db_filename = dir_path + '/zipCode_airQuality.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

zip_codes = [("Birmingham", "AL", 35211), ("Montgomery", "AL", 36117),
            ("Anchorage", "AK", 99504), ("Fairbanks", "AK", 99709),
            ("Phoenix", "AZ", 85032), ("Tucson", "AZ", 85710),
            ("Little Rock", "AR", 72204), ("Fort Smith", "AR", 72903),
            ("Los Angeles", "CA", 90011), ("San Diego", "CA", 92154),
            ("Denver", "CO", 80219), ("Colorado Springs", "CO", 80918),
            ("Bridgeport", "CT", "06606"), ("New Haven", "CT", "06511"),
            ("Wilmington", "DE", 19805), ("Dover", "DE", 19901),
            ("Jacksonville", "FL", 32210), ("Miami", "FL", 33186),
            ("Atlanta", "GA", 30318), ("Augusta", "GA", 30906),
            ("Honolulu", "HI", 96815), ("Pearl City", "HI", 96782),
            ("Boise", "ID", 83709), ("Meridian", "ID", 83646),
            ("Chicago", "IL", 60629), ("Aurora", "IL", 60506),
            ("Indianapolis", "IN", 46227), ("Fort Wayne", "IN", 46815),
            ("Des Moines", "IA", 50315), ("Cedar Rapids", "IA", 52402),
            ("Wichita", "KS", 67212), ("Overland Park", "KS", 66212),
            ("Louisville", "KY", 40214), ("Lexington", "KY", 40517),
            ("New Orleans", "LA", 70119), ("Baton Rouge", "LA", 70809),
            ("Portland", "ME", "04101"), ("Lewiston", "ME", "04240"),
            ("Baltimore", "MD", 21215), ("Frederick", "MD", 21701),
            ("Boston", "MA", "02124"), ("Worcester", "MA", "01604"),
            ("Detroit", "MI", 48219), ("Grand Rapids", "MI", 49504),
            ("Minneapolis", "MN", 55407), ("Saint Paul", "MN", 55106),
            ("Jackson", "MS", 39212), ("Gulfport", "MS", 39503),
            ("Kansas City", "MO", 64118), ("Saint Louis", "MO", 63116),
            ("Billings", "MT", 59102), ("Missoula", "MT", 59801),
            ("Omaha", "NE", 68104), ("Lincoln", "NE", 68503),
            ("Las Vegas", "NV", 89103), ("Henderson", "NV", 89014),
            ("Manchester", "NH", "03101"), ("Nashua", "NH", "03060"),
            ("Newark", "NJ", "07102"), ("Jersey City", "NJ", "07302"),
            ("Albuquerque", "NM", 87102), ("Las Cruces", "NM", 88001),
            ("New York City", "NY", 10019), ("Buffalo", "NY", 14201),
            ("Charlotte", "NC", 28202), ("Raleigh", "NC", 27601),
            ("Fargo", "ND", 58102), ("Bismarck", "ND", 58501),
            ("Columbus", "OH", 43215), ("Cleveland", "OH", 44113),
            ("Oklahoma City", "OK", 73102), ("Tulsa", "OK", 74103),
            ("Portland", "OR", 97201), ("Salem", "OR", 97301),
            ("Philadelphia", "PA", 19103), ("Pittsburgh", "PA", 15222),
            ("Providence", "RI", "02903"), ("Warwick", "RI", "02886"),
            ("Columbia", "SC", 29201), ("Charleston", "SC", 29401),
            ("Sioux Falls", "SD", 57104), ("Rapid City", "SD", 57701),
            ("Nashville", "TN", 37203), ("Memphis", "TN", 38103),
            ("Houston", "TX", 77002), ("Dallas", "TX", 75201),
            ("Salt Lake City", "UT", 84111), ("Provo", "UT", 84601),
            ("Burlington", "VT", "05401"), ("Rutland", "VT", "05701"),
            ("Virginia Beach", "VA", 23451), ("Richmond", "VA", 23220),
            ("Seattle", "WA", 98101), ("Spokane", "WA", 99201),
            ("Charleston", "WV", 25301), ("Huntington", "WV", 25701),
            ("Milwaukee", "WI", 53202), ("Madison", "WI", 53703),
            ("Cheyenne", "WY", 82001), ("Casper", "WY", 82601)]

cur.execute("DROP TABLE IF EXISTS zip_code_data")
cur.execute("CREATE TABLE IF NOT EXISTS zip_code_data (zip_code_id INTEGER PRIMARY KEY, city TEXT, state TEXT, zip_code TEXT)")

for city_val, state_val, zip_code_val in zip_codes:
    cur.execute("INSERT OR IGNORE INTO zip_code_data (city, state, zip_code) VALUES (?, ?, ?)",
               (city_val, state_val, zip_code_val))
conn.commit()


dates = [(1, "2023-11-17"), (2, "2023-11-18"), (3, "2023-11-19"), (4, "2023-11-20"), 
         (5, "2023-11-21"), (6, "2023-11-22"), (7, "2023-11-23")]

cur.execute("DROP TABLE IF EXISTS dates")
cur.execute("CREATE TABLE IF NOT EXISTS dates (day INTEGER, date TEXT)")

for date_num, date_text in dates:
    cur.execute("INSERT OR IGNORE INTO dates (day, date) VALUES (?, ?)", (date_num, date_text))
conn.commit()

cur.close()
conn.close()