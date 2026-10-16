a,b=map(int,input().split())
if(a==0):
    if(b==0):
        print("Vo so nghiem")
    elif(b!=0):
        print("Vo nghiem")
elif(a!=0):
    x=-b/a
    print("Nghiem cua pt:",x)

