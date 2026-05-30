n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

for i in range(n):
    if arr[i] == key:
        print("Element found at position", i + 1)
        break
else:
    print("Element not found")
