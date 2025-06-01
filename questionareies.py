#fist question
print("Hello,world!")
#question 2
name=input("your name:" )
Age= int(input("your age:"))
city=input("your city:")
print("Name:"  , name, end="" )
print("Age: "   ,Age, end="")
print("city:"  ,city,end=" ")
#question3
print("welcome to python!\n let's learn coding")
#question 4
print('He said,"python is amazing!"')
#question 5 pattern
row=int(input("Enter the number of row"))
for i in range(1,row+1):
    for j in range(0,i):
        print("*",end="")
    print("")
# question 6
name= input("enter your name")
age=int(input("enter your age")) 
print("hello , My name is ", name ,"and age is",age)
# question 7 5*5 multiplication table
size=5
for i in range(1,size+1):
    print(f"{i:2}|",end="")
    for j in range(1,size+1):
        print(f"{i*j:4}",end="")
    print("")
#question 8
word1="Apple"
word2="Banana"
word3="Cherry"
print(f"{word1:<10}" ,end="")
print(f"{word2:<10}",end=" ")
print(f"{word3:<10}")
#question 9
print(5+7)
#question 10
print("-item")
print("-Quantity")
print("-Price")
print("-Total")














