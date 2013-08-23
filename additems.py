from sqlalchemy import *

class Item(object):
	pass

db = create_engine('postgres://foodportal:analbuttsecks@localhost/foodportal')
db.echo = False
metadata = BoundMetaData(db)
items = Table('items', metadata, autoload=True)

itemmapper = mapper(Item, items)

session = create_session()


