from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into animes (nombre,cant_capitulos,tipo,autor_id,estudio_id) values ('Death Note','37','Anime','1','1') returning id;
"""
cur.execute(sql)

sql ="""
insert into estados (anime_id,tipo_de_estado,fecha_emision,fecha_termino) values ('1','Finalizado','03/10/2006','26/06/2007');
"""
cur.execute(sql)

sql ="""
insert into autores (nombre) values ('Tsugumi Ohba') returning id;
"""
cur.execute(sql)

sql ="""
insert into estudios (nombre) values ('Madhouse'), ('TV tokio'), ('Studio Ghibli'), ('8-bit'),('Bandai Namco Pictures') returning id;
"""
cur.execute(sql)

sql ="""
insert into generos (nombre) values ('Accion'), ('Ciencia Ficcion'), ('Deportes'), ('Espacial'), ('Infantil'), ('Mecha'), ('Parodia'), ('Romance'), ('Shounen'), ('Terror'), ('Artes Marciales'), ('Comedia'), ('Drama'), ('Fantasia'), ('Josei'), ('Militar'), ('Policia'), ('Samurai'), ('Sobrenatural'), ('Vampiros'), ('Aventuras'), ('Demencia'), ('Ecchi'), ('Harem'), ('Juegos'), ('Misterio'), ('Psicologico'), ('Seinen'), ('Superpoderes'), ('Yaoi'), ('Carreras'), ('Demonios'), ('Escolares'), ('Historico'), ('Magia'), ('Musica'), ('Recuentos de la vida'), ('Shoujo'), ('Suspenso'), ('Yuri') returning id;
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
