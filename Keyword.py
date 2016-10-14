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
		return  str(self.filename)#+ "," + self.casename)#+" : "+ str(len(self.keywords)))

class KeywordMapping:
	def __init__(self,keywordlist=[],filelist=[]):
		self.keywordlist=keywordlist
		self.filelist=filelist

	def getfilelist(self):
		return [str(i) for i in self.filelist]

	def __str__(self):
		return str(str(self.keywordlist) +" --- "+  ",".join([str(i) for i in self.filelist]))



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








def getGraph(filenamelist):
	f=[Keyword(filename) for filename in filenamelist]

	for fs in f:
		print fs
	joint= joinkeywords(f)

	savedgroups=groupkeywords(joint)

	keywordmappinglist=[]
	for i in savedgroups:
		#print i
		tempfilelist=[]
		for j in f: # Check in each file list about the keyword groups
			if bool(set(j.keywords) &(set(i))):
				tempfilelist.append(j)
		keywordmappinglist.append(KeywordMapping(list(set(i)),tempfilelist))

	return keywordmappinglist




if __name__=="__main__":
	for i in getGraph(["6.json","9.json","16.json"]):
		print i



