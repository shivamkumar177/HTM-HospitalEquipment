from flask import Flask,render_template,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import urllib.request
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///equipmen.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.secret_key = "secret key"


class Equip(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(1000))
    
    # def __repr__(self) -> str:
    #     return f"{self.name} - {self.desc}"

    

@app.before_first_request
def create_tables():
    db.create_all()

# UPLOAD_FOLDER = os.path.join('static', 'uploads')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method =='POST':
        # file = request.files['file']
        # if file.filename == '':
        #     flash('Please upload picture')
        #     return redirect(request.url)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        # filenames = os.path.join(app.config['UPLOAD_FOLDER'], file.filename) 
        # img=Img()
        # db.session.add(img)
        # db.session.commit()
        name=request.form['name']
        desc=request.form['desc']
        # data=file.read()
        # render_file=render_picture(data)
        equip = Equip(name=name,desc=desc)
        db.session.add(equip)
        db.session.commit()
    allequip = Equip.query.all()
    # filename1 = Img.query.all()
    return render_template('index.html', allequip=allequip)

@app.route('/delete/<int:sno>')
def delete(sno):
    equip = Equip.query.filter_by(sno=sno).first()
    db.session.delete(equip)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)