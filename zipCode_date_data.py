import os
import sqlite3
from datetime import date


def connect_database():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_filename = dir_path + '/zipCode_airQuality.db'
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    return cur, conn


def create_zip_code_table(cur, conn, zip_codes):
    for city_val, state_id, zip_code_val in zip_codes:
        cur.execute("INSERT OR IGNORE INTO zip_code_data (city, state_id, zip_code) VALUES (?, ?, ?)",
                (city_val, state_id, zip_code_val))
    conn.commit()


def create_dates_table(cur, conn):
    today = date.today()
    cur.execute("INSERT OR IGNORE INTO dates (date) VALUES (?)", (today,))
    conn.commit()


def create_states_table(cur, conn, states):
    for state_name in states:
        cur.execute("INSERT OR IGNORE INTO states (state) VALUES (?)", (state_name,))
    conn.commit()


cur, conn = connect_database()
cur.execute("CREATE TABLE IF NOT EXISTS zip_code_data (zip_code_id INTEGER PRIMARY KEY, city TEXT, state_id INTEGER, zip_code TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS dates (day_id INTEGER PRIMARY KEY, date TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS states (state_id INTEGER PRIMARY KEY, state TEXT)")
create_zip_code_table(cur, conn, zip_codes = [("Birmingham", 1, 35211), ("Montgomery", 1, 36117),
                                            ("Anchorage", 2, 99504), ("Fairbanks", 2, 99709),
                                            ("Phoenix", 3, 85032), ("Tucson", 3, 85710),
                                            ("Little Rock", 4, 72204), ("Fort Smith", 4, 72903),
                                            ("Los Angeles", 5, 90011), ("San Diego", 5, 92154),
                                            ("Denver", 6, 80219), ("Colorado Springs", 6, 80918),
                                            ("Bridgeport", 7, "06606"), ("New Haven", 7, "06511"),
                                            ("Wilmington", 8, 19805), ("Dover", 8, 19901),
                                            ("Jacksonville", 9, 32210), ("Miami", 9, 33186),
                                            ("Atlanta", 10, 30318), ("Augusta", 10, 30906),
                                            ("Honolulu", 11, 96815), ("Pearl City", 11, 96782),
                                            ("Boise", 12, 83709), ("Meridian", 12, 83646),
                                            ("Chicago", 13, 60629), ("Aurora", 13, 60506),
                                            ("Indianapolis", 14, 46227), ("Fort Wayne", 14, 46815),
                                            ("Des Moines", 15, 50315), ("Cedar Rapids", 15, 52402),
                                            ("Wichita", 16, 67212), ("Overland Park", 16, 66212),
                                            ("Louisville", 17, 40214), ("Lexington", 17, 40517),
                                            ("New Orleans", 18, 70119), ("Baton Rouge", 18, 70809),
                                            ("Portland", 19, "04101"), ("Lewiston", 19, "04240"),
                                            ("Baltimore", 20, 21215), ("Frederick", 20, 21701),
                                            ("Boston", 21, "02124"), ("Worcester", 21, "01604"),
                                            ("Detroit", 22, 48219), ("Grand Rapids", 22, 49504),
                                            ("Minneapolis", 23, 55407), ("Saint Paul", 23, 55106),
                                            ("Jackson", 24, 39212), ("Gulfport", 24, 39503),
                                            ("Kansas City", 25, 64118), ("Saint Louis", 25, 63116),
                                            ("Billings", 26, 59102), ("Missoula", 26, 59801),
                                            ("Omaha", 27, 68104), ("Lincoln", 27, 68503),
                                            ("Las Vegas", 28, 89103), ("Henderson", 28, 89014),
                                            ("Manchester", 29, "03101"), ("Nashua", 29, "03060"),
                                            ("Newark", 30, "07102"), ("Jersey City", 30, "07302"),
                                            ("Albuquerque", 31, 87102), ("Las Cruces", 31, 88001),
                                            ("New York City", 32, 10019), ("Buffalo", 32, 14201),
                                            ("Charlotte", 33, 28202), ("Raleigh", 33, 27601),
                                            ("Fargo", 34, 58102), ("Bismarck", 34, 58501),
                                            ("Columbus", 35, 43215), ("Cleveland", 35, 44113),
                                            ("Oklahoma City", 36, 73102), ("Tulsa", 36, 74103),
                                            ("Portland", 37, 97201), ("Salem", 37, 97301),
                                            ("Philadelphia", 38, 19103), ("Pittsburgh", 38, 15222),
                                            ("Providence", 39, "02903"), ("Warwick", 39, "02886"),
                                            ("Columbia", 40, 29201), ("Charleston", 40, 29401),
                                            ("Sioux Falls", 41, 57104), ("Rapid City", 41, 57701),
                                            ("Nashville", 42, 37203), ("Memphis", 42, 38103),
                                            ("Houston", 43, 77002), ("Dallas", 43, 75201),
                                            ("Salt Lake City", 44, 84111), ("Provo", 44, 84601),
                                            ("Burlington", 45, "05401"), ("Rutland", 45, "05701"),
                                            ("Virginia Beach", 46, 23451), ("Richmond", 46, 23220),
                                            ("Seattle", 47, 98101), ("Spokane", 47, 99201),
                                            ("Charleston", 48, 25301), ("Huntington", 48, 25701),
                                            ("Milwaukee", 49, 53202), ("Madison", 49, 53703),
                                            ("Cheyenne", 50, 82001), ("Casper", 50, 82601)])
create_dates_table(cur, conn)
create_states_table(cur, conn, states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL",
                                         "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
                                         "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
                                         "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])
conn.close()