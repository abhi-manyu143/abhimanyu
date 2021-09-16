a=input("enter a string")
a=a.lower()
b=reverse(a)
if list(a)==list(b):
    print("string is palindrome")
else:
    print("string is not palindrome")
