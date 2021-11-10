# If it is even we divide by 2
# If it is odd we multiply it by 3 and add 1
# Stop if we reach 1

import matplotlib.pyplot as plt

# Max numbers we are willing to go to
max_int = 9999
# The number we want to start with
min_int = 1

# X and Y co-ords for graph
xCords = []
yCords = []


def calculate(n):
    num = 0
    temp = n
    while temp != 1:
        if (temp % 2) == 0:
            # Even number 
            temp = temp / 2
        else:
            # Odd number
            temp = temp * 3 + 1
        num += 1

    xCords.append(n)
    yCords.append(num)


for x in range(min_int, max_int):
    calculate(x)

plt.scatter(xCords, yCords, c="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plot")

# To show the plot
plt.show()
