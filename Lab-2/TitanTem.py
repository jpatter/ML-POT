import urllib3, requests, json, os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, FloatField, IntegerField
from wtforms.validators import Required, Length, NumberRange
url = 'Enter url'
username = 'enter username'
password = 'enter password'
scoring_endpoint = 'enter scoring endpoint' 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretpassw0rd'
bootstrap = Bootstrap(app)
class TitanicForm(FlaskForm):
  pclass = RadioField('Passenger Class:', coerce=int, choices=[('1','First'),('2','Second'),('3','Third')])
  name = StringField('Name:')
  sex = RadioField('Gender:', coerce=str, choices=[('male','Male'),('female','Female')])
  age = RadioField('Age:', coerce=int, choices=[('0','0-5'),('1','6-11'),('2','12-17'),('3','18-39'),('4','40-64'),('5','65-79'),('6','>80')])
  ticket = StringField('Ticket:')
  fare = FloatField('Fare:')
  sibsp = IntegerField('Number of siblings/spouses:')
  parch = IntegerField('Number of parents/children:')
  embarked = RadioField('Embark Location:', coerce=str, choices=[('S','US'),('C','Canada')])
  submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():
  form = TitanicForm()
  if form.is_submitted(): 
    sex = form.sex.data
    print (sex)
    form.sex.data = ''
    age = form.age.data
    print (age)
    form.age.data = ''
    name = form.name.data
    form.name.data = ''
    pclass = form.pclass.data
    form.pclass.data = ''
    ticket = form.ticket.data
    form.ticket.data = ''
    fare = form.fare.data
    form.fare.data = '' 
    sibsp = form.sibsp.data
    form.sibsp.data = ''
    parch = form.parch.data
    form.parch.data = ''   
    embarked = form.embarked.data
    form.embarked.data = ''    
    
    headers = urllib3.util.make_headers(basic_auth='{}:{}'.format(username, password))
    path = '{}/v3/identity/token'.format(url)
    response = requests.get(path, headers=headers)
    mltoken = json.loads(response.text).get('token')
    scoring_header = {'Content-Type': 'application/json', 'Authorization': 'Bearer' + mltoken}
    payload = {"fields": ["pclass","name","sex","sibsp","parch","ticket","fare","embarked","Age_Bucket"], "values": [[pclass,name,sex,sibsp,parch,ticket,fare,embarked,age]]}
    scoring = requests.post(scoring_endpoint, json=payload, headers=scoring_header)
    return render_template('score.html', form=form, scoring=scoring)
  return render_template('index.html', form=form)
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(port))
