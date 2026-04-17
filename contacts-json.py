#!/usr/bin/env python3
import pymysql
import json

print("Content-Type: application/json; charset=utf-8\n")

conn = pymysql.connect(
    host="localhost",
    user="webuser",
    password="1234",
    database="contactsdb",
    charset="utf8"
)
cur = conn.cursor()
cur.execute("SELECT name, phone, email FROM contacts")

rows = cur.fetchall()
data = [{"name": name, "telephone": phone, "email": email} for name, phone, email in rows]

result = {
    "ok": True,
    "count": len(data),
    "data": data
}

print(json.dumps(result, ensure_ascii=False))

cur.close()
conn.close()
