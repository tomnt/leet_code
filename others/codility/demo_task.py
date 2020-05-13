"""
Codility demo task
https://app.codility.com/c/run/demo6HVNF8-QTV/
This is a demo task.

Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution(A):
    if max(A) < 1:
        return 1
    for a in range(min(A), max(A) + 1):
        if not (a in A):
            return a
    if max(A) > 0:
        return max(A) + 1


print('Expected: 5, Actual:', solution([1, 3, 6, 4, 1, 2]))
print('Expected: 4, Actual:', solution([1, 2, 3]))
print('Expected: 1, Actual:', solution([-1, -3]))
"""
##################################################
Compilation successful.

Example test:   [1, 3, 6, 4, 1, 2]
OK

Example test:   [1, 2, 3]
OK

Example test:   [-1, -3]
OK

Your code is syntactically correct and works properly on the example test.
Note that the example tests are not part of your score. On submission at least 8 test cases not shown here will assess your solution.
"""