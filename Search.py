import requests
import bibtexparser
import json
from Models import *

#testRequest = requests.get("http://inspirehep.net/search?ln=en&ln=en&p=find+eprint+1506.01386&of=hx&action_search=Search&sf=earliestdate&so=d&rm=&rg=25&sc=0")

#class SpiresFormat():
#	formatRequestPrefix="&of="
#	def __init__(self,name,format_string,record_tag):
#		self.name=name
#		self.format_string=format_string
#		self.record_tag=record_tag

#	def formatRequest(self):
#		return self.formatRequestPrefix+self.formatString

#spiresBibtex=SpiresFormat("bibtex","hx","pre")
#spiresJson=SpiresFormat("json","recjson","")

class SpiresSearch():
  inspire_url="http://www.inspirehep.net/search?"
  static_options={"of":"recjson","ot":"recid,authors,title,doi,system_control_number,journal_info,year,prepublication,publication_info"}

  def __init__(self,search_string,chunk_size=25,jump=1):

		self.chunk_size=chunk_size
		self.jump=jump
#		self.static_options=static_options
		self.search_string=search_string
		self.generate_request_string()
		self.requested_flag=False

  def update_options(self):
    self.search_options=self.static_options
    self.search_options["rg"]=str(self.chunk_size)
    self.search_options["jrec"]=str(self.jump)

  def generate_request_string(self):
    # generates the actual spires search string
    self.request_string=self.inspire_url+"&p="+self.search_string
    self.update_options()
    for key, value in self.search_options.items():
      self.request_string+="&"+key+"="+value
  def get_previous_chunk(self):
    if self.jump>self.chunk_size:
      self.jump-=self.chunk_size
    else:
      print "chunk size larger than offset. Resetting search to first chunk"
      self.jump=1
    self.perform_request()

  def get_next_chunk(self):
    self.jump+=self.chunk_size
    self.perform_request()

  def perform_request(self):
    self.generate_request_string()
    self.requested_flag=True
    self.request=requests.get(self.request_string)

  def parse_result(self):
    if not self.requested_flag:
      self.perform_request()
    return json.loads(self.request.text)

#class SpiresBibtexRequest():
#	inspire_url="http://inspirehep.net/search?"

#	def __init__(self,search_string,data_format=spiresBibtex,chunk_size=25,jump=1,
#			static_options={"sf" : "earliestdate"}):
#
#		self.chunk_size=chunk_size
#		self.jump=jump
#		self.data_format=data_format
#		self.static_options=static_options
#		self.search_string=search_string
#		self.generate_request_string()
#
#		self.parser=SpiresHTMLParser(data_format)
#		self.requested_flag=False
#
#	def update_options(self):
#		self.search_options=self.static_options
#		self.search_options["of"]=self.data_format.format_string
#		self.search_options["rg"]=str(self.chunk_size)
#		self.search_options["jrec"]=str(self.jump)
#
#	def generate_request_string(self):
#		# generates the actual spires search string
#		self.request_string=self.inspire_url+"&p="+self.search_string
#		# adds the options, including the data format
#		self.update_options()
#		for key, value in self.search_options.items():
#			self.request_string+="&"+key+"="+value



#	def get_previous_chunk(self):
#		if self.jump>self.chunk_size:
#			self.jump-=self.chunk_size
#		else:
#			print "chunk size larger than offset. Resetting search to first chunk"
#			self.jump=1
#		self.perform_request()
#
#	def get_next_chunk(self):
#		self.jump+=self.chunk_size
#		self.perform_request()
#
#	def perform_request(self):
#		self.generate_request_string()
#		self.requested_flag=True
#		self.request=requests.get(self.request_string)

#	def parse_request(self):
#		if not self.requested_flag:
#			self.perform_request()
#		return self.parser.get_tag_data(self.request.text)
#
#class SpiresBibtexSearch(SpiresSearch):
#
#	def __init__(self,search_string,chunk_size=25,jump=1,
#			static_options={"sf" : "earliestdate"}):
#		SpiresSearch.__init__(self,search_string,data_format=spiresBibtex,
#					chunk_size=chunk_size,jump=jump,
#					static_options=static_options)

#class SpiresBibtexEprintSearch(SpiresBibtexSearch):
#	def __init__(self,eprint_num):
#		SpiresBibtexSearch.__init__(self,"find eprint+"+eprint_num)


#class SpiresBibtexDoiSearch(SpiresBibtexSearch):
#	def __init__(self,doi):
#		SpiresBibtexSearch.__init__(self,"find doi+"+doi)


#test_search=SpiresBibtexEprintSearch("0709.2877")
