from configuraciones import *
import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))
cur = conn.cursor()
sql ="""
insert into animes (nombre,cant_capitulos,tipo,autor_id,estudio_id) values 
('Death Note','37','Anime','1','1'), 
('Watashi ga Motete Dousunda','12','Anime','2','6'), 
('Orange','13','Anime','3','7'), 
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
insert into estados (anime_id,tipo_de_estado,fecha_emision,fecha_termino) values 
('1','Finalizado','03/10/2006','26/06/2007'), 
('2','Finalizado','06/10/2016','22/12/2016'), 
('3','Finalizado','03/07/2016','25/09/2016'), 
('4','Finalizado','08/04/2015','23/09/2015'), 
('5','Finalizado','07/10/2014','24/03/2015'), 
('6','Finalizado','04/10/1995','27/03/1996'), 
('7','Finalizado','06/01/2011','21/04/2011'), 
('8','Finalizado','25/07/2004','17/10/2014'), 
('9','Finalizado','31/05/2014',''), 
('10','Finalizado','17/09/2011',''), 
('11','Finalizado','26/08/2016',''), 
('12','Finalizado','20/07/2001',''), 
('13','Finalizado','02/04/2015','25/06/2015'), 
('14','Finalizado','04/04/2013','27/06/2013'), 
('15','Finalizado','19/09/2013',''), 
('16','Finalizado','26/09/2012',''), 
('17','Finalizado','02/10/2008','26/03/2009'), 
('18','Finalizado','21/12/2011',''), 
('19','En emision','09/05/2016','-'), 
('20','Finalizado','15/02/2007','23/03/2017'), 
('21','Finalizado','03/10/2002','08/02/2007'), 
('22','En emision','20/10/1999','-'), 
('23','Finalizado','26/09/2014','19/12/2014'), 
('24','Finalizado','01/04/2016','24/06/2016'), 
('25','Finalizado','20/08/2014','28/11/2014'), 
('26','Finalizado','03/04/2016','26/06/2016'), 
('27','Finalizado','25/03/2017','30/09/2017'), 
('28','En emision','07/04/2018','-'), 
('29','Finalizado','03/04/1998','23/04/1999'), 
('30','Finalizado','01/09/2001',''), 
('31','Finalizado','14/05/2005','09/03/2006'), 
('32','Finalizado','05/10/2006','28/06/2007'), 
('33','Finalizado','06/04/2008','28/09/2008'), 
('34','Finalizado','27/07/2012',''), 
('35','Finalizado','08/01/2016','24/03/2016'), 
('36','Finalizado','07/04/1998','21/03/2000'), 
('37','Finalizado','07/01/2018','09/06/2018'), 
('38','Finalizado','13/09/2017',''), 
('39','Finalizado','11/04/2017','27/06/2017'), 
('40','Finalizado','06/01/2017','24/03/2017'), 
('41','Finalizado','12/04/2012','28/06/2012')
"""
cur.execute(sql)

sql ="""
insert into autores (nombre) values 
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
('Eiichirou Oda'), 
('Yu Sasuga'), 
('Kouhei Horikoshi'), 
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
insert into estudios (nombre) values 
('Madhouse'), 
('TV tokio'), 
('Studio Ghibli'), 
('8-bit'), 
('Bandai Namco Pictures'), 
('Brains Base'), 
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
('Diomedea'), 
('MAPPA')
returning id;
"""
cur.execute(sql)

sql ="""
insert into generos (nombre) values ('Accion'), ('Ciencia Ficcion'), ('Deportes'), ('Espacial'), ('Infantil'), ('Mecha'), 
('Parodia'), ('Romance'), ('Shounen'), ('Terror'), ('Artes Marciales'), ('Comedia'), ('Drama'), ('Fantasia'), ('Josei'), 
('Militar'), ('Policia'), ('Samurai'), ('Sobrenatural'), ('Vampiros'), ('Aventuras'), ('Demencia'), ('Ecchi'), ('Harem'), 
('Juegos'), ('Misterio'), ('Psicologico'), ('Seinen'), ('Superpoderes'), ('Yaoi'), ('Carreras'), ('Demonios'), ('Escolares'), 
('Historico'), ('Magia'), ('Musica'), ('Recuentos de la vida'), ('Shoujo'), ('Suspenso'), ('Yuri') 
returning id;
"""
cur.execute(sql)

sql ="""
insert into animes_generos (anime_id,genero_id) values 
('1','26'),  ('1','17'),  ('1','27'),  ('1','19'),('1','39'),
('2','12'),  ('2','33'),  ('2','24'),  ('2','8'), ('2','38'),
('3','2'),   ('3','13'),  ('3','33'),  ('3','8'), ('3','38'),
('4','12'),  ('4','8'),   ('4','38'),
('5','1'),   ('5','21'),  ('5','12'),  ('5','14'), ('5','8'),  ('5','38'),
('6','1'),   ('6','2'),   ('6','22'),  ('6','13'), ('6','6'),  ('6','27'),
('7','13'),  ('7','35'),  ('7','27'),  ('7','39'),
('8','1'),   ('8','13'),  ('8','27'),  ('8','8'),  ('8','28'), ('8','19'), ('8','10'),
('9','13'),  ('9','27'),  ('9','37'),  ('9','8'),
('10','13'), ('10','8'),  ('10','38'), ('10','19'), 
('11','13'), ('11','33'), ('11','8'),  ('11','19'),
('12','21'), ('12','13'), ('12','19'), 
('13','12'), ('13','13'), ('13','33'), ('13','8'), 
('14','12'), ('14','13'), ('14','33'), ('14','8'),
('15','12'), ('15','33'), ('15','8'),
('16','12'), ('16','33'), ('16','8'),  ('16','9'), 
('17','12'), ('17','33'), ('17','37'), ('17','8'), 
('18','12'), ('18','33'), ('18','37'), ('18','8'), 
('19','1'),  ('19','11'), ('19','21'), ('19','9'),  ('19','29'), 
('20','1'),  ('20','11'), ('20','12'), ('20','9'),  ('20','29'),  
('21','1'),  ('21','11'), ('21','12'), ('21','9'),  ('21','29'), 
('22','1'),  ('22','21'), ('22','12'), ('22','13'), ('22','14'), ('22','9'), ('22','29'), 
('23','1'),  ('23','2'),  ('23','13'), ('23','4'),  ('23','28'), ('23','10'), 
('24','1'),  ('24','2'),  ('24','13'), ('24','4'),  ('24','28'), ('24','10'), 
('25','1'),  ('25','2'),  ('25','13'), ('25','4'),  ('25','28'), ('25','10'), 
('26','1'),  ('26','12'), ('26','33'), ('26','9'),  ('26','29'), 
('27','1'),  ('27','12'), ('27','33'), ('27','9'),  ('27','29'), 
('28','1'),  ('28','12'), ('28','33'), ('28','9'),  ('28','29'), 
('29','1'),  ('29','21'), ('29','2'),  ('29','12'), ('29','13'), ('29','4'),  
('30','1'),  ('30','21'), ('30','2'),  ('30','12'), ('30','13'), ('30','4'), 
('31','1'),  ('31','21'), ('31','12'), ('31','34'), ('31','18'), ('31','9'), 
('32','1'),  ('32','2'),  ('32','33'), ('32','6'),  ('32','16'), ('32','29'), 
('33','1'),  ('33','2'),  ('33','13'), ('33','6'),  ('33','16'), ('33','29'), 
('34','12'), ('34','14'), ('34','7'),  
('35','26'), ('35','27'), ('35','28'), ('35','19'), 
('36','21'), ('36','12'), ('36','13'), ('36','33'), ('36','14'), ('36','35'), ('36','8'), ('36','38'),
('37','21'), ('37','12'), ('37','14'), ('37','35'), ('37','8'),  ('37','38'), 
('38','14'), ('38','35'), ('38','38'), 
('39','36'), ('39','8'),  ('39','38'), 
('40','13'), ('40','23'), ('40','33'), ('40','36'), ('40','8'),  ('40','9'),   
('41','13'), ('41','33'), ('41','15'), ('41','36'), ('41','8')
"""
cur.execute(sql)

sql ="""
insert into personajes (nombre) values  
('L. Lawliet'),        ('Light Yagami'),       ('Ryuk'),             ('Misa Amane'),    ('Nate River'),    ('Rem'),                    
('Nozomu Nanashima'),  ('Hayato Shinomiya'),   ('Yuusuke Igarashi'), ('Asuma Mutsumi'), ('Kae Serinuma'),  ('Shima Nishina'),          
('Naho Takamiya'),     ('Kakeru Naruse'),      ('Hiroto Suwa'),      ('Takako Chino'),  ('Saku Hagita'),   ('Azusa Murasaka'),         
('Makoto Sunakawa'),   ('Takeo Gouda'),        ('Rinko Yamato'),     ('Ai Sunakawa'),   ('Mariya Saijou'), ('Maki Gouda'),             
('Yona'),              ('Son Hak'),            ('Soo-Won'),          ('Yoon'),          ('Kija'),          ('Shin-Ah'),               
('Shinji Ikari'),      ('Rei Ayanami'),        ('Misato Katsuragi'), ('Kaworu Nagisa'), ('Toji Suzuhara'), ('Asuka Langley Soryu'),    
('Madoka Kaname'),     ('Homura Akemi'),       ('Kyubey'),           ('Sayaka Miki'),   ('Kyouko Sakura'), ('Mami Tomoe'),             
('Lucy'),              ('Nana'),               ('Mayu'),             ('Kouta'),         ('Yuka'),          ('Kurama'),                 
('Takao Akizuki'),     ('Yukari Yukino'),      ('Aizawa'),           ('Sato'),          ('Matsumoto'),     ('Takao no ani'),           
('Gin'),               ('Hotaru Takegawa'),                                                                                            
('Taki Tachibana'),    ('Mitsuha Miyamizu'),   ('Miki Okudera'),     ('Sayaka Natori'), ('Tsukasa Fujii'), ('Katsuhiko Teshigawara'),  
('Chihiro Ogino'),     ('Yubaba'),             ('Kamaji'),           ('Kaonashi'),      ('Lin'),           ('Nigihayami Kohaku Nushi'),
('Hachiman Hikigaya'), ('Yukino Yukinoshita'), ('Yui Yuigahama'),    ('Saika Totsuka'), ('Hayato Hayama'), ('Yoshiteru Zaimokuza'),    
('Izumi Miyamura'),    ('Kyoko Hori'),         ('Sota Hori'),        ('Yuri Yoshikawa'),('Toru Ishikawa'), ('Shu Iura'),               
('Ryuuji Takasu'),     ('Yusaku Kitamura'),    ('Minori Kushieda'),  ('Taiga Aisaka'),  ('Ami Kawashima'), ('Yasuko Takasu'),          
('Boruto Uzumaki'),    ('Sarada Uchiha'),      ('Himawari Uzumaki'), ('Mitsuki'),       ('Shikadai Nara'), ('Inojin Yamanaka'),        
('Naruto uzumaki'),    ('Sasuke Uchiha'),      ('Hinata Hyuga'),     ('sakura haruno'), ('Jiraiya'),       ('Kakashi Hatake'),         
('Monkey D. Luffy'),   ('Roronoa Zoro'),       ('Nami'),             ('Nico Robin'),    ('Vinsmoke Sanji'),('Tony Tony Chopper'),      
('Michelle K. Davis'), ('Akari Hizamaru'),     ('Shokichi Komachi'), ('Eva Frost'),     ('Marcos Garcia'),  ('Alex Stewart'),          
('Donatello K. Davis'),('Thien'),              ('Zhang Ming-Ming'),  ('Nanao Akita'),   ('Maria Viren'),                                       
('Izuku Midoriya'),    ('Katsuki Bakugou'),    ('Ochako Uraraka'),   ('Tsuyu Asui'),    ('Toshinori Yagi'), ('Shoto Todoroki'),        
('Spike Spiegel'),     ('Faye Valentine'),     ('Jet Black'),        ('Ed'),           ('Ein'),                                        
('Mugen'),             ('Jin'),                ('Fuu'),              ('Momo-san'),                                                      
('C.C'),               ('Kallen Kozuki'),     ('Suzaku Kururugi'),('Nunnally Lamperouge'),('Shirley Fenette'),('Lelouch Vi Britannia'),
('Satoru Fujinuma'),   ('Kayo Hinazuki'),      ('Sachiko Fujinuma'), ('Gaku Yashiro'),    ('Hiromi Sugita'),  ('Kenya Kobayashi'),     
('Sakura Kinomoto'),   ('Li Shaoran'),         ('Tomoyo Daidouji'),  ('Touya Kinomoto'),  ('Kero'),           ('Yukito Tsukishiro'),    
('Kanade Yuzuriha'),   ('Nino Arisugawa'),     ('Momo Sakaki'),      ('Miou Suguri'),     ('Tsukika Kuze'),   ('Yoshito Haruno'),      
('Fuuka Akitsuki'),    ('Yuu Haruna'),         ('Koyuki Hinashi'),   ('Sara Iwami'),      ('Kazuya Nachi'),   ('Yamato Akitsuki'),     
('Ritsuko Mukae'),     ('Sentaro Kawabuchi'),  ('Yurika Fukahori'),  ('Tsutomu Mukae'),   ('Kaoru Nishimi'),  ('Sentaro Kawabuchi') 

returning id;
"""
cur.execute(sql)

sql ="""
insert into animes_personajes (anime_id,personaje_id) values 
('1','1'),    ('1','2'),    ('1','3'),    ('1','4'),    ('1','5'),    ('1','6'), 
('2','7'),    ('2','8'),    ('2','9'),    ('2','10'),   ('2','11'),   ('2','12'), 
('3','13'),   ('3','14'),   ('3','15'),   ('3','16'),   ('3','17'),   ('3','18'), 
('4','19'),   ('4','20'),   ('4','21'),   ('4','22'),   ('4','23'),   ('4','24'), 
('5','25'),   ('5','26'),   ('5','27'),   ('5','28'),   ('5','29'),   ('5','30'), 
('6','31'),   ('6','32'),   ('6','33'),   ('6','34'),   ('6','35'),   ('6','36'),  
('7','37'),   ('7','38'),   ('7','39'),   ('7','40'),   ('7','41'),   ('7','42'),  
('8','43'),   ('8','44'),   ('8','45'),   ('8','46'),   ('8','47'),   ('8','48'),  
('9','49'),   ('9','50'),   ('9','51'),   ('9','52'),   ('9','53'),   ('9','54'),  
('10','55'),  ('10','56'),                                                         
('11','57'),  ('11','58'),  ('11','59'),  ('11','60'),  ('11','61'),  ('11','62'), 
('12','63'),  ('12','64'),  ('12','65'),  ('12','66'),  ('12','67'),  ('12','68'),  
('13','69'),  ('13','70'),  ('13','71'),  ('13','72'),  ('13','73'),  ('13','74'), 
('14','69'),  ('14','70'),  ('14','71'),  ('14','72'),  ('14','73'),  ('14','74'), 
('15','69'),  ('15','70'),  ('15','71'),  ('15','72'),  ('15','73'),  ('15','74'), 
('16','75'),  ('16','76'),  ('16','77'),  ('16','78'),  ('16','79'),  ('16','80'), 
('17','81'),  ('17','82'),  ('17','83'),  ('17','84'),  ('17','85'),  ('17','86'), 
('18','81'),  ('18','82'),  ('18','83'),  ('18','84'),  ('18','85'),  ('18','86'), 
('19','87'),  ('19','88'),  ('19','89'),  ('19','90'),  ('19','91'),  ('19','92'),  
('20','93'),  ('20','94'),  ('20','95'),  ('20','96'),  ('20','97'),  ('20','98'), 
('21','93'),  ('21','94'),  ('21','95'),  ('21','96'),  ('21','97'),  ('21','98'),  
('22','99'),  ('22','100'), ('22','101'), ('22','102'), ('22','103'), ('22','104'),
('23','105'), ('23','106'), ('23','107'), ('23','108'), ('23','109'), ('23','110'),
('24','105'), ('24','106'), ('24','107'), ('24','108'), ('24','109'), ('24','110'), 
('25','111'), ('25','112'), ('25','113'), ('25','114'), ('25','115'), ('25','107'),
('26','116'), ('26','117'), ('26','118'), ('26','119'), ('26','120'), ('26','121'),
('27','116'), ('27','117'), ('27','118'), ('27','119'), ('27','120'), ('27','121'),
('28','116'), ('28','117'), ('28','118'), ('28','119'), ('28','120'), ('28','121'),
('29','122'), ('29','123'), ('29','124'), ('29','125'), ('29','126'),              
('30','122'), ('30','123'), ('30','124'), ('30','125'), ('30','126'),              
('31','127'), ('31','128'), ('31','129'), ('31','130'),                            
('32','131'), ('32','132'), ('32','133'), ('32','134'), ('32','135'), ('32','136'),
('33','131'), ('33','132'), ('33','133'), ('33','134'), ('33','135'), ('33','136'),
('34','131'), ('34','132'), ('34','133'), ('34','134'), ('34','135'), ('34','136'),
('35','137'), ('35','138'), ('35','139'), ('35','140'), ('35','141'), ('35','142'), 
('36','143'), ('36','144'), ('36','145'), ('36','146'), ('36','147'), ('36','148'),
('37','143'), ('37','144'), ('37','145'), ('37','146'), ('37','147'), ('37','148'),
('38','143'), ('38','144'), ('38','145'), ('38','146'), ('38','147'), ('38','148'),
('39','149'), ('39','150'), ('39','151'), ('39','152'), ('39','153'), ('39','154'),
('40','155'), ('40','156'), ('40','157'), ('40','158'), ('40','159'), ('40','160'),
('41','161'), ('41','162'), ('41','163'), ('41','164'), ('41','165'), ('41','166')
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
