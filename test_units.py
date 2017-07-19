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
	assert createItem('music', 1, 'vivian','entertainment').name == 'music'

def test_checkItemListSize():
	assert len(bucket_items) == 1

def test_createItem1():
	assert createItem('music', 2, 'vivian','travel').name == 'cu'

def test_checkItemListSize():
	assert len(bucket_items) == 2

def test_createItem2():
	assert createItem('music', 3, 'vivian','books').id == 1

def test_checkItemListSize():
	assert len(bucket_items) == 3


def test_deleteItem():
   del bucket_items[0]
   assert len(bucket_items) == 2



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
    assert createCategory('books', 2, 'vivian').name == 'series'

def test_createCategory3():
    assert createCategory('Entertainment', 3, 'vivian').createdBy == 'nelly'










    