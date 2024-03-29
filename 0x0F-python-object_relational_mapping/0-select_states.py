#!/usr/bin/python3
"""
Lists all states from database hbtn_0e_0_usa
Usage: script takes 3 arguments; username, password and db
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
