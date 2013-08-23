from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('postgres://foodportal:analbuttsecks@localhost/foodportal', encoding='latin1', echo=True)
Session = sessionmaker(bind=db)
Base = declarative_base()

class Item(Base):
	__tablename__ = 'items'

	name = Column(String)
	uid = Column(Integer, primary_key=True)
	cost = Column(Float)
	section = Column(String)
	is_current = Column(Boolean)
	event = Column(String)

	def __init__ (self, name, uid, cost, section, event):
		self.name = name
		self.uid = uid
		self.cost = cost
		self.section = section
		self.is_current = True
		self.event = event

	def __repr__(self):
		return "<Item ('%s', '%i', '%f', '%s', '%i', '%s')>"

chicken = Item('chicken', 001, 1.0, 'entree', 'chinese')

session = Session()

session.add(chicken)

session.commit()
