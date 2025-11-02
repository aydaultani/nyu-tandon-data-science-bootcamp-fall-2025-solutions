def num_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    print(count)

def animals():
    a = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
    for i in a:
        print(i.upper())

def odd_or_even_1_to_20():
    for i in range(1,21):
        if i % 2 == 0:
            print(i , ": Even")
        else:
            print(i, ": Odd")

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    done = False
    while left <= right:
        if s[left] != s[right]:
            print("Not a palindrome")
            done = True
            break
        left += 1
        right -= 1

    if not done:
        print("It is a palindrome")

def sum_of_integers():
    a = int(input("a: "))
    b = int(input("b: "))
    return a+b

def sum_of_integers_2(a,b): # Question wasn't clear so I here's both
    return a+b

