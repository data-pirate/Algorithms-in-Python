# TWO SUM PROBLEM:
# In this problem we need to find the terms in array which result in target sum
# for example taking array = [1,5,5,15,6,3,5]
# and we are told to find if array consists of a pair whose sum is 8

# There can be 3 possible solutions to this problem

#solution 1: brute force
# this might not be the best choice to get the job done but will be easy to implement
# time complexity: O(n^2)

def two_sum_brute_force(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j])
                return True
    return False

arr = [9,3,1,4,5,1]
target = 13
print(two_sum_brute_force(arr, target))
# prints 9 4 True

# solution 2: Hash table
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_table(A, target):
  ht = dict()
  for i in range(len(A)):
    if A[i] in ht:
      print(ht[A[i]], A[i])
      return True
    else:
      ht[target - A[i]] = A[i]
  return False

A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum_hash_table(A,target))

# solution 3: Using to indices
#  Here, we have two indices that we keep track of,
# one at the front and one at the back. We move either
# the left or right indices based on whether the sum of the elements
# at these indices is either greater than or less than the target element.

# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(A, target):
  i = 0
  j = len(A) - 1
  while i < j:
    if A[i] + A[j] == target:
      print(A[i], A[j])
      return True
    elif A[i] + A[j] < target:
      i += 1
    else:
      j -= 1
  return False

A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum(A,target))
