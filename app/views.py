from app import app
from flask import render_template
from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


@app.route('/')
@app.route('/index')
def index():
	sql = "select * from Animes"
	cur.execute(sql)
	resultados = cur.fetchall()
	print resultados
	return resultados[0][2]

@app.route('/adios')
def adios():
        return "No me quiero venir, senores homeros"

