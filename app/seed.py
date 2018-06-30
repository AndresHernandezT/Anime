from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()
sql ="""
insert into animes (id,nombre,cant_capitulos,tipo,autor_id,estudio_id) values ('Death Note','38','Anime','1','1') returning id;
"""
cur.execute(sql)


sql ="""
conn.commit()
post_id = cur.fetchone()[0]

print post_idinsert into estados (anime_id,tipo_de_estado,fecha_emision,fecha_termino) values ('Finalizado','03/10/2006','26/06/2007') returning anime_id;
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
