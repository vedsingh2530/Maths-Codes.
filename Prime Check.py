#python 3.7.1

#Night_owl_net  - Code By !!

print("Welcome To 'Prime Checker' By ved_singh_1830")
print(" ")

Num=int(input("Enter A Number To Check it's Prime or Not - "))
A=0
for i in range(2,Num):
  if Num%i==0:
    A=1
    break

if A==1:
  print("Not A Prime Number.")
else:
  print("Prime Number.")