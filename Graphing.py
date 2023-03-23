# QAP 4 - Graphing
# Evan Davies
# March 21, 2023

# Imports
import matplotlib.pyplot as plt

# Setting up the x and y axis
x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = []

# User input for total sales in each month.
# I created another list for this using the full month names. This is because I thought it would look
# better in the input statement than using the month's abbreviation.
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in months:
    while True:
        try:
            sales = float(input(f"Enter total sales for {month} (no $ sign): "))
        except:
            print("Must be a valid number. Try again.")
        else:
            break
    y_axis.append(sales)

# Setting up the labels and plotting the graph
plt.title("Total Sales in Each Month")
plt.plot(x_axis, y_axis)
plt.xlabel("Months")
plt.ylabel("Total Sales ($)")
plt.grid(True)

# Displaying the graph
plt.show()



'''
The program below is another method I thought of using. It's not exactly what you asked in the QAP
instructions, but I thought it'd be fun to try, and it worked out pretty well. The only difference is that
instead of needing input for every single month, the user can choose to end the program at any month. You
can uncomment it if you'd like to give it a try.
'''

#
# # Imports
# import matplotlib.pyplot as plt
#
# # Setting up the x and y axis
# x_axis = []
# y_axis = []
#
# # User inputs for sales per month. As opposed to the main program, here months from the month list are
# # abbreviated and put into the x-axis list. This way, you don't need to input information for every
# # month if you don't have the information yet.
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# for month in months:
#     while True:
#         try:
#             # If there is no more sales information to input, the user can input 0 and end on the
#             # previous month.
#             sales = float(input(f"Enter total sales for {month} (no $ sign, type 0 to end): "))
#         except:
#             print("Must be a valid number. Try again.")
#         else:
#             break
#     if sales == 0:
#         break
#     abbr = month[0:3]
#     x_axis.append(abbr)
#     y_axis.append(sales)
#
# # Setting up the labels and plotting the graph
# plt.title("Total Sales in Each Month")
# plt.plot(x_axis, y_axis)
# plt.xlabel("Months")
# plt.ylabel("Total Sales ($)")
# plt.grid(True)
#
# # Displaying the graph
# plt.show()