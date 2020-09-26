def selectionsort(A):
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):
            if (A[min] > A[j]):
                min = j
        A[i], A[min] = A[min], A[i]
    return A
def bubblesort(a):
    for i in range(0, len(a)):
        for j in range(0, len(a) - 1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
def insertionsort(A):
    for i in range(1, len(A)):
        value = A[i]
        hole = i
        while (hole > 0 and (A[hole - 1] > A[hole])):
            A[hole], A[hole - 1] = A[hole - 1], A[hole]
            hole = hole - 1
    return A

print(insertionsort(A))