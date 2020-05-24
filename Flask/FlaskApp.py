from flask import Flask, render_template



app = Flask(__name__)
EmployeeDict={0:{'name':'Manasa','Salary':2000000,'Age':31},
    1:{'name':'Manasa','Salary':2000000,'Age':31},
    2:{'name':'Manasa','Salary':2000000,'Age':31},
    3:{'name':'Manasa','Salary':2000000,'Age':31},
    4:{'name':'Manasa','Salary':2000000,'Age':31}
}

@app.route('/')
def homePage():
    return (f'Hi Hello ! You are in HomePage!')


@app.route('/empDet/<int:emp_id>')
def getEmployeeDetails(emp_id):
    empDet=EmployeeDict.get(emp_id)
    return (render_template('employeeDetails.html',empDet=empDet))
    
if __name__=='__main__':
    app.run(debug=True)