CREATE TABLE ips(
	id INT NOT NULL AUTO_INCREMENT,
	type varchar(50) , 

   ip varchar(30),
   port int,
   country varchar(20),
   speed FLOAT, 
   last_check timestamp ,
   extra varchar(200),
   PRIMARY KEY( id )
);


CREATE TABLE Users (
user_id INT NOT NULL AUTO_INCREMENT,
email VARCHAR(80) NOT NULL,
display_name VARCHAR(50) NOT NULL,
password CHAR(41) NOT NULL,
PRIMARY KEY (user_id),
UNIQUE INDEX (email)
) ENGINE=INNODB;
