from flask import Flask, render_template, redirect, request

app = Flask(__name__)

ALL_DATA = [
    {
        'f_name': 'Mubashir',
        'l_name': 'Haider',
        'class': 'BSCS', 'dofbirth':
        '28/10/2003',
        'roll': '1',
        'fee': '25000'
    },
    {
        'f_name': 'Ali Raza',
        'l_name': 'Yameen',
        'class': 'BBA',
        'dofbirth':
        '5/10/2000',
        'roll': '2',
        'fee': '35000'
    },
    {
        'f_name': 'Usman',
        'l_name': 'Malik',
        'class': 'BSCS',
        'dofbirth': '26/10/2002',
        'roll': '3',
        'fee': '12000'
    }
]
TEACHER_DATA = [
    {
        'f_name': 'Shahzaib',
        'l_name': 'Akash',
        'class': 'BSCS',
        'dofbirth': '2000-01-31',
        'id': '1',
        'salary': '6000'
    },
    {
        'f_name': 'Manzoor',
        'l_name': 'Ahmed',
        'class': '10th',
        'dofbirth': '1984-11-29',
        'id': '2',
        'salary': '4000'
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/student.list")
def student_list():
    return render_template("students/student_list.html", students=ALL_DATA)


@app.route("/student/<roll_number>")
def student_detail(roll_number):
    for student in ALL_DATA:
        if student['roll'] == roll_number:
            return render_template("students/student_detail.html", student=student)
    return render_template("students/404.html")


@app.route("/student/<roll_number>/delete")
def delete_student(roll_number):
    for student in ALL_DATA:
        if student['roll'] == roll_number:
            ALL_DATA.remove(student)
            return redirect("/student.list")
    return render_template("students/404.html")

@app.route("/student/add", methods=["GET", "POST"])
def add_student():
    if request.method == "GET":
        return render_template("students/add_student.html")
    elif request.method == "POST":
        first_name =  request.form["first_name"]
        last_name = request.form["last_name"]
        class_ = request.form["class"]
        dob_ = request.form["date_of_birth"]
        roll_ = request.form["roll_number"]
        fees_ = request.form["fee"]
        student = {
            'f_name': first_name,
            'l_name': last_name,
            'class': class_,
            'dofbirth': dob_,
            'roll': roll_,
            'fee': fees_
            }
        ALL_DATA.append(student)
        return redirect("/student.list")


@app.route("/student/<roll_number>/edit", methods=['GET', 'POST'])
def edit_student(roll_number):
    # Handle 404/ Check if students exists
    current_student = None
    for student in ALL_DATA:
        if student['roll'] == roll_number:
            current_student = student
    if current_student == None:
        return render_template("students/404.html")
    
    # Send the form on get request
    if request.method == "GET":
        return render_template("students/edit_student.html", student=current_student)
    elif request.method == 'POST':
        index = ALL_DATA.index(current_student)
        ALL_DATA[index] = {
            "roll": roll_number,
            "f_name": request.form["first_name"],
            "l_name": request.form["last_name"],
            "class": request.form["class"],
            "dofbirth": request.form["date_of_birth"],
            "fee": request.form["fee"],
        }
        return redirect("/student.list")

# Teachers

@app.route("/teacher.list")
def teacherlist():
    return render_template("/teachers/teacher_list.html", teachers= TEACHER_DATA)


@app.route("/teacher/<id>")
def teacherid(id):
    for teacher in TEACHER_DATA:
        if teacher["id"] == id:
            return render_template("teachers/teacher_detail.html", teacher= teacher)
    return render_template("teachers/404_.html")

@app.route("/<id>/view_")
def view_teacher(id):
    for teacher in TEACHER_DATA:
        if teacher["id"] == id:
            return render_template("teachers/teacher_detail.html", teacher= teacher)
    return render_template("teachers/404_.html")


@app.route("/<id>/delete")
def delete_teacher(id):
    for teacher in TEACHER_DATA:
        if teacher["id"] == id:
            TEACHER_DATA.remove(teacher)
            return redirect("/teacher.list")
    return render_template("teachers/404_.html")


@app.route("/teacher/add", methods=  ['GET', 'POST'])
def add_teacher():
    if request.method == "GET":
        return render_template("teachers/add_teacher.html")
    elif request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        date_of_birth = request.form["date_of_birth"]
        class_ = request.form["class_"]
        id_number = request.form["id_number"]
        salary_ = request.form["salary_"]
        teacher = {    
        'f_name': first_name,
        'l_name': last_name,
        'class': class_,
        'dofbirth': date_of_birth,
        'id': id_number,
        'salary': salary_
        }
        TEACHER_DATA.append(teacher)
        return redirect("/teacher.list")

@app.route("/<id>/edit", methods= ["GET", "POST"])
def edit_teacher(id):
    current_teacher = None
    for teacher in TEACHER_DATA:
        if teacher['id'] == id:
            current_teacher = teacher
    if current_teacher == None:
        return render_template("teachers/404_.html")
    if request.method == "GET":
        return render_template("teachers/edit_teacher.html", teacher= current_teacher)
    elif request.method == "POST":
        index = TEACHER_DATA.index(current_teacher)
        TEACHER_DATA[index] = {
            "id": id,
            "f_name": request.form["first_name"],
            "l_name": request.form["last_name"],
            "dofbirth": request.form["date_of_birth"],
            "class": request.form["class_"],
            "salary": request.form["salary_"]
        }
        return redirect("/teacher.list")
    