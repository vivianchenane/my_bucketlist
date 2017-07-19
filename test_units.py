class BucketlistItem(object):
    pass

class Category(object):
    pass


bucket_items = []

def createItem(name,id,createdBy, category):
 	item = BucketlistItem()
 	item.name=name
 	item.id=id
 	item.createdBy=createdBy
 	item.category=category

 	bucket_items.append(item)
 	return item

def test_vee():
	assert createItem('curtis',1, 'vivian','entertainment').name == 'curtis'


def test_createItem1():
	assert createItem('curtis',1, 'vivian','entertainment').name == 'cu'

def test_createItem2():
	assert createItem('curtis',1, 'vivian','entertainment').id == 1


    