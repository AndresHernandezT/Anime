from app import app
from flask import render_template
from configuraciones import *

import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/animes')
def animes():
	sql = "select * from Animes"
	cur.execute(sql)
	resultados = cur.fetchall()
	print resultados
	final = ""
	for i in resultados:
		final += str(i[1]) + "<br/>"
	return final

@app.route('/adios')
def adios():
        return "No me quiero venir, senores homeros"

@app.route('/animes/<int:id>')
def animes_id(id):
	sql = "select nombre from Animes where id = " + str(id)
	cur.execute(sql)
	resultados = cur.fetchall()
	return str(resultados[0][0])
