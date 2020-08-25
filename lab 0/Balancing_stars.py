string=str(input())
open=['[','{','(']
close=[']','}',')']
stack=[]
count=0
br=0 #brackets counting
sc=0 #stars counting
f=0 #if condition failed
ob=0 #for open brackets
for i in string:
    if i in open:
        stack.append(i)
        br=br+1
        ob=1
    elif i=='*' and ob==1:
        sc=sc+1
    elif i in close:
        pos=close.index(i)
        if(len(stack)>0) and (open[pos]==stack[len(stack)-1]):
            stack.pop()
            if sc>=2:
                count=count+br
                sc=0
                ob=0
                br=0
            elif ob==1:
               f=1
        else:
            f=1
if len(stack)==0 and f==0 and count>0:
    print('yes',count)
else:
    print('No',count)
    
