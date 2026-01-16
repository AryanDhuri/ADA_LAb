arr = [2,4,3,6]
for i in range(1,len(arr)):
    key = arr[i]
    for j in range (i-1):
        sorted = arr[j]
        if sorted > key:
            arr [j], arr[i] = arr[i] , arr[j]
print(arr)
