# Validate Subsequence

# 1. Understand the problem
#   Restate: Make a function that takes two lists, then check 
#   if values in the second list exist in the same order in the 
#   first list
#   Inputs: two lists
#   Outputs: Boolean
#   Labeling: parent_list, subset_list

# 2. Exploring Concrete Examples
#   isValidSubsequence([1, 2, 3, 4], [2, 4]) --> True
#   isValidSubsequence([1, 2, 3, 4], [3, 1]) --> False

# 3. Break it down
#   1. check if the second list is longer than the first list
#   2. If it is, we can return false
#   3. Using some different problem solving patterns, we loop over
#       Both the parent and subset list, checking if the values are
#       in the same order or even in the list at all

# 4. Simplify/Solve
def is_subsequence(parent_list, subset_list):
    if len(subset_list) > len(parent_list): return False
    parent_counter = 0
    subset_counter = 0
    while subset_counter < len(subset_list):
        if(parent_list[parent_counter] == subset_list[subset_counter]):
            if(parent_counter < subset_counter): return False
            parent_counter += 1
            subset_counter += 1
        else:
            parent_counter += 1
            if parent_counter >= len(parent_list): return False
    return True

print(is_subsequence([1, 2, 3, 4], [2, 4]))
print(is_subsequence([1, 2, 3, 4], [3, 1]))