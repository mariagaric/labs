#Lab4

#Task 4.2 Fibbonacci 
def fibonacci (limit):
    a=0
    b=1
    while a<= limit:
        yield a 
        a,b= b, a+b

for i in fibonacci(1000000):
    print(i)