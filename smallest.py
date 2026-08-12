# Write a program to find the smallest number in a given array of integers. The first line of the input will be an integer indicating how many array elements are being input. If we let n denote this number, the following n lines of input will have one integer each.

# (2022 Hirepro)

# Sample Input:

# 3
# 2
# 10
# -1

# Output:

# -1

n=int(input())
arr=[int(input() )for _ in range(n)]
print(min(arr))