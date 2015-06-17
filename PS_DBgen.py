import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Article(Base):

	__tablename__ = 'articles'

	id            = Column(Integer, primary_key=True)
	recid		  = Column(Integer)
#	slaccitation  = Column(String(250))
	title         = Column(String(250))
#	author        = Column(String(250))
#		I will make an author class separately and 
#		establish a many-to-many relation between 
#		articles and authors
	eprint        = Column(String(250))
	doi           = Column(String(250))
#	journal       = Column(String(250))
#	primaryclass  = Column(String(250))
	year          = Column(Integer)
#	archiveprefix = Column(String(250))
#	Type          = Column(String(250))
#	Ident         = Column(String(250))
#	address       = Column(String(250))
#	booktitle     = Column(String(250))
#	chapter       = Column(String(250))
#	crossref      = Column(String(250))
#	edition       = Column(String(250))
#	editor        = Column(String(250))
#	Name          = Column(String(250))
#	howpublished  = Column(String(250))
#	institution   = Column(String(250))
#	key           = Column(String(250))
#	month         = Column(String(250))
#	note          = Column(String(250))
#	number        = Column(String(250))
#	organization  = Column(String(250))
#	pages         = Column(String(250))
#	publisher     = Column(String(250))
#	school        = Column(String(250))
#	series        = Column(String(250))
#	volume        = Column(String(250))

	def __init__(self,result_dictionary):
		try:
			self.title=result_dictionary["title"]["title"]
		except KeyError:
			print "Encountered KeyError, article lacks a title"
			return False

		if result_dictionary["doi"]:
			self.doi=result_dictionary
		self.recid=result_dictionary["recid"]

		if result_dictionary["year"]:
			self.year=year




#engine = create_engine('sqlite:///sqlite_paperscraper.db')

#Base.metadata.create_all(engine)


#
## List of fields
#

