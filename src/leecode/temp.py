def longestOnes(A, K):
    i = 0
    for j in range(len(A)):
        if A[j] == 0:
            K -= 1
        if K < 0:
            if A[i] == 0:
                K += 1
            i += 1
        print("i:{},j:{},k:{}".format(i, j, K))
    return j - i + 1




A1 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K1 = 3

print(longestOnes(A1, K1))
