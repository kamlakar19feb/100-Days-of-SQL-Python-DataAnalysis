1️⃣ Find the GCD (Greatest Common Divisor) of two numbers using Euclidean algorithm.
👉 Example: gcd(48, 18) → 6

n1=int(input("Enter number n1: "))
n2=int(input("Enter number n2: "))
for i in range (min(n1,n2),0,-1):
    if n1%i==0 and n2%i==0:
      print("gcd of ", n1, "and", n2, "is ", i)
      break


true Euclidean algorithm, it’s shorter and faster:

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
print("GCD =", gcd(n1, n2))
