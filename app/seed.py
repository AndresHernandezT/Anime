from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()
sql ="""
insert into animes (id,nombre,cant_capitulos,tipo,autor_id,estudio_id) values 
('Death Note','38','Anime','1','1'),('Watashi ga Motete Dousunda','12','Anime',' ',' '), 
('Orange','13','Anime',' ',' '), ('Ore Monogatarti!!','24','Anime',' ',' '), 
('Akatsuki no Yona','24','Anime',' ',' '),('Neon Genesis Evangelion','26','Anime',' ',' '),
('Maho Shojo Madoka Magica','12','Anime',' ',' '),('Elfen Lied','13','Anime',' ',' '),
('Kotonoha no Niwa','1','Pelicula',' ',' '),('Hotarubi no Mori e','1','Pelicula',' ',' '),
('Kimi no Na wa','1','Pelicula',' ',' '),('Sen to Chihiro no Kamikakushi','1','Pelicula',' ',' '),
('Yahari Ore no Seishun Love Comedy wa Machigatteiru. Zoku','13','Anime',' ',' '),
('Yahari Ore no Seishun Love Come wa Machigatteiru','13','Anime',' ',' '),
('Yahari Ore no Seishun Love Comedy wa Machigatteiru.OVA','1','Ova',' ',' '),
('Hori-san to Miyamura-kun','3','Ova',' ',' '),('ToraDora!','25','Anime',' ',' '),
('Toradora!: Bentou no Gokui','1','Ova',' ',' '),('Boruto: Naruto Next Generations','65','Anime',' ',' '),
('Naruto Shippuden','500','Anime',' ',' '),('Naruto','220','Anime',' ',' '),
('One Piece','844','Anime',' ',' '),('Terra Formars','13','Anime',' ',' '),
('Terra Formars: Revenge','13','Anime',' ',' '),('Terra Formars OVA','2','Ova',' ',' '),
('Boku no Hero Academia','15','Anime',' ',' '),('Boku no Hero Academia 2nd Season','25','Anime',' ',' '),
('Boku no Hero Academia 3rd Season','14','Anime',' ',' '),('Cowboy Bebop','26','Anime',' ',' '),
('Cowboy Bebop: Tengoku no Tobira','1','Pelicula',' ',' '),('Samurai Champloo','26','Anime',' ',' '),
('Code Geass','25','Anime',' ',' '),('Code Geass: R2','25','Anime',' ',' '),
('Code Geass: Nunnally in Wonderland','1','Ova',' ',' '),('Boku dake ga Inai Machi','12','Anime',' ',' '),
('Sakura Card Captor','70','Anime',' ',' '),('Cardcaptor Sakura: Clear Card-hen','22','Anime',' ',' '),
('Sakura Card Captor: Clear Card-hen - Prologue Sakura to Futatsu no Kuma','1','Ova',' ',' '),
('Fukumenkei Noise','12','Anime',' ',' '), ('Fuuka','12','Anime',' ',' '),
('Sakamichi no Apollon','12','Anime',' ',' ') returning id;
"""
cur.execute(sql)

sql ="""
conn.commit()
post_id = cur.fetchone()[0]

print post_idinsert into estados (anime_id,tipo_de_estado,fecha_emision,fecha_termino) values ('1','Finalizado','03/10/2006','26/06/2007') returning anime_id;
"""
cur.execute(sql)

sql ="""
insert into autores (id,nombre) values ('Tsugumi Ohba')returning id;
"""
cur.execute(sql)

sql ="""
insert into estudios (id,nombre) values ('Madhouse'), ('TV tokio'), ('śtudio ghibli'), ('8-bit'),('bandai namco pictures') returning id;
"""
cur.execute(sql)

sql ="""
insert into generos (id,nombre) values ('Accion'), ('Ciencia Ficcion'), ('Deportes'), ('Espacial'), ('Infantil'), ('Mecha'), ('Parodia'), ('Romance'), ('Shounen'), ('Terror'), ('Artes Marciales'), ('Comedia'), ('Drama'), ('Fantasia'), ('Josei'), ('Militar'), ('Policia'), ('Samurai'), ('Sobrenatural'), ('Vampiros'), ('Aventuras'), ('Demencia'), ('Ecchi'), ('Harem'), ('Juegos'), ('Misterio'), ('Psicologico'), ('Seinen'), ('Superpoderes'), ('Yaoi'), ('Carreras'), ('Demonios'), ('Escolares'), ('Historico'), ('Magia'), ('Musica'), ('Recuentos de la vida'), ('Shoujo'), ('Suspenso'), ('Yuri') returning id;
"""
cur.execute(sql)

conn.commit()
post_id = cur.fetchone()[0]

print (post_id)

cur.execute(sql)


conn.commit()
cur.close()
conn.close()
