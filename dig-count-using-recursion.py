def digcount(n):
    if n==0:
        return 0
    else:
        return 1+digcount(n//10)
n=int(input())
print(digcount(n))
