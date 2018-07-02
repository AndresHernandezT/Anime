from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()
sql ="""
insert into animes (id,nombre,cant_capitulos,tipo,autor_id,estudio_id) values 
('Death Note','38','Anime','1','1'),('Watashi ga Motete Dousunda','12','Anime',' ',' '), 
('Orange','13','Anime',' ',' '), ('Ore Monogatari!!','24','Anime',' ',' '), 
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
('Sakamichi no Apollon','12','Anime',' ',' ') 
returning id;
"""
cur.execute(sql)

sql ="""
insert into estados (anime_id,tipo_de_estado,fecha_emision,fecha_termino) values 
('1','Finalizado','03/10/2006','26/06/2007') 
returning id;

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
('14','12'), ('14','13'), ('14','33'), ('14','8')
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
('37','21'), ('37','12'), ('37','14'), ('37',35''), ('37','8'),  ('37','38'), 
('38','14'), ('38','35'), ('38','38'), 
('39','36'), ('39','8'),  ('39','38'), 
('40','13'), ('40','23'), ('40','33'), ('40','36'), ('40','8'),  ('40','9'),   
('41','13'), ('41','33'), ('41','15'), ('41','36'), ('41','8'), 
returning id;
"""
cur.execute(sql)

sql ="""
insert into personajes (id,nombre) values  
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
('Ritsuko Mukae'),     ('Sentaro Kawabuchi'),  ('Yurika Fukahori'),  ('Tsutomu Mukae'),   ('Kaoru Nishimi'),  ('Sentaro Kawabuchi'),   

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
('41','161'), ('41','162'), ('41','163'), ('41','164'), ('41','165'), ('41','166'),

returning id;
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
