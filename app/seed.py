from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()
sql ="""
insert into animes (id,nombre,cant_capitulos,tipo,autor_id,estudio_id) values ('Death Note','37','Anime','1','1') returning id;
"""
cur.execute(sql)


sql ="""
conn.commit()
post_id = cur.fetchone()[0]

print post_idinsert into estados (anime_id,tipo_de_estado,fecha_emision,fecha_termino) values ('Finalizado','03/10/2006','26/06/2007') returning anime_id;
"""
cur.execute(sql)

sql ="""
insert into autores (id,nombre) values ('Tsugumi Ohba')returning id;
"""
cur.execute(sql)

sql ="""
insert into estudios (id,nombre) values ('Madhouse') returning id;
"""
cur.execute(sql)

conn.commit()
post_id = cur.fetchone()[0]

print post_id

cur.execute(sql)


conn.commit()
cur.close()
conn.close()
