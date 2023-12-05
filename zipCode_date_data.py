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
    for zip_code in zip_codes:
        state_id = zip_code[0]
        zip_code_num = zip_code[1]
        cur.execute("INSERT OR IGNORE INTO zip_code_data (state_id, zip_code) VALUES (?, ?)",
                (state_id, zip_code_num))
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

cur.execute("CREATE TABLE IF NOT EXISTS dates (day_id INTEGER PRIMARY KEY, date TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS zip_code_data (zip_code_id INTEGER PRIMARY KEY, state_id INTEGER, zip_code TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS states (state_id INTEGER PRIMARY KEY, state TEXT)")

create_dates_table(cur, conn)
cur.execute("SELECT * FROM zip_code_data")
check_row = cur.fetchall()
if len(check_row) == 100:
    exit()
create_states_table(cur, conn, states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL",
                                         "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
                                         "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
                                         "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])
create_zip_code_table(cur, conn, zip_codes = [(1, 35211), (1, 36117),
                                            (2, 99504), (2, 99709),
                                            (3, 85032), (3, 85710),
                                            (4, 72204), (4, 72903),
                                            (5, 90011), (5, 92154),
                                            (6, 80219), (6, 80918),
                                            (7, "06606"), (7, "06511"),
                                            (8, 19805), (8, 19901),
                                            (9, 32210), (9, 33186),
                                            (10, 30318), (10, 30906),
                                            (11, 96815), (11, 96782),
                                            (12, 83709), (12, 83646),
                                            (13, 60629), (13, 60506),
                                            (14, 46227), (14, 46815),
                                            (15, 50315), (15, 52402),
                                            (16, 67212), (16, 66212),
                                            (17, 40214), (17, 40517),
                                            (18, 70119), (18, 70809),
                                            (19, "04101"), (19, "04240"),
                                            (20, 21215), (20, 21701),
                                            (21, "02124"), (21, "01604"),
                                            (22, 48219), (22, 49504),
                                            (23, 55407), (23, 55106),
                                            (24, 39212), (24, 39503),
                                            (25, 64118), (25, 63116),
                                            (26, 59102), (26, 59801),
                                            (27, 68104), (27, 68503),
                                            (28, 89103), (28, 89014),
                                            (29, "03101"), (29, "03060"),
                                            (30, "07102"), (30, "07302"),
                                            (31, 87102), (31, 88001),
                                            (32, 10019), (32, 14201),
                                            (33, 28202), (33, 27601),
                                            (34, 58102), (34, 58501),
                                            (35, 43215), (35, 44113),
                                            (36, 73102), (36, 74103),
                                            (37, 97201), (37, 97301),
                                            (38, 19103), (38, 15222),
                                            (39, "02903"), (39, "02886"),
                                            (40, 29201), (40, 29401),
                                            (41, 57104), (41, 57701),
                                            (42, 37203), (42, 38103),
                                            (43, 77002), (43, 75201),
                                            (44, 84111), (44, 84601),
                                            (45, "05401"), (45, "05701"),
                                            (46, 23451), (46, 23220),
                                            (47, 98101), (47, 99201),
                                            (48, 25301), (48, 25701),
                                            (49, 53202), (49, 53703),
                                            (50, 82001), (50, 82601)])

conn.close()