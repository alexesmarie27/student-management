from flask import Flask, render_template, request, url_for
import MySQLdb
import itertools

app = Flask(__name__)
con = MySQLdb.connect("hackweek.cknowok54my8.us-west-2.rds.amazonaws.com", "ampwd6", "password", "hackweek")

# directs the user to the homepage
@app.route('/')
def home():
   return render_template('home.html')

#directs the user to the addStudent webpage
@app.route('/view/addStudent')
def view_add_student():
   return render_template('addStudent.html')

# directs the user to the addClass webpage
@app.route('/view/addClass')
def view_add_class():
   return render_template('addClass.html')

# queries the database for all students and classes, then redirects the user
# to the enroll webpage
@app.route('/view/enroll')
def view_enroll():
   cur = con.cursor()
   cur.execute("SELECT snum, fname, lname FROM students ORDER BY lname")
   students = cur.fetchall()
   
   cur.execute("SELECT cnum, cname, instructor FROM classes ORDER BY cnum")
   classes = cur.fetchall()

   return render_template('enroll.html', students = students, classes = classes)

# queries the database for all enrollment information, then redirects the user to the viewEnrolled webpage
@app.route('/enrollment')
def enrolled():
   cur = con.cursor()
   cur.execute("SELECT fname, lname, cnum, cname, instructor FROM students NATURAL JOIN enrolled_students NATURAL JOIN classes ORDER BY lname")
   rows = cur.fetchall()
    
   return render_template('viewEnrolled.html', rows = rows)

# adds a user into the database
@app.route('/submit/addStudent', methods = ['POST', 'GET'])
def submit_add_student():
   if request.method == 'POST':
      try:
         fname = request.form['fname']
         lname = request.form['lname']
         year = request.form['year']

         cur = con.cursor()
         cur.execute("INSERT INTO students (fname, lname, year) VALUES (%s, %s, %s)",(fname, lname, year) )
         con.commit()
	 
      except:
         con.rollback()
	 
      finally:
         return home()

# adds a class into the database
@app.route('/submit/addClass', methods = ['POST', 'GET'])
def submit_add_class():
   if request.method == 'POST':
      try:
         cnum = request.form['cnum']
         cname = request.form['cname']
         instructor = request.form['instructor']

         cur = con.cursor()
         cur.execute("INSERT INTO classes (cnum, cname, instructor) VALUES (%s, %s, %s)",(cnum, cname, instructor) )
         con.commit()

      except:
         con.rollback()
     
      finally:
         return home()

# adds an enrollment into the database
@app.route('/submit/enroll', methods = ['POST', 'GET'])
def submit_enroll():
   if request.method == 'POST':
      try:
         snum = request.form['chosen_student']
         cnum = request.form['chosen_class']

         cur = con.cursor()
         cur.execute("INSERT INTO enrolled_students (snum, cnum) VALUES (%s, %s)",(snum, cnum) )
         con.commit()

      except:
         con.rollback()

      finally:
         return enrolled()


if __name__ == '__main__':
   app.run(debug = True)









