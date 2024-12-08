def generate_and_print_squares():
    # Generate a list of squares for numbers from 1 to 20
    square_list = [x**2 for x in range(1, 21)]
    
    # Print all elements except the first 5
    print("All values except the first 5:", square_list[5:])

generate_and_print_squares()
