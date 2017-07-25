from flask import render_template, flash, redirect, session, request, url_for
from app import app
from .models import BucketListItem, Category


database_users = {'username': 'user' ,'password': 'user'}

bucket_list_items = [
    {
        'id': '1',
        'name': 'Travel to coast via SGR',
        'description': 'Going to Mombasa',
        'category': 'Travel',
        'user': 'vivian',
        'date': '30/07/2017'
    }
]


category_items = [
    {
        'id': '1',
        'name': 'Travel',
        'description': 'My dream destinations',
        'user': 'vivian'
    }
]



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
        flash(u'login success')
        return redirect(url_for('dashboard'))

    flash(u'login failed')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard',bucket_list_items=bucket_list_items)

@app.route('/logout') 
def logout():
    return redirect('/index')


@app.route('/add_item',methods= ['GET','POST'])
def add_item():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        category = request.form.get('category')
        user = session['username']
        date = request.form.get('date')
        id = len(bucket_list_items) + 1

        bucket_item = BucketListItem(id,name,description,category,user,date)
        bucket_list_items.append(bucket_item)
        return redirect('/dashboard')

    return render_template('add_item.html', title='Add Item')


@app.route('/addcategory')
def addcategory():
	return render_template('add_category.html', title='Add Category')


@app.route('/save_category', methods=['POST'])
def saveCategory():
    name = request.form.get('name')
    description = request.form.get('description')
    user = session['username']
    id = len(category_items) + 1
    category = Category(id,name,description,user)
    category_items.append(category)
    return redirect('/categorylist')

    return redirect('/addcategory')


@app.route('/categorylist')
def categorylist():
    return render_template('category_list.html', title='Category List',category_items=category_items)


