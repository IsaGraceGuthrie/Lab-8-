#the authors are Isa Grace Guthrie and Ellen Kevin
#part 1
import math
def total_length(x):
    w=0
    for item in x:
        w=len(item)+w
    print(w)
total_length(['queen','rule'])
total_length(['ball','help','me','please'])

#the authors are Isa Grace Guthrie and Ellen Kevin
#part 2
s="abracadabra"
index=12
while 0<index<=len(s)+1:
    index-=1
    print(s[:index])

#the authors are Isa Grace Guthrie and Ellen Kevin
#part 3
def count_character(x,y):
    total=0
    index=0
    while index>=0:
        index=index+1
        for w in x:
            if w==y:
                total+=1
        if index==1:
            break
    print(total)
count_character("bonobos","o")
count_character("hellllloo","l")

#the authors are Isa Grace Guthrie and Ellen Kevin
#part 4
def until_dot(s):
    index=0
    while index<len(x) and x[index]!=".":
        index+=1
    print(x[:index])
