def fibo(n):
  if n<=1:
    return n
  else:
    return (fibo(n-1) + fibo(n-2))

terms= int(input("Enter Number of Terms: "))

if terms<=0:
 print("Enter Positive Integer")
else:
 print("Fibonacci Sequence: ")
 for i in range(terms):
     print(fibo(i))
  