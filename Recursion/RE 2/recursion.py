#print name using recursion n times
def print_name(name, n):
    if n <= 0:
        return
    print(name)
    print_name(name, n - 1)

# print_name("Nikhil", 12)

# print linearly from 1 to n using recursion
def rec(n,i):
    if i>n:
        return 
    print(i)
    rec(n, i + 1)
    
# rec(10, 1)

#print from 1 to n using backtracking
def f(n,i):
    if i<1:
        return 
    f(n,i-1)
    print(i)
    
f(10,10)

