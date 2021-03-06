from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc,desc,func
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kowsalya:Kowsi@localhost:5432/test1'
app.debug = True
db = SQLAlchemy(app)


class emplDet(db.Model):
    __tablename__ = 'employee'
    emp_id = db.Column('emp_id', db.Integer, primary_key=True)
    emp_name = db.Column(db.String(100))
    place = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    age = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    d_join=db.Column(db.Date)
    def __init__(self,emp_id, emp_name,place, addr, pin,age,salary,d_join):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.place = place
        self.addr = addr
        self.pin = pin
        self.age=age
        self.salary=salary
        self.d_join=d_join


@app.route('/grp',methods=['GET'])
def grp_sal():
    det=db.session.query(emplDet.salary,func.count(emplDet.emp_id)).group_by(emplDet.salary).all()
    return(dict(det))
#db.create_all()
#db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
