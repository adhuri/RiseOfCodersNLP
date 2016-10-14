import json
import itertools
import difflib


tolerance=0.5


def _byteify(data, ignore_dicts = False):
	# if this is a unicode string, return its string representation
	if isinstance(data, unicode):
		return data.encode('utf-8')
	# if this is a list of values, return list of byteified values
	if isinstance(data, list):
		return [ _byteify(item, ignore_dicts=True) for item in data ]
	# if this is a dictionary, return dictionary of byteified keys and values
	# but only if we haven't already byteified it
	if isinstance(data, dict) and not ignore_dicts:
		return {
			_byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
			for key, value in data.iteritems()
		}
	# if it's anything else, return it in its original form
	return data

def json_load_byteified(file_handle):
	return _byteify(
		json.load(file_handle, object_hook=_byteify),
		ignore_dicts=True
	)

def json_loads_byteified(json_text):
	return _byteify(
		json.loads(json_text, object_hook=_byteify),
		ignore_dicts=True)

def create_keyword(filename):
	return Keyword(filename)

class Keyword:
	def __init__(self,json1):
		temp=""
		with open(json1) as data_file:
			data=json.load(data_file)
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

	def getcasename(self):
		return [i.casename for i in self.filelist]

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








def getGraph(dir,filenamelist):
	f=[Keyword(dir+"/"+filename) for filename in filenamelist]

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



