#http://www.pythontip.com/coding/code_oj_case/13
'''
a=52
oneCount=0
while True:
    if a%2!=0:
        a/=2
        oneCount+=1
    else:
        a/=2
    if a==0:
        break
print oneCount
'''
#convert ten to two

'''
a=52
M=[]
while True:
    if a%2!=0:
        a/=2
        M.append(1)
    else:
        a/=2
        M.append(0)
    if a==0:
        break
'''

def func(nameList):
    #for item in nameList:
    #    print item
    print nameList

L = ['33', '232']
#L = 232
func(L)