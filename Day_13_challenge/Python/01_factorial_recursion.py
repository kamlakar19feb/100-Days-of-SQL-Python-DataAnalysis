1️⃣ Find the factorial of a number using recursion.
👉 Input: 5 → Output: 120

def fact(n):
  if n ==1:
    return 1
  else:
    return n*fact(n-1)
fact(5)
