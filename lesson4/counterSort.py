a = [1, 45, 33, 200, 22, 100, 50, 179, 129, 46, 55, 128, 200, 199, 200]
arr = [0 for i in range(0, 201)]
for i in range(len(a)):
    num = a[i]
    arr[num] += 1
new_arr = []
for i in range(0, 201):
    if arr[i]:
        for j in range(arr[i]):
            new_arr.append(i)
print(new_arr)
