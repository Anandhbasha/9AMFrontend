from flask import render_template,request,redirect,url_for,Blueprint
from Controller.StuController import getAllStudent,getStudentById,addStudent,updateStudent,deleteStudent

studentBp = Blueprint("studentBp",__name__)

@studentBp.route('/')
def viewAll():
    students = getAllStudent()
    return render_template("index.html",students=students)

@studentBp.route('/addStudent',methods=["POST","GET"])
def add():
    if request.method=="POST":
        data = {
            "name" : request.form["name"],
            "age" : request.form["age"],
            "mobile":request.form["mobile"],
            "course" : request.form["course"]
        }
        addStudent(data)
        return redirect(url_for("studentBp.viewAll"))
    return render_template("add.html")

@studentBp.route("/updateStudent/<id>",methods=["POST","GET"])
def update(id):
    stu = getStudentById(id)
    if request.method=="POST":
        updated={
            "name":request.form["name"],
            "age": request.form["age"],
            "mobile":request.form["mobile"],
            "course":request.form["course"]
        }
        updateStudent(id,updated)
        return redirect(url_for("studentBp.viewAll"))
    return render_template("edit.html",stu=stu)

@studentBp.route("/deleteStudent/<id>")
def delete(id):
    deleteStudent(id)
    return redirect(url_for("studentBp.viewAll"))