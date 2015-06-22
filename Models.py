from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date, datetime
from HTMLParser import HTMLParser
import requests
#from Search import *

Base = declarative_base()

class Article(Base):

    __tablename__ = 'articles'

    id            = Column(Integer, primary_key=True)
    recid		  = Column(Integer)
    title         = Column(String(250))
#	author        = Column(String(250))
#		I will make an author class separately and 
#		establish a many-to-many relation between 
#		articles and authors
    eprint        = Column(String(250))
    doi           = Column(String(250))
    date          = Column(Date())
    bibtex        = Column(String(2000))
#	slaccitation  = Column(String(250))
#	journal       = Column(String(250))
#	primaryclass  = Column(String(250))
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
            raise NoTitle(dictionary)

        if "doi" in result_dictionary:
            self.doi=result_dictionary

        self.recid=result_dictionary["recid"]

        if "prepublication" in result_dictionary:
            self.date=datetime.strptime(result_dictionary["prepublication"]["date"],"%Y-%m-%d").date()
        
    def get_bibtex(self):    
        request_url="http://inspirehep.net/record/"+str(self.recid)+"?of=hx"
#        try:
        bibtex_request=requests.get(request_url)
#        except:
#            raise RequestError() 
        parser=SpiresHTMLParser(bibtex_request.text)
        self.bibtex=parser.get_tag_data()

class RequestError(Exception):
    def __str__(self):
        "Some strange thing happened to this request"
            
class NoTitle(Exception):
    def __init__(self,dictionary):
        self.dictionary=dictionary

    def __str__(self):
        return "NoTitle exception in article"+repr(self.dictionary)

class SpiresHTMLParser(HTMLParser):
    def __init__(self,request_data):
        HTMLParser.__init__(self)
        self.pre_flag=False
#		self.data_format=data_format
        self.record_tag="pre"
        self.request_data=request_data

    def get_tag_data(self):
        self.results=[]
        self.feed(self.request_data)
        self.result=''
        for item in self.results:
            self.result+=item
        return self.result

    def handle_starttag(self,tag,attrs):
		if tag==self.record_tag:
#			print "found start-tag "+tag
			self.pre_flag=True

    def handle_endtag(self,tag):
        if tag==self.record_tag:
#			print "found end-tag "+tag
            self.pre_flag=False

    def handle_data(self,data):
 #       self.results=""
        if self.pre_flag:
            print "Found bibtex: "+data
            self.results.append(data)
#        return self.results
