# Question

# There are N straight lines that are not parallel, and no three lines pass through the same point. These lines divide the plane into M regions.

# Write a function to find the maximum number of regions that can be obtained on the plane.

# Input

# An integer N representing the number of straight lines:

# 0 <= N <= 100

# Output

# Return the maximum number of regions.

# Examples

# Input:

# 2

# Output:

# 4

# Input:

# 3

# Output:

# 7
n = int(input())

ans = 1 + n * (n + 1) // 2

print(ans)