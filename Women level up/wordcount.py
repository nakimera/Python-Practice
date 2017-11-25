a='foof foof this and that this'
words=a.split(' ')
dic={}
for word in words:
    if dic.key(word):
        dic[word]+=1
    else:
        dic[word]=1

print (dic)
