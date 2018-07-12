from app import app
from flask import render_template
from configuraciones import *

import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	return render_template('index.html',generos=generos)

@app.route('/animes')
def animes():
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Animes"
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('index.html',animes=animes,generos=generos)

@app.route('/categorias')
def categorias():
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	return render_template('categorias.html',generos=generos)

@app.route('/personajes')
def personajes():
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Personajes"
	cur.execute(sql)
	personajes = cur.fetchall()
	return render_template('personajes.html',generos=generos,personajes=personajes)

@app.route('/autores')
def autores():
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Autores"
	cur.execute(sql)
	autores = cur.fetchall()
	return render_template('autores.html',generos=generos,autores=autores)

@app.route('/estudios')
def estudios():
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Estudios"
	cur.execute(sql)
	estudios = cur.fetchall()
	return render_template('estudios.html',generos=generos,estudios=estudios)

@app.route('/categorias/<int:id>')
def categorias_id(id):
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select nombre from Generos where id = " + str(id)
	cur.execute(sql)
	resultado = cur.fetchall()
	sql = "select * from Animes, Generos, Animes_Generos where anime_id = Animes.id and genero_id = Generos.id and Generos.id = " + str(id)
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('categorias_id.html',animes=animes,generos=generos)

@app.route('/animes/<int:id>')
def animes_id(id):
	sql = "select * from Animes where id = " + str(id)
	cur.execute(sql)
	anime = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Personajes, Animes_Personajes where anime_id = " + str(id) + " and Personajes.id = personaje_id"
	cur.execute(sql)
	personajes = cur.fetchall()
	sql = "select * from Generos, Animes_Generos where anime_id = " + str(id) + " and Generos.id = genero_id"
	cur.execute(sql)
	categorias = cur.fetchall()
	sql = "select * from Estudios, Animes where Estudios.id = estudio_id and Animes.id = " + str(id) 
	cur.execute(sql)
	estudio = cur.fetchall()
	sql = "select * from Autores, Animes where Autores.id = autor_id and Animes.id = " + str(id)
	cur.execute(sql)
	autor = cur.fetchall()
	sql = "select * from Estados where anime_id = " + str(id)
	cur.execute(sql)
	estado = cur.fetchall()
	return render_template('animes_id.html',generos=generos,anime=anime,personajes=personajes,categorias=categorias,estudio=estudio,autor=autor,estado=estado)

@app.route('/buscar/results?key=<keyword>')
def search(keyword):
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = """ select * from Animes where nombre like '%{perra}%'"""
	perra = "Death"
	cur.execute(sql)
	resultados = cur.fetchall()
	return render_template('buscar.html',generos=generos,resultados=resultados)
