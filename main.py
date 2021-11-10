# For graphic
import matplotlib.pyplot as plt

# Max numbers we are willing to go to
max_int = 9999
# The number we want to start with
min_int = 1

# X and Y co-ords for graph
xCords = []
yCords = []


# Function to calculate the steps
def calculate(n):
    # Number of times we loop
    num = 0
    # The number we are working with
    temp = n
    # While we don't reach the 4-2-1 loop
    while temp != 1:
        if (temp % 2) == 0:
            # Even number, divide by 2
            temp = temp / 2
        else:
            # Odd number, multiply by 3 and add 1
            temp = temp * 3 + 1
        num += 1  # Increment the number of loops

    # Add the values to the lists
    xCords.append(n)
    yCords.append(num)


# For each of the values in 1 - 9999
for x in range(min_int, max_int):
    # Calculate how many times it needs to be calculated
    calculate(x)

# Display it into a scatter plot
plt.scatter(xCords, yCords, c="blue")
plt.xlabel("# Being applied to the conjecture")
plt.ylabel("How many #'s to reach loop")
plt.title("Visualising Collatz Conjecture")

# To show the plot
plt.show()
