#! python
import sqlite3
conn = sqlite3.connect('data.db');
import sys
sys.stdout.write("Data Base Opened \n");
c = conn.cursor();
c.execute('Select * from Sensors');

rows = c.fetchall();
for row in rows:
        print(row);

conn.close();
