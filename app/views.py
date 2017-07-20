from flask import render_template, flash, redirect, session, request
from app import app


database_users = {'username': 'user' ,'password': 'user'}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Sign In')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(request.form.get('username'))
    print(request.form.get('password'))

    #if not username or password:
      #flash('please enter username or password')
      #return index()

    if database_users['username'] == username and database_users['password'] == password:
        session['username'] = username
        return redirect('/dashboard' ,message = 'Login successful!!')

    flash('please enter valid login credentials##')
    return index()

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

@app.route('/logout') 
def logout():
    return redirect('/index')

@app.route('/additem' ,methods = ['GET' , 'POST'])
def addItem():
   return render_template('add_item.html', title='Add Item')


@app.route('/addcategory')
def addcategory():
	return render_template('add_category.html', title='Category')


@app.route('/save_category', methods=['POST'])
def saveCategory():
    return redirect('/categorylist')


@app.route('/categorylist')
def categorylist():
    return render_template('category_list.html', title='Category List')


