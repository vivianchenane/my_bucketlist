from flask import render_template, flash, redirect, session, request, url_for
from app import app
# from .models import BucketListItem, Category
from .forms import LoginForm, RegisterForm
import json



database_users = {'username': 'user', 'password': 'user'}

bucket_list_items = []

    # {
    #     'id': '1',
    #     'name': 'Travel to coast via SGR',
    #     'description': 'Going to Mombasa',
    #     'category': 'Travel',
    #     'user': 'vivian',
    #     'date': '30/07/2017'
    # }

    # {
    #     'id': '1',
    #     'name': 'Travel',
    #     'description': 'My dream destinations',
    #     'user': 'vivian'
    # }

category_items = []



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
    return redirect('/bucketlist')

@app.route('/logout') 
def logout():
    return redirect('/index')


@app.route('/add_item',methods= ['GET','POST'])
def add_item():
    
    id = request.args.get('id')
    uname = session['username']
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        category = request.form.get('category')
        user = session['username']
        date = request.form.get('date')
        id = len(bucket_list_items) + 1

        # bucket_item = BucketListItem(id,name,description,category,user,date)
        bucket_item = {"id":  id, "name": name,"description": description,"category":category, "user": user,"date": date}
        bucket_list_items.append(bucket_item)

        bucket_index_to_view = int(category) - 1
        print(bucket_index_to_view)
        bucket_to_view = category_items[bucket_index_to_view]
        items_to_view = []
        for item in bucket_list_items:
            if item['user'] == str(uname) and item['category'] == category:
                items_to_view.append(item)
            else:
                print('Item NoT for Current logged in User or Bucket##')
        
        return render_template('item_list.html', title='Item List',bucket_list_itemss=items_to_view,bucket=bucket_to_view)

    return render_template('add_item.html', title='Add Item', category=id)


@app.route('/addbucket')
def addcategory():
	return render_template('add_category.html', title='Add bucket')


@app.route('/save_bucket', methods=['POST'])
def saveCategory():
    name = request.form.get('name')
    description = request.form.get('description')
    user = session['username']
    id = len(category_items) + 1
    # category = Category(id,name,description,user)

    category = {"id":  id, "name": name,"description": description, "user": user}
    
    category_items.append(category)
    print('****New Object Added***')
    print(len(category_items))
    print(category_items)
    return redirect('/bucketlist')

    # return redirect('/addbucket')


@app.route('/bucketlist')
def categorylist():
    uname = session['username']
    print(uname)
    user_bucket = []
    print(len(category_items))
    for bucket in category_items:
        print('****Object Details***')
        print(len(category_items))
        print(str(bucket))
        print(str(bucket['user']))
        print(str(bucket['id']))
        print(str(uname))
        print('****End Object Details***')
        # buk = str(bucket)
        print('****Object Details After Convert***')
        
        if bucket['user'] == str(uname):
            user_bucket.append(bucket)
        else:
            print('Item NoT for Current logged in User##')
        

    return render_template('bucket_list.html', title='Bucket List',category_items=user_bucket)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    category = request.args.get('category')
    print(id)
    if id == None:
     return redirect('/dashboard')

    index_to_delete = int(id) - 1
    print(index_to_delete)
    del bucket_list_items[index_to_delete]

    bucket_index_to_view = int(category) - 1
    print(bucket_index_to_view)
    bucket_to_view = category_items[bucket_index_to_view]

    return render_template('item_list.html', title='Item List',bucket_list_itemss=bucket_list_items,bucket=bucket_to_view)



@app.route('/delete1')
def delete1():
    id = request.args.get('id')
    print(id)
    if id == None:
     return redirect('/dashboard')

    index_to_delete = int(id) - 1
    print(index_to_delete)
    del category_items[index_to_delete]
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
    uname = session['username']
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
            if item_to_update['id'] == int(id):
                item_to_update['name'] = name
                item_to_update['description'] = description
                item_to_update['date'] = date
                item_to_update['category'] = category
                break
        
        # bucket_item = {"id":  id, "name": name,"description": description,"category":category, "user": user,"date": date}
        # display items now for the user
        print('Item Details!')
        print(len(bucket_list_items))
        print(bucket_list_items)
        bucket_index_to_view = int(category) - 1
        print(bucket_index_to_view)
        bucket_to_view = category_items[bucket_index_to_view]
        items_to_view = []
        for item in bucket_list_items:
            if item['user'] == str(uname) and item['category'] == category:
                items_to_view.append(item)
            else:
                print('Item NoT for Current logged in User or Bucket##')
        print(items_to_view)
        print(len(items_to_view))
        print('end ')
        return render_template('item_list.html', title='Item List',bucket_list_itemss=items_to_view,bucket=bucket_to_view)      


@app.route('/viewitems')
def view_items():
    id = request.args.get('id')
    uname = session['username']
    print(id)
    if id == None:
     return redirect('/dashboard')

    bucket_index_to_view = int(id) - 1
    print('****List Details***')
    print(len(bucket_list_items))
    print(bucket_index_to_view)

    bucket_to_view = category_items[bucket_index_to_view]
    items_to_view = []
    for item in bucket_list_items:
        print('****Object Details***')
        print(len(bucket_list_items))
        print(str(item))
        print(str(item['user']))
        print(str(item['id']))
        print(str(uname))
        print('****End Object Details***')

        if item['user'] == str(uname) and item['category'] == id:
            items_to_view.append(item)
        else:
            print('Item NoT for Current logged in User or Bucket##')
        
    return render_template('item_list.html', title='Item List',bucket_list_itemss=items_to_view,bucket=bucket_to_view)



