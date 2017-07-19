class BucketlistItem(object):
    pass

class Category(object):
    pass


bucket_items = []

def createItem(name,id,createdBy, category):
 	item = BucketlistItem()
 	item.name = name
 	item.id = id
 	item.createdBy = createdBy
 	item.category = category

 	bucket_items.append(item)
 	return item

def test_createItem():
	assert createItem('curtis', 1, 'vivian','entertainment').name == 'curtis'

def test_createItem1():
	assert createItem('curtis', 1, 'vivian','entertainment').name == 'cu'

def test_createItem2():
	assert createItem('curtis', 1, 'vivian','entertainment').id == 1

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
    assert createCategory1('movies', 1, 'vivian').category == 'series'







    