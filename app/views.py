from flask import render_template, flash, redirect, session, request, url_for
from app import app
from .models import BucketListItem, Category
from .forms import LoginForm, RegisterForm



database_users = {}

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


@app.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm()
    if request.method== 'GET': 
        return render_template('register.html', form=form, title='Register') 
    if request.method=='POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        database_users[username] = dict(email=email, password=password)
        session['username'] = username
        return redirect('/dashboard')
        

@app.route('/login', methods=['GET' ,'POST'])
def login():
    form=LoginForm()
    if request.method== 'GET': 
        return render_template('index.html', form=form, title='Login') 

    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')

    #if not username or password:
      #flash('please enter username or password')
      #return index()
        try:
            if database_users[username] and database_users[username]['password'] == password:
                session['username'] = username
                flash(u'login success')
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('login'))
        
        except (KeyError, ValueError):
            flash(u'login failed')
            return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard',bucket_list_itemss=bucket_list_items)

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

@app.route('/delete')
def delete():
    id = request.args.get('id')
    print(id)
    if id == None:
     return redirect('/dashboard')

    index_to_delete = int(id) - 1
    print(index_to_delete)
    del bucket_list_items[index_to_delete]
    return redirect('/dashboard')

@app.route('/edititem')
def edit_item():
    id = request.args.get('id')
    print(id)
    if id == None:
     return redirect('/dashboard')
    index_to_edit = int(id) - 1
    print(index_to_edit)
    item_to_edit=bucket_list_items[index_to_edit]
    return render_template('edit_item.html',vee=item_to_edit)

@app.route('/update_item', methods=['POST'])
def update_item():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        description = request.form.get('description')
        category = request.form.get('category')
        user = session['username']
        date = request.form.get('date')

        for item_to_update in bucket_list_items:
            print('Item To Update##')
            print(bucket_list_items)
            print(item_to_update['id'])
            print('Done printing')
            if item_to_update['id'] == id:
                item_to_update['name'] = name
                item_to_update['description'] = description
                item_to_update['date'] = date
                item_to_update['category'] = category
                break

    return redirect('/dashboard')

