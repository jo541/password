from flask import Flask
app = Flask(__name__)

import psycopg2
conn = psycopg2.connect(dbname="password")
cr = conn.cursor()
import server.index
import server.page2
