#http://www.pythontip.com/coding/code_oj_case/17
'''
def fun(a,b):
    if a>b:
        min=b
    else:
        min=a
    count=0
    for M in range(1,min+1):
        if a%M==0 and b%M==0:
            count+=1
    print count
fun(120,90)
'''
a=120
b=90
print len([x for x in range(1,a+1) if a % x ==0 and b % x ==0])