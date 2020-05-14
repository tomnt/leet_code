"""
The shortest possible length of the compressed representation of a string
http://prochal.com/2020/05/the-shortest-possible-length-of-the-compressed-representation-of-a-string/

https://app.codility.com/c/run/DA5DTY-KEN/
Test 1

Test 2: def solution(A):
Test 3: def solution(A):
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S: str, K: int) -> int:
    """
    :param str S:
    :param int K:
    :return int:
    """
    # write your code in Python 3.6
    # print(S, K)
    # if len(S) < K:
    #    raise Exception('len(S=' + str(len(S)) + ') should be longer than K=' + str(K))
    list_length = []
    for i in range(0, len(S) - K + 1):
        trimmed = S[0:i] + S[i + K:len(S)]
        compressed = get_compressed(trimmed)
        list_length.append(len(compressed))
    return min(list_length)


def get_compressed(target: str) -> str:
    """
    Compress given string.
    :param str target: Target string to compress.
    :return str: Compressed string.
    """
    c_tmp = None
    count = 1
    position = 0
    dict_char = {}
    for c in list(target):
        if c is c_tmp:
            count += 1
        else:
            if c_tmp is not None:
                dict_char[c_tmp + str(position)] = count
            c_tmp = c
            count = 1
            position += 1
    if c_tmp is not None:
        dict_char[c_tmp + str(position)] = count
    compressed = ''
    for k in dict_char:
        if dict_char[k] == 1:
            compressed += k[0]
        else:
            compressed += str(dict_char[k]) + k[0]
    return compressed


print("Example 1: Expected: 5, Actual:", solution("ABBBCCDDCCC", 3))
print("Example 2: Expected: 3, Actual:", solution("AAAAAAAAAAABXXAAAAAAAAAA", 3))
print("Example 3: Expected: 6, Actual:", solution("ABCDDDEFG", 2))
