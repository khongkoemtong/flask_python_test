from flask import Flask ,render_template
import pymysql

app = Flask(__name__)


def connect_db ():
    connection  = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="reaksa_piseth_db"

    )

    if not connection:
        print("can not connect to database ! 🥺🥺")
    else:
        print("database connected ! ⭐⭐🥳")    


connect_db()


@app.route('/')
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)