#http://www.pythontip.com/coding/code_oj?page=2
L=[2,5,9,15,27]
sum=1
for each in L:
    sum*=each
while True:
    if sum%10==0:
        sum=int(sum/10)
    else:
        print(sum)
        break
M=list(str(sum))
count=int(M[(len(M)-1)])
if count%2==0:
    print(0)
else:
    print(1)

