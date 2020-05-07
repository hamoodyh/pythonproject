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


# for loop that loops through the number tally
for number in tally:

    # use modulus operator to find the remainder of the number when divided by 2
    if number % 2 == 0:    # if the remainder is 0
        even = even + 1 # increment amount of even numbers

    if number % 2 == 1:  # else if the remainder when divided by 2 is 1
        odd = odd + 1   # increment amount of odd numbers

print("The list you entered is: ", tally)

print("Even numbers in the list: ", even)
print("Odd numbers in the list: ", odd)