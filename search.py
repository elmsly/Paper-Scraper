import requests
import bibtexparser
from HTMLParser import HTMLParser

#testRequest = requests.get("http://inspirehep.net/search?ln=en&ln=en&p=find+eprint+1506.01386&of=hx&action_search=Search&sf=earliestdate&so=d&rm=&rg=25&sc=0")

class spiresFormat():
#	formatRequestPrefix="&of="
	def __init__(self,name,formatString,recordTag):
		self.name=name
		self.formatString=formatString
		self.recordTag=recordTag

#	def formatRequest(self):
#		return self.formatRequestPrefix+self.formatString

spiresBibtex=spiresFormat("bibtex","hx","pre")

class spiresSearch():
	requestStringPre="http://inspirehep.net/search?"
	requestStringPost=""

	def __init__(self,searchString,dataFormat=spiresBibtex,chunkSize=25,jump=1,
			staticOptions={"sf" : "earliestdate"}):

		self.chunkSize=chunkSize
		self.jump=jump
		self.dataFormat=dataFormat
		self.staticOptions=staticOptions
#		self.updateOptions()
		self.searchString=searchString
		self.generateRequestString()

		self.parser=spiresHTMLParser(dataFormat)
		self.requestedFlag=False

	def updateOptions(self):
		self.searchOptions=self.staticOptions
		self.searchOptions["of"]=self.dataFormat.formatString
		self.searchOptions["rg"]=str(self.chunkSize)
		self.searchOptions["jrec"]=str(self.jump)

	def generateRequestString(self):
		# generates the actual spires search string 
		self.requestString=self.requestStringPre+"&p="+self.searchString
#		self.requestString+=dataFormat.formatRequest()
		# adds the options, including the data format
		self.updateOptions()
		for key, value in self.searchOptions.items():
			self.requestString+="&"+key+"="+value

		self.requestString+=self.requestStringPost

	def getPreviousChunk(self):
		if self.jump>self.chunkSize:
			self.jump-=self.chunkSize
		else:
			print "chunk size larger than offset. Resetting search to first chunk"
			self.jump=1
#		self.updateOptions()
#		self.generateRequestString()
		self.performRequest()

	def getNextChunk(self):
		self.jump+=self.chunkSize
#		self.updateOptions()
#		self.generateRequestString()
		self.performRequest()
		
	def performRequest(self):
		self.generateRequestString()
		self.requestedFlag=True
		self.request=requests.get(self.requestString)

	def parseRequest(self):
		if not self.requestedFlag:
			self.performRequest()
		return self.parser.getTagData(self.request.text)

class spiresBibtexSearch(spiresSearch):

	def __init__(self,searchString,chunkSize=25,jump=1,
			staticOptions={"sf" : "earliestdate"}):
		spiresSearch.__init__(self,searchString,dataFormat=spiresBibtex,
					chunkSize=chunkSize,jump=jump,
					staticOptions=staticOptions)

class spiresBibtexEprintSearch(spiresBibtexSearch):
	def __init__(self,eprintNum):
		spiresBibtexSearch.__init__(self,"find eprint+"+eprintNum)


class spiresBibtexDoiSearch(spiresBibtexSearch):
	def __init__(self,doi):
		spiresBibtexSearch.__init__(self,"find doi+"+doi)
		

class spiresHTMLParser(HTMLParser):
	def __init__(self,dataFormat):
		HTMLParser.__init__(self)
		self.preFlag=0
		self.dataFormat=dataFormat
		self.recordTag=dataFormat.recordTag

	def getTagData(self,text):
		self.results=[]
		self.feed(text)
		return self.results

	def handle_starttag(self,tag,attrs):
		if tag==self.recordTag:
#			print "found start-tag "+tag
			self.preFlag=True
	
	def handle_endtag(self,tag):
		if tag==self.recordTag:
#			print "found end-tag "+tag
			self.preFlag=False

	def handle_data(self,data):
		if self.preFlag:
#			print "Found bibtex: "+data
			self.results.append(data)


#testSearch=spiresBibtexSearch("find+a+gardi")
testSearch=spiresBibtexEprintSearch("0709.2877")
