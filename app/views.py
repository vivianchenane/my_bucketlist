from flask import render_template, flash, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Sign In')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('dashboard.html', title='Dashboard')

@app.route('/logout')
def logout():
    return redirect('/index')

@app.route('/additem')
def addItem():
   return render_template('add_item.html', title='Add Item')


@app.route('/addcategory')
def addcategory():
	return render_template('add_category.html', title='Category')

@app.route('/categorylist')
def categorylist():
    return render_template('category_list.html', title='Category List')


