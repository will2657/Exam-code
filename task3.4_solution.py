import matplotlib.pyplot as plt
import numpy as np
def plot_and_ask():
    while True:
        # Ask the user if they want to display a graph
        user_response = input("Do you want to display a graph? (yes/no): ").lower()
        if user_response == 'no':
            print("Exiting.")
            break
        elif user_response == 'yes':
            try:
                # Get the min and max values from the user
                min_x = float(input("Enter the minimum value for the X axis: "))
                max_x = float(input("Enter the maximum value for the X axis: "))
                
                # Generate 1000 evenly spaced points between min_x and max_x
                x = np.linspace(min_x, max_x, 1000)
                # Calculate the sine and cosine of x
                y_sin = np.sin(x)
                y_cos = np.cos(x)
                
                # Plot the sine and cosine functions
                plt.figure(figsize=(10, 6))
                plt.plot(x, y_sin, label='Sine', color='blue')
                plt.plot(x, y_cos, label='Cosine', color='red')
                plt.title('Sine and Cosine Functions')
                plt.xlabel('X axis')
                plt.ylabel('Y axis')
                plt.legend()
                plt.grid(True)
                plt.show()
                
            except ValueError:
                print("Please enter valid numerical values for min and max X axis values.")
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")

# To execute the function, you would simply call it like this:
# plot_and_ask()
plot_and_ask()

