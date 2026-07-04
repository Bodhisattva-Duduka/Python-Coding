# create new array with common elements from both arrays

def commonElementsArray(arr1, arr2):
    k = 0
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1)):
            if (arr1[i] == arr2[j]):
                k += 1
    arr3 = [0 for p in range(k)]
    l=0
    while l<k:
        for i in range(0, len(arr1)):
            for j in range(0, len(arr1)):
                if (arr1[i] == arr2[j]):
                    arr3[l] = arr1[i]
                    l += 1
    return arr3

arr4 = [1, 2, 3, 4, 5]
arr5 = [3, 4, 5, 6, 2]
print(commonElementsArray(arr4, arr5))