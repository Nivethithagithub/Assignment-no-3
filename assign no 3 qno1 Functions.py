 # Write a Python function to sum all the numbers in a list.
def sum(num):
    total=0
    for i in num:
        total+=i
    return total
print(sum((8,2,3,0,7)))
