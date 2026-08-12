# Problem Statement

# There are n students in a class. Each student has a certain number of marks.

# You want to maintain equality in each section of the class. To do this, you need to remove students who have marks equal to the top two highest distinct marks.

# For example, if the marks are:

# 2 2 3 4 4

# The top two distinct marks are 4 and 3.

# There are two students with 4, so one student needs to be removed.
# There is only one student with 3, so nobody needs to be removed.

# Therefore, the answer is 1.

# Task

# Given the marks of all students, find the minimum number of students that need to be removed so that there is exactly one student with each of the top two highest distinct marks.

# Input
# First line: an integer n, the number of students.
# Second line: n space-separated integers representing the marks of the students.
# Output

# Print the number of students that need to be removed.

# Constraints
# 2 ≤ n ≤ 10⁵
# 1 ≤ marks[i] ≤ 100

# nput
# 5
# 90 80 90 80 70
# Output
# 2
# Another Example

# Input:

# 2
# 78 90

# Output:

# 0
n=int(input())
arr=list(map(int,input().split()))
count=0
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
freq=dict(sorted(freq.items(),reverse=True)) 
item=list(freq.values())
count+=max(0,item[0]-1)
count+=max(0,item[1]-1)

print(count)


