import csv
import random
import locale
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

locale.setlocale(locale.LC_ALL, '')

db = create_engine('postgres://foodportal:analbuttsecks@localhost/foodportal', encoding='latin1', echo=False)
Session = sessionmaker(bind=db)
Base = declarative_base()
session = Session()

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
		return "<Item ('%s', '%i', '%s', '%s', '%i', '%s')>" % (self.name, self.uid, self.cost, self.section, self.is_current, self.event)


items = session.query(Item).from_statement("SELECT * FROM items").all()
highestuid = 0
for item in items:
	if item.uid > highestuid:
		highestuid = int(item.uid)

with open('temp.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	rows = []
	for row in reader:
		rows.append(row)
	firstRow = True
	for row in rows:
		if firstRow:
			firstRow = False
		else:
			matchingItem = None
			for item in items:
				if item.name == row[0]:
					matchingItem = item
			if matchingItem == None or matchingItem.cost != locale.currency(float(row[1]), grouping=True) or matchingItem.section != row[2] or matchingItem.event != row[3]:
				if matchingItem != None:
					matchingItem.is_current = False
				highestuid += 1
				session.add(Item(row[0], highestuid, float(row[1]), row[2], row[3]))

	for item in items:
		matchingItem = False
		for row in rows:
			if item.name == row[0]:
				matchingItem = True
		if not matchingItem:
			item.is_current = False

session.commit()
