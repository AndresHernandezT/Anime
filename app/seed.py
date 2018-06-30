from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()
sql ="""
insert into animes (id,nombre,cant_capitulos,tipo,autor_id,estudio_id) values 
('Death Note','38','Anime','1','1'), 
('Watashi ga Motete Dousunda'.'12','anime','2','6'), 
('Orange','13','anime','3','7'), 
('Ore Monogatarti!!','24','Anime','4','1'), 
('Akatsuki no Yona','24','Anime','5','8'), 
('Neon Genesis Evangelion','26','Anime','6','9'),
('Maho Shojo Madoka Magica','12','Anime','7','10'), 
('Elfen Lied','13','Anime','8','11'),
('Kotonoha no Niwa','1','Pelicula','9','12'), 
('Hotarubi no Mori e','1','Pelicula','10','6'), 

('Kimi no Na wa','1','Pelicula','9','12'), 
('Sen to Chihiro no Kamikakushi','1','Pelicula','11','3'), 
('Yahari Ore no Seishun Love Come wa Machigatteiru. Zoku','13','Anime','12','13'), 
('Yahari Ore no Seishun Love Come wa Machigatteiru','13','Anime','12','6'), 
('Yahari Ore no Seishun Love Come wa Machigatteiru.OVA','1','Ova','12','6'), 
('Hori-san to Miyamura-kun','3','Ova','13','14'), 
('ToraDora!','25','Anime','14','15'), 
('Toradora!: Bentou no Gokui','1','Ova','14','15'), 
('Boruto: Naruto Next Generations','65','Anime','15','8'), 
('Naruto Shippuden','500','Anime','16','8'), 

('Naruto','220','Anime','16','8'), 
('One Piece','844','Anime','17','16'), 
('Terra Formars','13','Anime','18','17'), 
('Terra Formars: Revenge','13','Anime','18','17'), 
('Terra Formars OVA','2','Ova','18','17'), 
('Boku no Hero Academia','15','Anime','19','18'), 
('Boku no Hero Academia 2nd Season','25','Anime','19','18'), 
('Boku no Hero Academia 3rd Season','14','Anime','19','18'), 
('Cowboy Bebop','26','Anime','20','19'), 
('Cowboy Bebop: Tengoku no Tobira','1','Pelicula','20','19'), 

('Samurai Champloo','26','Anime','20','20'), 
('Code Geass','25','Anime','21','19'), 
('Code Geass: R2','25','Anime','21','19'), 
('Code Geass: Nunnally in Wonderland','1','Ova','21','19'), 
('Boku dake ga Inai Machi','12','Anime','22','21'), 
('Sakura Card Captor','70','Anime','23','1'), 
('Cardcaptor Sakura: Clear Card-hen','22','Anime','23','1'), 
('Sakura Card Captor: Clear Card-hen - Prologue Sakura to Futatsu no Kuma','1','Ova','23','1'), 
('Fukumenkei Noise','12','Anime','24','6'), 
('Fuuka','12','Anime','25','22'), 

('Sakamichi no Apollon','12','Anime','26','23')

returning id;
"""
cur.execute(sql)


sql ="""
conn.commit()
post_id = cur.fetchone()[0]

print post_idinsert into estados (anime_id,tipo_de_estado,fecha_emision,fecha_termino) values 
('Finalizado','03/10/2006','26/06/2007') 

returning anime_id;
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
('Ukyo Kodachi'), 
('Masashi Kishimoto'), 
('Eiichirō Oda'), 
('Yu Sasuga'), 
('Kōhei Horikoshi'), 
('Shinichiro Watanabe'), 
('Goro Taniguchi'), 
('Kei Sanbe'), 
('CLAMP'), 
('Ryoko Fukuyama'), 
('Kouji Seo'), 
('Yuki Kodama')


returning id;
"""
cur.execute(sql)

sql ="""
insert into estudios (id,nombre) values 
('Madhouse'), 
('TV tokio'), 
('Studio Ghibli'), 
('8-bit'), 
('Bandai Namco Pictures'), 
('Brain's Base'), 
('TMS Entertainment'), 
('Pierrot'), 
('Gainax'), 
('Shaft'), 

('Arms Corporation'), 
('CoMix Wave Films'), 
('feel'), 
('Hoods Entertainment'), 
('J.C.Staff'), 
('Toei Animation'), 
('Liden Films'), 
('Bones'), 
('Sunrise'), 
('Manglobe'),

('A-1 Pictures'), 
('Diomedéa'), 
('MAPPA')


returning id;
"""
cur.execute(sql)

conn.commit()
post_id = cur.fetchone()[0]

print (post_id)

cur.execute(sql)


conn.commit()
cur.close()
conn.close()
