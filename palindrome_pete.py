# Palindrome Check

# 1. Understand the Problem
#   Restate: Check if the word is the same backwards as it is forwards
#   Inputs: str
#   Outputs: Boolean
#   Labeling: call our variable we will be checking something like str_to_check

#2. Exploring Concrete Examples
#   Small: is_palindrome('racecar') --> True
#   More complex: is_palindrome('pancakes') --> False
#   Edge Cases: is_palindrome(10) --> None or Undefined or Null
#   Edge Cases: is_palindrome() --> None or False

#3. Break it down
#   1. Ask the user a string
#   2. Reverse the string
#   3. Check if the reversed string is the same as the original
#   4. Print true if it is, false otherwise.

#4. Simplify/Solve
def is_palindrome(str_to_check):
    if not isinstance(str_to_check, str): return None
    str_to_check = str_to_check.lower()
    new_str = ''
    count = len(str_to_check) - 1
    # Reverses the string
    while count >= 0:
        new_str += str_to_check[count]
        count -= 1
    # Checks if new_str is the same as str_to_check
    return new_str == str_to_check

# print(is_palindrome('Racecar'))
# print(is_palindrome('pancakes'))
# print(is_palindrome(10))

#5. Refactor Using Built in methods
# the list(str) creates an list of characters...we do this so we can access the reverse
# built in method that lists have. We then use the method, which is automatically saved
# we then convert the reversed list back to a string using the ''.join() string method
# and finally we compare the original to the reversed
def is_palindrome2(str_to_check):
    if not isinstance(str_to_check, str): return None
    new_list = list(str_to_check.lower())
    new_list.reverse()
    return str_to_check.lower() == ''.join(new_list)

# print(is_palindrome2('Racecar'))
# print(is_palindrome2('pancakes'))
# print(is_palindrome2(10))

#Refactor using multiple pointers problem solving pattern
# Multiple pointers Patter: 
    # Essentially creating pointers that correspond to different indeces in a list
    # We then have the pointers move to the beginning middle or end based on diff. conditions
    # Can help us from using nested loops
def is_palindrome3(str_to_check):
    if not isinstance(str_to_check, str): return None
    if len(str_to_check) % 2 == 0: return False
    str_to_check = str_to_check.lower()
    start = 0
    end = len(str_to_check) - 1
    while start < end:
        if(str_to_check[start] != str_to_check[end]):
            return False
        start += 1
        end -= 1
    return True

print(is_palindrome3('Racecar'))
print(is_palindrome3('pancakes'))
print(is_palindrome3(10))