from configuraciones import *
import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE Animes
           (id serial PRIMARY KEY, nombre varchar(80), cant_capitulos integer, tipo varchar(40), autor_id integer, estudio_id integer);
"""

cur.execute(sql)


sql ="""
CREATE TABLE Estados
           (anime_id integer PRIMARY KEY, tipo_de_estado varchar(40), fecha_emision varchar(10), fecha_termino varchar(10));
"""

cur.execute(sql)

sql ="""
CREATE TABLE Animes_generos
           (anime_id integer, genero_id integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE  Autores
           (id serial PRIMARY KEY, nombre varchar(140));
"""

cur.execute(sql)

sql ="""
CREATE TABLE Estudios
           (id serial PRIMARY KEY, nombre varchar(140));
"""

cur.execute(sql)

sql = """
CREATE TABLE Personajes
           (id serial PRIMARY KEY, nombre varchar(140));
"""

cur.execute(sql)

sql = """
CREATE TABLE Animes_personajes
           (anime_id integer, personaje_id integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE Generos
	(id serial PRIMARY KEY, nombre varchar(40));
"""

cur.execute(sql)


conn.commit()
cur.close()
conn.close()
