class BucketListItem:

    def __init__(self,id,name,description,category,created_by,date):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.createdBy = created_by
        self.date = date


class Category:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


