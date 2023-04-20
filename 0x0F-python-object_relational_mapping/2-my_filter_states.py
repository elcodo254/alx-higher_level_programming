#!/usr/bin/python3
"""
takes in an argument and displays all values in states table from database hbtn_0e_0_usa
Usage: script takes 4 arguments; username, password, db and state name searched
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost", passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
    cur.close()
    db.close()
