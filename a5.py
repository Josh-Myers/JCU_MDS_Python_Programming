import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
    Program to upload a CSV dataset and display statistics and plots from the variables. 
    """
    data = pd.DataFrame()
    display_menu()
    menu_choice = get_valid_input(4)
    while menu_choice != 4:
        if menu_choice == 1:
            data = load_data()
            display_menu()
            menu_choice = get_valid_input(4)
        elif menu_choice == 2:
            if data.empty:
                display_data_error()
                display_menu()
                menu_choice = get_valid_input(4)
            else:
                name, n, ave, sd, se = analyse_data(data)
                display_stats(name, n, ave, sd, se)
                display_menu()
                menu_choice = get_valid_input(4)
        elif menu_choice == 3:
            if data.empty:
                display_data_error()
                display_menu()
                menu_choice = get_valid_input(4)
            else:
                display_plots(data)
                display_menu()
                menu_choice = get_valid_input(4)
        else:
            exit()


def display_menu():
    """
    Prints the display menu to the screen and gets valid user input.
    """
    print()
    print('Welcome to the DataFrame Statistician!')
    print('Please choose from the following options: ')
    print('\t1 - Load from a CSV file')
    print('\t2 - Analyse')
    print('\t3 - Visualise')
    print('\t4 - Quit')
    print()


def get_valid_input(n):
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


display_data_error = lambda: print("Upload a dataset first")


def load_data():
    """
    Loads a dataset from a CSV file, remove empty strings and convert to floats.
    """
    filename = input("Enter the filename: ")
    try:
        data = pd.read_csv(filename)
        return data 
    except:
        print('File does not exist.')


def analyse_data(data):
    """
    Renames a set. 
    """
    valid_input = False
    while not valid_input:
        print('Choose a variable to analyse: ')
        
        display_variables(data)
        menu_choice = get_valid_input(len(data.columns))
        valid_input = True
        menu_choice_index = menu_choice - 1
        var = data.iloc[:, menu_choice_index]
        name = data.columns[menu_choice_index]
        n = len(var)
        ave = round(var.mean(), 2)
        sd = round(var.std(), 2)
        se = round(var.sem(), 2)
        return name, n, ave, sd, se


def display_stats(name, n, ave, sd, se):
    print(name)
    print('----------')
    print(f'Number of values (n): {n}')
    print(f'Mean: {ave}')
    print(f'Standard Deviation: {sd}')
    print(f'Std.Err of Mean: {se}')
    print('----------')
    

def display_variables(data):
    """
    Prints each variable and an index in a dataframe.
    """
    vars = data.columns
    for i, var in zip(range(1,len(vars)+1), vars):
        print(f'\t{i} - {var}')


def display_plots(data):
    plot_type_dict = {1: 'line', 2: 'bar', 3: 'box'}
    subplots_dict = {1: False, 2: True}
    print('Choose a plot type: ')
    print('\t1 - Line')
    print('\t2 - Bar')
    print('\t3 - Box')
    plot_choice = get_valid_input(3)
    print()
    print('Choose a layout: ')
    print('\t1 - All data on a single plot')
    print('\t2 - Subplots for each variable')
    layout_choice = get_valid_input(2)
    data.plot(kind = plot_type_dict[plot_choice], subplots = subplots_dict[layout_choice])
    plt.show()


main()

