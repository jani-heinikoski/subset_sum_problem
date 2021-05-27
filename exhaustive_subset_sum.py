#####
# Author: Jani Heinikoski
# Last modified: 27.05.2021
# Description:
# Finds all possible subsets of elements in vector whose sum equals the target variable exhaustively
# by trying all of the possible combinations.
# Time complexity of the solution is pseudo-polynomial with upper limit of O(2^n), where n is the length of the element vector.
# Prerequisites:
# Vector contains only unique, positive integers
#####

# Vector of all elements
vector = [1, 2, 3, 4, 5]
# Vector which indicates which elements from above vector are included in the subset
inclusion_vector = []
# Wanted target sum
target = 9
# Counts the amount of recursive calls to solution -function
rec_iters = 0
# Inclusion vector must be the same length as vector and contain zeros when initialized.
for _ in range(len(vector)):
    inclusion_vector.append(0)

def solution(inclusion_vector: list, idx: int):
    global rec_iters
    rec_iters += 1
    current_sum = 0
    subset = []
    index = 0
    # Loop through the inclusion vector and append included elements to the subset
    for included in inclusion_vector:
        if (included):
            subset.append(vector[index])
        index += 1
    # Sum the elements in subset -vector
    current_sum = sum(subset)
    # If the subset's sum matches the target, print it and return
    if (current_sum == target):
        print(subset)
        return
    # If it exceedes the target, do not try further and just return (improves time complexity)
    elif (current_sum > target):
        return
    # If no more elements are left to add, return
    if (idx == len(inclusion_vector)):
        return
    # Include the element at index idx and call the solution function.
    # Also, call the solution function where the element at idx is not included,
    # this yields all possible combinations.
    inclusion_vector[idx] = 1
    idx += 1
    solution(inclusion_vector, idx)
    idx -= 1
    inclusion_vector[idx] = 0
    idx += 1
    solution(inclusion_vector, idx)
    
solution(inclusion_vector, 0)
print(rec_iters)