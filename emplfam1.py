from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kowsalya:Kowsi@localhost:5432/test1'
app.debug = True
db = SQLAlchemy(app)


class emplFam(db.Model):
    __tablename__ = 'employeefam'
    emp_id = db.Column('emp_id', db.Integer, primary_key=True)
    f_name = db.Column(db.String(100))
    m_name = db.Column(db.String(50))
    m_status= db.Column(db.String(200))
    ann_inc = db.Column(db.Integer)
    def __init__(self,emp_id,f_name,m_name,m_status,ann_inc):
        self.emp_id = emp_id
        self.f_name = f_name
        self.m_name=m_name
        self.m_status=m_status
        self.ann_inc=ann_inc
@app.route('/emp',methods=['POST'])
def emrec():
    ipt=request.get_json()
    #print(ipt)
    det=emplFam(emp_id=ipt['emp_id'],f_name=ipt['f_name'],m_name=ipt['m_name'],m_status=ipt['m_status'],ann_inc=ipt['ann_inc'])
    db.session.add(det)
    db.session.commit()
    return("successfully created")
#db.create_all()
#db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
