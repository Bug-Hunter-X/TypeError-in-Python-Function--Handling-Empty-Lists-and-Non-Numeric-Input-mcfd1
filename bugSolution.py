def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        print("Error: List must contain only numbers.")
        return None #or raise exception

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_numbers_2 = [10, 20, 'a', 40, 50]
result = calculate_average(my_numbers_2) #This will print the error message