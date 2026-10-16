a,b,c=map(int,input().split())
if(a==b==c):
    print("Tam giac deu")
elif(a==b or b==c or a==c):
    print("Tam giac can")
if(a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a):
    print("Tam giac vuong")
else:
    print("Tam giac thuong")