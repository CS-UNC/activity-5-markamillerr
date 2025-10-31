wordsfile= open('CROSSWD.txt','r')
#print(wordsfile.readline())
#print(wordsfile.readline())
#print(wordsfile.readline())
#print(wordsfile.readline())
#words=[]
#for i in wordsfile:
    #words.(append.readline())
    #print(i.strip())
#print(type(wordsfile))
#for k in dir(wordsfile):
#    if '__' not in k:
#       print(k)
# print ([x for x in dir(wordsfile) if 'read' in x])

def twenty_or_more(file):
    result= []
    for i in file:
        if file[i] > 20:
            result.append(file[i])
    return result

print(twenty_or_more(wordsfile))