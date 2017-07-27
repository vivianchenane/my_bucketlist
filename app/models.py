class BucketListItem:

    def __init__(self,id,name,description,category,user,date):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.user = user
        self.date = date


class Category:
    def __init__(self, id, name, description,user):
        self.id = id
        self.name = name
        self.description = description
        self.user = user


 

