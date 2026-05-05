from flask import Flask,render_template,request,redirect,url_for
import pymysql
app = Flask(__name__)

def connect_db ():
    conection = pymysql.connect(
        host="localhost",
        user='root',
        passwd="",
        database="reaksa_piseth_db",
    )
    return  conection



@app.route("/")
def hello():
    conection = connect_db()
    cursor = conection.cursor()


    cursor.execute("SELECT * FROM students ")
    students = cursor.fetchall()
    conection.commit()

    return  render_template("index.html",data = students)


@app.route('/insert' ,methods=['POST'])
def insert ():
    conection = connect_db()
    cursor = conection.cursor()

    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    grade = request.form['grade']

    sql = "INSERT INTO students (name,age,gender,grade) values (%s,%s,%s,%s)"

    cursor.execute(sql,(name,age,gender,grade))
    conection.commit()
    
    return redirect(url_for('hello'))


@app.route('/update',methods=['POST'])
def update ():
    conection = connect_db()
    cursor = conection.cursor()

    id = request.form['update_id']
    name = request.form['update_name']
    age = request.form['update_age']
    gender = request.form['update_gender']
    grade = request.form['update_grade']

    sql = "UPDATE students SET name = %s , age = %s ,gender = %s ,grade =%s WHERE id= %s"

    cursor.execute(sql,(name,age,gender,grade,id))

    conection.commit()

    return redirect(url_for("hello"))


@app.route('/delete' ,methods=['POST'])
def delete ():
    conection = connect_db()
    cursor = conection.cursor()

    id = request.form['delete_id']

    sql = "DELETE FROM students WHERE id = %s"

    cursor.execute(sql,(id))

    conection.commit()

    return redirect(url_for('hello'))





if __name__=="__main__":
    app.run(debug=True)