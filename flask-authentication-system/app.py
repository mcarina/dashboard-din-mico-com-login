from flask import request,render_template, redirect,session
from models import app, User, db
from dashboard import dashboard_plot

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        coordenadoria = request.form['coordenadoria']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,coordenadoria=coordenadoria,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')

    return render_template('register.html')

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        graph_html = dashboard_plot(user.coordenadoria)
        return render_template('dashboard.html',user=user, graph_html=graph_html)
    
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')