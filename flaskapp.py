from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/view/addStudent')
def view_add_student():
   return render_template('addStudent.html')


@app.route('/view/addClass')
def view_add_class():
   return render_template('addClass.html')


@app.route('/view/enroll')
def view_enroll():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("SELECT * FROM students")
   students = cur.fetchall();

   cur = con.cursor()
   cur.execute("SELECT * FROM classes")
   classes = cur.fetchall();

   return render_template('enroll.html', students = students, classes=classes)


@app.route('/enrollment')
def enrolled():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("SELECT * FROM students NATURAL JOIN enrolled_students NATURAL JOIN classes")

   rows = cur.fetchall();
   return render_template('viewEnrolled.html', rows=rows)


@app.route('/submit/addStudent', methods = ['POST', 'GET'])
def submit_add_student():
   if request.method == 'POST':
      try:
         fname = request.form['fname']
         lname = request.form['lname']
         year = request.form['year']

         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (fname, lname, year) VALUES (?,?,?)",(fname, lname, year) )
            con.commit()
            msg = "Record successfully added"

   except:
      con.rollback()
      msg = "error in insert student"

   finally:
      return render_template("home.html", msg = msg)
      con.close()


@app.route('/submit/addClass', methods = ['POST', 'GET'])
def submit_add_class():
   if request.method == 'POST':
      try:
         cnum = request.form['cnum']
         cname = request.form['cname']
         instructor = request.form['instructor']

         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO classes (cnum, cname, instructor) VALUES (?,?,?)",(cnum, cname, instructor) )
            con.commit()
            msg = "Record successfully added"

   except:
      con.rollback()
      msg = "error in insert class"

   finally:
      return render_template("home.html", msg = msg)
      con.close()


@app.route('/submit/enroll', methods = ['POST', 'GET'])
def submit_enroll():
   if request.method == 'POST':
      try:
         snum = request.form['student']
         cnum = request.form['class']

         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO enrolled_students (snum, cnum) VALUES (?,?)",(snum, cnum) )
            con.commit()
            msg = "Record successfully added"

   except:
      con.rollback()
      msg = "error in enroll student"

   finally:
      return render_template("viewEnrolled.html", msg = msg)
      con.close()


if __name__ == '__main__':
   app.run(debug = True)