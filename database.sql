create table students (
	snum INTEGER AUTO_INCREMENT, 
	fname VARCHAR(30), 
	lname VARCHAR(30),
	year VARCHAR(20),
	PRIMARY KEY(snum)
);

create table classes (
	cnum VARCHAR(10), 
	cname VARCHAR(50),
	instructor VARCHAR(75),
	PRIMARY KEY(cnum)
);

create table enrolled_students (
	snum INTEGER, 
	cnum VARCHAR(10), 
	FOREIGN KEY(snum) REFERENCES students(snum), 
	FOREIGN KEY(cnum) REFERENCES classes(cnum),
	PRIMARY KEY(snum, cnum)
);