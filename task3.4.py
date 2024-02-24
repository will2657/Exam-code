import numpy as np
import matplotlib.pyplot as plt

def plotsinandcos(min_x,max_x):
    
    
    
    x_values= np.linspace(min_x,max_x,300)
    y_sin = np.sin(x_values)
    y_cos = np.cos(x_values)
    plt.plot(x_values,y_sin, color='red', label='sinx')
    plt.plot(x_values,y_cos,color='blue', label ='cosx')
    plt.title('sin and cos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    
plotsinandcos(0,2*np.pi)
    
    
while True:
    # Ask the user if they want to display a graph
    user_input = input("Do you want to display a graph? (yes/no): ").strip().lower()

    # Check if the user wants to exit the loop
    if user_input == "no":
        break

    # If the answer is yes, ask for min and max values
    if user_input == "yes":
        try:
            min_x = float(input("Enter the minimum x value: "))
            max_x = float(input("Enter the maximum x value: "))
            plotsinandcos(min_x, max_x)
        except ValueError:
            print("Please enter valid numerical values for min and max.")

    else:
        print("Please enter 'yes' or 'no'.")