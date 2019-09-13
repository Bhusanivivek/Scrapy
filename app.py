from flask import  Flask,render_template,request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Fetch the service account key JSON file contents
cred = credentials.Certificate('scp.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://scrap-5282a.firebaseio.com'
})




app=Flask(__name__)

@app.route('/')
def one():
    return render_template('index.html')

@app.route('/blog1')
def bo():

    return  render_template('blog-single.html')

@app.route('/bl',methods=['GET','POST'])
def bg():

    cmt = request.form.get('cmt')
    ref = db.reference('Comments/')
    ref.push(cmt)


    return  render_template('blog-single.html')
@app.route('/blog2')
def bb():

    return render_template('blog2.html')

@app.route('/b2',methods=['GET','POST'])
def bg2():
    cm=request.form.get('comment')

    ref = db.reference('Comments/')
    ref.push(cm)
    return  render_template("blog2.html")
@app.route('/about')
def abt():
    return render_template('about.html')
