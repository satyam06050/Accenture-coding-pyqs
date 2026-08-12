#     Edward’s Birthday

# It is Edward's birthday today. His friends have bought him a huge circular cake.

# Edward wants to find out the maximum number of pieces he can get by making exactly N straight vertical cuts on the cake.

# Your task is to write a function that returns the maximum number of pieces that can be obtained by making N number of cuts.

# Note: Since the answer can be quite large, return the answer modulo 1000000007.

# Input Specification

# An integer N denoting the number of cuts.

# Output Specification

# Return the maximum number of pieces that can be obtained by making N cuts on the cake.

# Examples

# Input:

# 1

# Output:

# 2

# Input:

# 5

# Output:

# 16

#code

n=int(input())
ans=1+n*(n+1)//2
print(ans%1000000007)