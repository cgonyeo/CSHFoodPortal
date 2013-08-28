import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Database initialization
db = create_engine('postgres://foodportal:analbuttsecks@localhost/foodportal', encoding='latin1', echo=False)
Session = sessionmaker(bind=db)
Base = declarative_base()
session = Session()

#represents a row in the events table
class Event(Base):
	__tablename__ = 'events'

	name = Column(String)
	uid = Column(Integer, primary_key=True)
	dueTime = Column(DateTime)
	foodEta = Column(DateTime)
	organizer_username = Column(String)
	description = Column(String)

	def __init__ (self, name, uid, dueTime, foodEta, organizer_username, description):
		self.name = name
		self.uid = uid
		self.dueTime = dueTime
		self.foodEta = foodEta
		self.organizer_username = organizer_username
		self.description = description

	def __repr__(self):
		return "<Event ('%s', '%i', '%s', '%s', '%s', '%s')>" % (self.name, self.uid, str(self.dueTime), str(self.foodEta), str(self.organizer_username), self.description)

#the uids of all events, so we can calculate the new event's uid
event_uids = session.query(Event).from_statement("SELECT uid FROM events").all()
print event_uids

#Get the information from the user
name = raw_input("Name: ")
organizer = raw_input("Organizer's username: ")
dateText = raw_input("Date of event: ")
#we want month/date, or month/day/year
while(len(dateText.split('/')) < 2 or len(dateText.split('/')) > 4):
	dateText = raw_input("Error, try again: ")
dueTimeText = raw_input("Orders due at: ")
#we want an hour, or hour:minute
while(len(dueTimeText.split(':')) > 2):
	dueTimeText = raw_input("Error, try again: ")
foodEtaText = raw_input("Food arrives at: ")
#we want an hour, or hour:minute
while(len(foodEtaText.split(':')) > 2):
	foodEtaText = raw_input("Error, try again: ")
description = raw_input("Description of event: ")

dateTokens = dateText.split('/')
dueTimeTokens = dueTimeText.split(':')
foodEtaTokens = foodEtaText.split(':')

#if they didn't enter a year, assume it's this year
if len(dateTokens) == 2:
	year = datetime.datetime.now().year
else:
	year = int(dateTokens[2])

#if they entered only two digits for a year, assume this century
if year < 100:
	year = year + 2000

#if they entered no minutes, assume 00
if len(dueTimeTokens) == 1:
	minutes = 0
else:
	minutes = int(dueTimeTokens[1])

#Also assuming each time shares the same date
dueTime = datetime.datetime(year, int(dateTokens[0]), int(dateTokens[1]), int(dueTimeTokens[0]), minutes)
foodEta = datetime.datetime(year, int(dateTokens[0]), int(dateTokens[1]), int(foodEtaTokens[0]), minutes)

#The uid will be one higher than the highest one
event_uid = 0
if len(event_uids) != 0:
	event_uid = event_uids[len(event_uids) - 1] + 1

#Make the event
session.add(Event(name, event_uid, dueTime, foodEta, organizer, description))
session.commit()
