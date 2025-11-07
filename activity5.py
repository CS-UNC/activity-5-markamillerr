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

def more_than_20(file):
    wrds= open(file)
    ret_list= []
    for i in wrds:
        x= i.strip()
        if len(x)> 20:
            ret_list.append(x)
    return ret_list

# print(more_than_20('CROSSWD.txt'))

def has_no_e(word):    
    if 'e' in word:
        return False 
    else:
        return True

# print(has_no_e('allegory'))

def uses_only(word, letters):
    # temp = letters
    for letter in word:
        if letter not in letters:
            return False
    return True  
           
#print(uses_only('abra','abr'))
    
def all_uses_only(file,letters):
    result=[]
    f= open(file,'r')
    for line in f:
        word= line.strip()
        if uses_only(word,letters):
            result.append(word)

    return result 