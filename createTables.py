#! python
import sqlite3
conn = sqlite3.connect('data.db');
c = conn.cursor();
c.execute('CREATE TABLE sensors(light text, hum text, temp text, meas_date text PRIMARY KEY)');
conn.commit();
conn.close();
