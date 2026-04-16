#!/usr/bin/env python3
import pymysql

print("Content-Type: text/html; charset=utf-8\n")

print("<html><head><meta charset='UTF-8'><title>Contacts (DB)</title>")
print("<style>")
print("table { border-collapse: collapse; width: 300px; }")
print("th, td { border: 1px solid #000; padding: 5px; text-align: left; }")
print("</style></head><body>")
print("<h2>연락처</h2>")
print("<table>")
print("<tr><th>이름</th><th>전화번호</th></tr>")

# Kết nối DB
conn = pymysql.connect(
    host="localhost",
    user="webuser",
    password="1234",
    database="contactsdb",
    charset="utf8"
)

cur = conn.cursor()
cur.execute("SELECT name, phone FROM contacts")

for name, phone in cur.fetchall():
    print(f"<tr><td>{name}</td><td>{phone}</td></tr>")

print("</table></body></html>")

cur.close()
conn.close()

