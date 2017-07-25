from app import app


class BucketlistItem(object):
    pass

class Category(object):
    pass


bucket_items = []

def test_successful_user_registration(self):
    email ="vivianchenane@gmail.com"
    password ="vee"
    user = {"email": email,"password":password}
    # assertEqual(app.test_client().post('/register'), data=json.dump(user),"login succesful")

def test_index_page():
    print("testing if index page is loading")
    test_page_load = app.test_client()
    response = test_page_load.get('/indexx')
    assert response.status_code == 404

def test_index_page_fail():
    print("testing if index page is loading")
    test_page_load = app.test_client()
    response = test_page_load.get('/index')
    assert response.status_code == 404

def test_login_correct_login_details():
    print("testing if index page is loading")
    test_login = app.test_client()
    response = test_login.post('/login',data = dict(username='user',password='user'),follow_redirects=True)
    # print(response)
    assert b'login success' in response.data


def createItem(name,id,createdBy, category):
 	item = BucketlistItem()
 	item.name = name
 	item.id = id
 	item.createdBy = createdBy
 	item.category = category

 	bucket_items.append(item)
 	return item


def test_createItem():
	assert createItem('music', 1, 'vivian','entertainment').name == 'music'

def test_checkItemListSize():
	assert len(bucket_items) == 1

def test_createItem1():
	assert createItem('Dubai', 2, 'vivian','travel').name == 'Dubai'

def test_checkItemListSize():
	assert len(bucket_items) == 2

def test_createItem2():
	assert createItem('novel', 3, 'vivian','books').id == 3

def test_checkItemListSize():
	assert len(bucket_items) == 3


def test_deleteItem():
   del bucket_items[0]
   assert len(bucket_items) == 2

def test_deleteItem2():
    del bucket_items[1]
    assert len(bucket_items) == 1
def test_editItem():
	bucket_items[0].name = 'videos'
	assert bucket_items[0].name =='videos'






category = []

def createCategory(name,id,createdBy):
    categories = Category()
    categories.name = name
    categories.id = id
    categories.createdBy = createdBy

    category.append(categories)
    return categories

def test_createCategory():
    assert createCategory('movies', 1, 'vivian').id == 1

def test_createCategory1():
    assert createCategory('books', 2, 'vivian').name == 'books'

def test_createCategory3():
    assert createCategory('Entertainment', 3, 'vivian').createdBy == 'vivian'










    