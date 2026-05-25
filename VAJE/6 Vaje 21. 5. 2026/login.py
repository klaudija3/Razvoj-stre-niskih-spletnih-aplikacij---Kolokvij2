from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

us_pass = {'martin' : 'martin00', 'student' : 'student00'}

@app.route('/success/<name>', methods = ['GET'])
def success(name):
    return 'Welcome, %s' % name

@app.route('/failure', methods = ['GET'])
def failure():
    return 'Wrong username or password'

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        if us_pass[user] == password:
            return redirect(url_for('success',name = user))
        else:
            return redirect(url_for('failure',name = user))


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=1235, use_reloader=False)
