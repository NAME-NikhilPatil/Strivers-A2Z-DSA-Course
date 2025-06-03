# Reverse an array using recursion  
def reverse_array(arr, start, end):
    
    if start >= end:
        print(arr)
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start + 1, end - 1)
    
# reverse_array([1, 2, 3, 4, 5], 0, 4)

def reverse_array_using_single_variable(arr, start):
    
    if start >= len(arr) // 2:
        print(arr)
        return
    arr[start], arr[len(arr) - start - 1] = arr[len(arr) - start - 1], arr[start]
    reverse_array_using_single_variable(arr, start + 1,)
    
# reverse_array_using_single_variable([1, 2, 3, 4, 5], 0)

#check if the string is a palindrome or not using recursion
def is_palindrome(s, start, end):
    
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome(s, start + 1, end - 1)

print(is_palindrome("racecwr", 0, 6))  # True