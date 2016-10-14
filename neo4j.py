from __future__ import print_function
import Keyword
from os import listdir
from os.path import isfile, join
import codecs
from py2neo import Graph, Path,authenticate


def fix_json():
    mypath="json"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i in onlyfiles:
        with open(mypath+"/"+i) as text_file:
            print( "Fixing ", mypath+"/"+i)
            newlines =[ line.replace("u\'","\'")  for line in text_file]

        with codecs.open(mypath+"/"+i, 'w', encoding='utf8') as f:
            for s in newlines:
                f.write(s)

"""
from py2neo import Graph, Path,authenticate

authenticate("localhost:7474", "neo4j", "aniketd9")


# connect to authenticated graph database
graph = Graph("http://localhost:7474/db/data/")

tx = graph.cypher.begin()
for name in ["Alice", "Bob", "Carol"]:
    tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
alice, bob, carol = [result.one for result in tx.commit()]

friends = Path(alice, "KNOWS", bob, "KNOWS", carol)
graph.create(friends)

"""



authenticate("localhost:7474", "neo4j", "aniketd9")


# connect to authenticated graph database
graph = Graph("http://localhost:7474/db/data/")



#fix_json()

mypath="json"
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#onlyfiles=["6.json","9.json","16.json"]

onlyfiles=["t1.json","t2.json","t3.json"]

graphMapping=Keyword.getGraph(mypath,onlyfiles)

# for i in graphMapping:
#     #print i.keywordlist,i.getcasename()
#
#     for j in i.getcasename():
#         tx = graph.cypher.begin()
#         tx.append("CREATE (keyword:KEYWORD {keywords:{list}}) RETURN KEYWORD", list=",".join(i.keywordlist))
#         s=[result.one for result in tx.commit()]
#         tx.append("CREATE (file:FILE {name:{n}}) RETURN FILE", n=j)
#         t=[result.one for result in tx.commit()]
#
#         for u in s:
#             friends = Path(u ,"CONTAINS" , t)
#         graph.create(friends)



print ("CREATE " ,end='')
temp=[]
for m,i in enumerate(graphMapping):
    #print i.keywordlist,i.getcasename()
    temp.append( "(k"+str(m)+":KEYWORD { list : \" "+",".join(i.keywordlist)+"\"})" )
print (",".join(temp))

print()

print ("CREATE " ,end='')
temp=[]

f=[Keyword.Keyword(mypath+"/"+filename) for filename in onlyfiles]
for m,k in enumerate(f):
    temp.append( "(f"+str(m)+":FILE { name : \" "+k.casename+"\"})" )
print (",".join(temp))


print()

for m,i in enumerate(graphMapping):
    kl=",".join(i.keywordlist)
    print ("MATCH " ,end='')
    for j in i.getcasename():
        print("(k:KEYWORD { list :\" "+kl+"\"}) , (f:FILE{name:\" "+j+"\"}) \nCREATE (k)-[:IS_CONTAINED_IN]-> (f)\n\n" )


print("MATCH (n) DETACH\nDELETE n")
