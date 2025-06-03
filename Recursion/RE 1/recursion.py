count = 0
# This code demonstrates a simple recursive function that counts from 0 to 499.
# It uses a global variable to keep track of the count and prints each number.
def recursion():
    global count
    if count == 500: #base condition
        return
    print(count)
    count+= 1
    recursion()
    
recursion()