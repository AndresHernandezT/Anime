from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE Animes 
           (id serial PRIMARY KEY, nombre varchar(40), cant_capitulos integer, tipo varchar(40), autor_id integer, estudio_id integer);
"""

cur.execute(sql)


sql ="""
CREATE TABLE Estados 
           (anime_id serial PRIMARY KEY, tipo_de_estado varchar(40), fecha_emision varchar(10), fecha_termino varchar(10));
"""

cur.execute(sql)

sql ="""
CREATE TABLE Animes_generos 
           (anime_id integer, genero_id integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE  Autores
           (id serial PRIMARY KEY, nombre varchar(40));
"""

cur.execute(sql)

sql ="""
CREATE TABLE Estudios
           (id serial PRIMARY KEY, nombre varchar(140));
"""

cur.execute(sql)

sql = """CREATE TABLE Personajes
           (id serial PRIMARY KEY, nombre varchar(140));
"""

cur.execute(sql)

sql = """CREATE TABLE Animes_personajes
           (anime_id integer, personajes_id integer);
"""

cur.execute(sql)



conn.commit()
cur.close()
conn.close()
