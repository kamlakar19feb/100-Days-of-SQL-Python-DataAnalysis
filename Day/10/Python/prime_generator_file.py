Write a function that generates all prime numbers up to n and saves them into a text file (primes.txt).

n=int(input("Enter range: "))
prime_list=[]
for i in range (2,n+1):
  for j in range (2,int(i**0.5) + 1):
    if i%j==0:
      break
  else:
    prime_list.append(i)
print(prime_list)
with open("primes.txt","w") as f:
  f.write(str(prime_list))
