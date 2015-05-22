import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
import bibtexparser

from PS_DBgen import Article, Base

engine = create_engine('sqlite:///sqlite_paperscraper.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session   = DBSession()

r = requests.get("http://inspirehep.net/search?ln=en&ln=en&p=find+eprint+"+ sys.argv[1] + "&of=hx&action_search=Search&sf=earliestdate&so=d&rm=&rg=25&sc=0")

preIndex  = r.text.index('<pre>')+6
nPreIndex = r.text.index('</pre>')

entry = bibtexparser.loads(r.text[preIndex:nPreIndex]).entries[0]

entry['Ident'] = entry['id']
del entry['id']

entry['Type'] = entry['type']
del entry['type']

temp = session.query(Article).filter_by(eprint = sys.argv[1]).first()

if type(temp) == type(None):
	new_article = Article(**entry)
	session.add(new_article)
	session.commit()
	print "\n Added: " + sys.argv[1] + ": " + new_article.Ident + "\n"
else:
	print "\n" + sys.argv[1] + ": " + temp.Ident + "\n"