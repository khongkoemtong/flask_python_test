from flask import Flask,render_template
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


if __name__=="__main__":
    app.run(debug=True)