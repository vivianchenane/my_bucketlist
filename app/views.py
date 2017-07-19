from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Sign In')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/login', methods=['POST'])
def login():
    return render_template('dashboard.html', title='Dashboard')


@app.route('/logout')
def logout():
    return redirect('/index')

@app.route('/add_item')
def addItem():
   return render_template('add_item.html', title='Add Item'



