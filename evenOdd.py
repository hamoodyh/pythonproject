#even and odd number initializations
even = 0
odd = 0

# empty tally
# empty tally created
tally = []

# number of elements as input
elementcount = int(input("Enter the number of elements in your list : "))

# for loop until the number of element is reached
for number in range(0, elementcount):
    ele = int(input())

    tally.append(ele)  # adds the element to the tally

print("The list you entered is: ", tally)