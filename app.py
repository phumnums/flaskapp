from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello My First Web Application"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '5000', debug = True)

#---------------------------- HTTP Methods ---------------------------------#

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)

#---------------------------- Flask Templates ---------------------------------#

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

#---------------------------- Flask Static Files ---------------------------------#

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)

