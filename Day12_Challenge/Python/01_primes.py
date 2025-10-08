Write a program to find all prime numbers between 10 and 50.

print("Enter range between which list of prime numbers to be found:")
n1=int(input("Enter Lower limit: "))
n2=int(input("Enter Upper limit: "))
list_prime=[]
for i in range(n1,n2+1):
  for j in range(2,int(pow(i,0.5))+1):
    if i%j==0:
      break
  else:
    list_prime.append(i)
print("list of prime numbers between 10 and 50: ",list_prime)
