
rows = int(input("Enter number of rows in the comment box: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")