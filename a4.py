import csv

def main():
    """
    Program to upload data from a CSV file, display the data, rename and sort variables, and calculate summary statistics.
    """
    display_menu()
    menu_choice = get_valid_input(6)
    data = False
    while menu_choice != 6:
        if menu_choice == 1:
            data = load_data()
            display_menu()
            menu_choice = get_valid_input(6)
        elif menu_choice == 2:
            if not data:
                display_data_error()
                display_menu()
                menu_choice = get_valid_input(6)
            else:
                display_data(data)
                display_menu()
                menu_choice = get_valid_input(6)
        elif menu_choice == 3:
            if not data:
                display_data_error()
                display_menu()
                menu_choice = get_valid_input(6)
            else:
                rename_set(data)
                display_menu()
                menu_choice = get_valid_input(6)
        elif menu_choice == 4:
            if not data:
                display_data_error()
                display_menu()
                menu_choice = get_valid_input(6)
            else:
                sort_set(data)
                display_menu()
                menu_choice = get_valid_input(6)
        elif menu_choice == 5:
            if not data:
                display_data_error()
                display_menu()
                menu_choice = get_valid_input(6)
            else:
                analyse_set(data)
                display_menu()
                menu_choice = get_valid_input(6)
        else:
            exit()

display_data_error = lambda: print("Upload a dataset first.")

def display_menu():
    """
    Prints the display menu to the screen.
    """
    print()
    print('Welcome to the Smart Statistician!')
    print('Please choose from the following options: ')
    print('\t1 - Load data from a file')
    print('\t2 - Display the data to the screen')
    print('\t3 - Rename a set')
    print('\t4 - Sort a set')
    print('\t5 - Analyse a set')
    print('\t6 - Quit')
    print()
    

def get_valid_input(n):
    """
    Gets input from the user and validates it.
    """
    valid_choice = False
    while not valid_choice:
        try:
            menu_choice = int(input("Choose an option: "))
            if menu_choice not in range(1, n + 1):
                raise Exception
            valid_choice = True
            return menu_choice
        except:
            print(f'Enter a number from 1 to {n} ')

    
def load_data():
    """
    Loads a dataset from a CSV file, removes empty strings and converts to float format.
    """
    data = {}
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            raw_data = csv.reader(file)
            for row in raw_data:
                row = [i for i in row if i] 
                name = row[0] 
                values = [float(i) for i in row[1:]] 
                data[name] = values 
            return data
    except:
        print('File does not exist.')


def display_data(data):
    """
    Displays a dictionary's keys and items.
    """
    for name, values in data.items():
        print(name)
        values = format_array(values)
        print(values)
        print('----------')


def format_array(array):
    """
    Formats numbers for printing so that decimals will only be displayed if necessary.
    """
    num_array = [int(i) if i.is_integer() else float(i) for i in array]
    str_array = ', '.join(str(i) for i in num_array)
    return str_array


def rename_set(data):
    """
    Renames a set. 
    """
    valid_input = False
    while not valid_input:
        print('Choose a set to rename: ')
        key_index = create_key_index(data)
        display_names(key_index)
        menu_choice = get_valid_input(len(data.keys()))
        valid_input = True
        menu_choice_index = menu_choice - 1
        old_name = key_index[menu_choice_index]
        new_name = get_new_name(data)
        data[new_name] = data.pop(old_name)
        print(f'{old_name} has been renamed to {new_name}')
        

def create_key_index(data):
    """
    Creates a dictionary with the index and key names from the data dictionary. 
    This is able to link the data dictionary key to a selection entered by the user.
    """
    key_index = {}
    for i, name in enumerate(data):
        key_index[i] = name
    return key_index


def display_names(key_index):
    """
    Displays each key and name from the key index dictionary.
    """
    for i, name in key_index.items():
        print(f'\t{i + 1} - {name}')
    

def get_new_name(data):
    """
    Gets a new variable name from the user.
    """
    valid_name = False
    while not valid_name:
        new_name = input('Enter the new name: ')
        if new_name == '' or new_name in data.keys():
            print('Enter a valid name.')
        else:
            valid_name = True
            return new_name


def sort_set(data):
    """
    Asks the user which set they would like to sort and sorts it.
    """
    valid_input = False
    while not valid_input:
        print('Choose a set to sort: ')
        key_index = create_key_index(data)
        display_names(key_index)
        menu_choice = get_valid_input(len(data.keys()))
        valid_input = True
        menu_choice_index = menu_choice - 1
        set_name = key_index[menu_choice_index]
        data[set_name].sort()
        

def analyse_set(data):
    """
    Calculates summary statistics for a set.
    """
    valid_input = False
    while not valid_input:
        print('Choose a set to analyse: ')
        key_index = create_key_index(data)
        display_names(key_index)
        menu_choice = get_valid_input(len(data.keys()))
        valid_input = True
        menu_choice_index = menu_choice - 1
        set_name = key_index[menu_choice_index]
        array = data[set_name]
        n = len(array)
        smallest = format_array([min(array)])
        largest = format_array([max(array)])
        median = format_array([calculate_median(array)])
        mode = calculate_mode(array)
        print(set_name)
        print('----------')
        print(f'Number of values (n): {n}')
        print(f'\tMin: {smallest}')
        print(f'\tMax: {largest}')
        print(f'\tMedian: {median}')
        print(f'\tMode: {mode}')
            

def calculate_median(array):
    """
    Calculates the median of an array.
    """
    n = len(array)
    sorted_array = sorted(array)
    half = n // 2
    if not n % 2:
        median = (sorted_array[half - 1] + sorted_array[half]) / 2.0
    
    else:
        median = sorted_array[half]
    return median
        

def calculate_mode(array):
    """
    Calculates the mode of an array. If all values are unique, returns that all values are unique.
    Otherwise, if there is a single or multiple modes, the function returns the values as a string. 
    """
    counts = dict((i, array.count(i)) for i in set(array))
    if len(set(counts.values())) == 1:
        mode = 'All values in the set are unique.'
    
    else:
        mode = format_array([keys for keys, values in counts.items() if values == max(counts.values())])
    return mode


main()