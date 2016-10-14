import json
import itertools
import difflib

tolerance=0.5

def create_keyword(filename):
	return Keyword(filename)

class Keyword:
	def __init__(self,json1):
		with open(json1) as data_file:
			data = json.load(data_file)
		self.casename = data['casename']
		self.keywords= data['keywords']
		self.filename =data['filename']


	def __str__(self):
		return  str(self.filename +" : "+ str(len(self.keywords)))

class KeywordMapping:
	def __init__(self,keywordlist=[],filelist=[]):
		self.keywordlist=keywordlist
		self.filelist=filelist

	def __str__(self):
		return str(",".join(self.keywordlist) +"--" ",".join(self.filelist))



def joinkeywords(filelist):
	temp=[]
	for f in filelist:
		temp+=f.keywords
	return temp


def same (a,b):
	d = difflib.SequenceMatcher(None, a, b).ratio()
	if(d > tolerance):
			return True
	return False

def groupkeywords(allkeywordlist):
	visited=[False for _ in xrange(len(allkeywordlist))]
	#print visited
	set=[]
	for i in xrange(len(allkeywordlist)):
		if not visited[i]:
			temp=[]
			for j in xrange(len(allkeywordlist)):
				if (not visited[j] ):
					if(same(allkeywordlist[i],allkeywordlist[j])):
						visited[j]=True
						temp.append(allkeywordlist[j])
			set.append(temp)
	return set








if __name__=="__main__":

	f=[Keyword(filename) for filename in ["6.json","9.json","16.json"]]

	for fs in f:
		print fs
	joint= joinkeywords(f)

	for i in (groupkeywords(joint)):
		print i



