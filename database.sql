CREATE TABLE students (
	snum INTEGER AUTO_INCREMENT, 
	fname VARCHAR(30), 
	lname VARCHAR(30),
	year VARCHAR(20),
	PRIMARY KEY(snum)
);

INSERT INTO students (fname, lname, year) VALUES ("Alexes", "Presswood", "Senior");

CREATE TABLE classes (
	cnum VARCHAR(10), 
	cname VARCHAR(50),
	instructor VARCHAR(75),
	PRIMARY KEY(cnum)
);

INSERT INTO classes (cnum, cname, instructor) VALUES ("CS1000", "Intro to CS", "Michael Jurzcyk");

CREATE TABLE enrolled_students (
	snum INTEGER, 
	cnum VARCHAR(10), 
	FOREIGN KEY(snum) REFERENCES students(snum), 
	FOREIGN KEY(cnum) REFERENCES classes(cnum),
	PRIMARY KEY(snum, cnum)
);

INSERT INTO enrolled_students (snum, cnum) VALUES (1, "CS1000");