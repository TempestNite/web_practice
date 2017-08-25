import sqlite3

from flask import g

DATABASE = 'C:\\Users\\Tempest\\PycharmProjects\\unk\\user.db'

def commit_db (cmd, values):
    userDB = sqlite3.connect(DATABASE)
    cur = userDB.cursor()
    cur.execute(cmd, values)
    userDB.commit()
    userDB.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db (query, args, one=True):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

