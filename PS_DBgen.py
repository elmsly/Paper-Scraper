import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Article(Base):

	__tablename__ = 'article'

	id            = Column(Integer, primary_key=True)
	slaccitation  = Column(String(250))
	title         = Column(String(250))
	author        = Column(String(250))
	eprint        = Column(String(250))
	doi           = Column(String(250))
	journal       = Column(String(250))
	primaryclass  = Column(String(250))
	year          = Column(String(250))
	archiveprefix = Column(String(250))
	Type          = Column(String(250))
	Ident         = Column(String(250))

engine = create_engine('sqlite:///sqlite_paperscraper.db')

Base.metadata.create_all(engine)