# Question 4 — Sum of Odd Integers in Array
# Problem Statement

# An odd number is an integer which is not a multiple of 2.

# You are required to implement the following function:

# int SumOddIntegers(int arr[], int n);

# The function accepts an integer array arr of length n and should calculate and return the sum of all odd integers in the array.

# Input
# First line: integer n, the size of the array.
# Second line: n space-separated integers representing the array elements.
# Example

# Input:

# 8
# 1 4 6 7 10 12 11 5

# Output:

# 24

# Because the odd numbers are:

# 1 + 7 + 11 + 5 = 24

# Another Example

# Input:

# 12
# 2 4 9 7 11 13 25 31 6 8 10 24

# Output:

# 96

n=int(input())
arr=list(map(int,input().split()))
su=0
for i in arr:
    if i%2!=0:
        su+=i

print(su)