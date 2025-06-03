def f(i,sum):
    if i<1:
        print(sum)
        return
    f(i-1,sum+i)
    
    
f(100,0)

# Functional recursion
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

ans=factorial(3)
print(ans)