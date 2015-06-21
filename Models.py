from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date, datetime

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
    date          = Column(Date())
#	year          = Column(Integer)
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
#			print "Encountered KeyError, article lacks a title"
            raise NoTitle(dictionary)

        if "doi" in result_dictionary:
            self.doi=result_dictionary

        self.recid=result_dictionary["recid"]

        if "prepublication" in result_dictionary:
            self.date=datetime.strptime(result_dictionary["prepublication"]["date"],"%Y-%m-%d").date()
            
#		if result_dictionary["year"]:
#			self.year=year

class NoTitle(Exception):
    def __init__(self,dictionary):
        self.dictionary=dictionary

    def __str__(self):
        return "NoTitle exception in article"+repr(self.dictionary)
