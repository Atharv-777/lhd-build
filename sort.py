def sortArr(arr):
    numArr = [int(i) for i in arr.split(" ")]
    for i in range(len(numArr)-1):
        for j in range(i+1, len(numArr)):
            if numArr[i] > numArr[j]:
                temp = numArr[i]
                numArr[i] = numArr[j]
                numArr[j] = temp
    return numArr

arr = input("Enter space separated array of numbers : ")
print(sortArr(arr))