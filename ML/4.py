import seaborn as sns
import matplotlib.pyplot as plt

# Define the function
def func(x):
    return (x + 3)**2

# Define the derivative
def derivative(x):
    return 2 * (x + 3)

# Store x values
gd = []

# Implement Gradient Descent
def gradient_descent(starting_x, learning_rate, num_iterations):

    x = starting_x
    gd.append(x)

    for i in range(num_iterations):

        grad = derivative(x)

        x = x - learning_rate * grad

        gd.append(x)

        print(f"Iteration {i+1}: x = {x}, f(x) = {func(x)}")

    return x


# Initial values
starting_x = 2
learning_rate = 0.1
num_iterations = 50

# Perform Gradient Descent
min_x = gradient_descent(starting_x, learning_rate, num_iterations)

print("Local minimum occurs at x =", min_x)
print("Minimum function value =", func(min_x))


# Plot the Gradient Descent process
y_values = [func(x) for x in gd]

sns.scatterplot(x=gd, y=y_values)
plt.xlabel("x values")
plt.ylabel("f(x)")
plt.title("Gradient Descent")
plt.show()