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
insert into estados (anime_id,tipo_de_estado,fecha_emision,fecha_termino) values ('1','Finalizado','03/10/2006','26/06/2007') returning anime_id;
"""
cur.execute(sql)

sql ="""
insert into autores (id,nombre) values 
('Tsugumi Ohba'), 
('Junko'), 
('Ichigo Takano'), 
('Kazune Kawahara'), 
('Mizuho Kusanagi'), 
('Hideaki Anno'), 
('Gen Urobuchi'), 
('Lynn Okamoto'), 
('Makoto Shinkai'), 
('Yuki Midorikawa'), 
('Hayao Miyazaki'), 
('Wataru Watari'), 
('HERO'), 
('Yuyuko Takemiya'), 


returning id;
"""
cur.execute(sql)

sql ="""
insert into estudios (id,nombre) values 
('Madhouse'), 
('TV tokio'), 
('Studio Ghibli'), 
('8-bit'), 
('bandai namco pictures'), 
('Brain's Base'), 
('TMS Entertainment'), 
('Pierrot')
('Gainax'), 
('Shaft'), 
('Arms Corporation'), 
('CoMix Wave Films'), 
('feel'), 
('Hoods Entertainment'), 
('J.C.Staff'), 


returning id;
"""
cur.execute(sql)

sql ="""
insert into generos (id,nombre) values ('Accion'), ('Ciencia Ficcion'), ('Deportes'), ('Espacial'), ('Infantil'), ('Mecha'), 
('Parodia'), ('Romance'), ('Shounen'), ('Terror'), ('Artes Marciales'), ('Comedia'), ('Drama'), ('Fantasia'), ('Josei'), 
('Militar'), ('Policia'), ('Samurai'), ('Sobrenatural'), ('Vampiros'), ('Aventuras'), ('Demencia'), ('Ecchi'), ('Harem'), 
('Juegos'), ('Misterio'), ('Psicologico'), ('Seinen'), ('Superpoderes'), ('Yaoi'), ('Carreras'), ('Demonios'), ('Escolares'), 
('Historico'), ('Magia'), ('Musica'), ('Recuentos de la vida'), ('Shoujo'), ('Suspenso'), ('Yuri') returning id;
"""
cur.execute(sql)

sql ="""
insert into animes_generos (anime_id,genero_id) values 
('1','26'),('1','17'),('1','27'),('1','19'),('1','39'),
('2','12'),('2','33'),('2','24'),('2','8'),('2','38'),
('3','2'), ('3','13'), ('3','33'), ('3','8'), ('3','38'),
('4','12'), ('4','8'), ('4','38'),
('5','1'), ('5','21'),('5','12'),('5','14'),('5','8'),('5','38'),
('6','1'), ('6','2'), ('6','22'), ('6','13'), ('6','6'), ('6','27'),
('7','13'), ('7','35'), ('7','27'), ('7','39'),
('8','1'), ('8','13'), ('8','27'), ('8','8'), ('8','28'), ('8','19'), ('8','10'),
('9','13'), ('9','27'), ('9','37'), ('9','8'),
('10','13'), ('10','8'), ('10','38'), ('10','19'), 
('11','13'), ('11','33'), ('11','8'),('11','19'),
('12','21'), ('12','13'), ('12','19'), 
('13','12'), ('13','13'), ('13','33'), ('13','8'), 
('14','12'), ('14','13'), ('14','33'), ('14','8')
('15','12'), ('15','33'), ('15','8'),
('16',''), ('16',''), ('16',''), ('16',''), (Hori-san to Miyamura-kun)
returning id;
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
