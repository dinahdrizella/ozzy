# This script demonstrates various Python constructs.
# It uses functions, loops, conditional statements,
# dictionaries, tuples, strings, integers, and more.
def get_user_info():
    """Capture user info including name, age, and favorite items."""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    fav_colors = ("Red", "Blue", "Green")
    print("Favorite colors:", fav_colors)
    
    fav_items = input("Enter your favorite items, separated by commas: ").split(",")

    return name, age, fav_items  # Return values


def display_user_info(name, age, fav_items):
    """Display user information."""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Your Favorite items are: {fav_items}")  # Fixed string formatting

# Get user info and display it
name, age, fav_items = get_user_info()
display_user_info(name, age, fav_items)
# Function to get user details
def get_user_data():
    name = input("Enter your name: ")  # String input
    age = int(input("Enter your age: "))  # Integer input
    return name, age

# Function to process user data
def process_data(name, age):
    user_info = {"Name": name, "Age": age}  # Dictionary
    user_info["Status"] = "Adult" if age >= 18 else "Minor"  # Conditional statement
    return user_info
# Using a tuple to store available roles
roles = ("Admin", "User", "Guest")

# Loop through roles
for role in roles:
    print(f"Role available: {role}")  # String formatting

# Get and process user data
name, age = get_user_data()
user_details = process_data(name, age)

# Display results
for key, value in user_details.items():  # Loop through dictionary
    print(f"{key}: {value}")



