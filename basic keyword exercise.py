#fist question
import keyword
kw=keyword.kwlist
print(kw)
#second question conditional statments
x=int(input("enter number"))
if x>0:
    print("postive number")
elif x==0:
    #print("zero") 
#else:
    print("negative number")    
#question 3  loops
for i in range(5):
    print(i)
#while loop
i=0
while(i<5):
    print("count is",i) 
    i=i+1
#continue
for i in range(5):
    if i==2:
        continue
    print(i) 
#break 
for i in range(5):
    if i==2:
        break
    print(i)
#question 4 boolen keyword
a=True
b=False
c=None 
print(a) 
print(b)
print(c)
#question 5  manually sort
keywords=["banana","apple","cherry","data","fig"]
n=len(keywords)
for i in range(n):
    for j in range(0,n-i-1):
        if keywords[j]>keywords[j+1]:
            keywords[j],keywords[j+1]=keywords[j+1],keywords[j]
print("stored keyword")
for word in keywords:
    print(word)
#question 6
print("The keyword 'if' is uesd to check condition") 
#question 7 all capital letter version 5 keyword
print(" RETURN,AS,ASSERT,IN,IS") 
#QUESTION 10
print(f"{'sql':<10}") 
print(f"{'copyedit':<10}")
print(f"{'keyword':<10}|{'use'}")
print(f"{'if':<10}|{'condition checak'}")
print(f"{'while':<10}|{'loop'}")
print(f"{'break':<10}|{'exit loop'}")
