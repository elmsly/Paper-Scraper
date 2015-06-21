#!/usr/bin/python
import os.path
from Conf import *
from Models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if not os.path.isfile(db_path):
    engine = create_engine('sqlite:///'+db_path)
    Base.metadata.create_all(engine)
else:
    print "Database already exists"

#
## List of fields
#

