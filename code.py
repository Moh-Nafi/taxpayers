"""Created by Mohammad Nafi, HW-6 Problem-1, 6/1/2022.
The app collects and stores taxpayers' data into a dictionary.
Inputs from the user: name (str) || income, in dollars (float)
Outputs to the user: tax, in dollars (float) || average_tax, in dollars (float) || taxpayers (dict), key: name (str), value: income (float) & tax (float)
"""

# Global

taxpayers = {} # key: name (str), value: income (float) & tax (float)

# Functions

def compute_tax(inc):
    """Computes tax.
    Parameter: 
        income, in dollars (float)
    Return:
        tax amount, in dollars (float)
    """

    tx_rt = 0.2 if inc > 100000.00 else 0.1

    tx = inc * tx_rt


    return tx


def print_taxpayer(name):
    """ Prints information about a taxpayer from the dictionary.
    Parameter:
        name (str)
    Return:
         Taxpayer's name (str), income (float) and tax (float)
    """

    global taxpayers

    if not taxpayers:
        print('No data exists.')
        return
    
    for name in taxpayers: 
        value = taxpayers[name]
        inc = value[0]
        tx = value[1]

    print(f'\nName:{name:s}    Income: ${inc:.2f}    Tax: ${tx:.2f}\n')


def add_lines():
    """Adds dashed lines.
    Parameter:
        No parameters
    Return:
        Dashed lines"""

    return '-' * 40


def display_result():
    """Displays name, and respective income & tax of the taxpayers in columns, within a specified space.
    Parameters:
        No parameters
    Return:
        Three columns in parallel, each row showing Name, matching Income & Tax
    """
    global taxpayers

    print(add_lines())
    print(f'|{"Name":^12s}|{"Income ($)":^14s}|{"Tax ($)":^10s}|')
    print(add_lines())

    if not taxpayers:
        print('No data exists.')
        return 

    for name in taxpayers: 
        value = taxpayers[name]
        inc = value[0]
        tx = value[1]
        print(f'|{name:^12s}|{inc:^14.2f}|{tx:^10.2f}|')
    print(f'{add_lines()}\n')


def compute_avg_tax():
    """Computes the average tax of taxpayers.
    Parameter: 
        No parameter
    Return:
        Average tax, in dollars (float)
    
    """
    global taxpayers

    if not taxpayers:
        print("No data exists.")
        return 
    
    total_tx = 0.0
    count = 0

    for value in taxpayers.values():
        tx = value[1]
        total_tx += tx
        count += 1

    if count> 0:
        avg = total_tx/count
    else:
        avg = None
    

    return avg


def submit():
    global taxpayers

    # Inputs
    name = input('Enter name: ')
    income = float(input('Enter income: '))

    # Computing tax
    tax = compute_tax(income)

    # Inserting name as key, income and tax as values in the dictionary 'taxpayers'
    taxpayers[name] = [income, tax]

    print_taxpayer(name)


def summary():
    global taxpayers

    if not taxpayers:
        print("No data exists.")
        return 

    average_tax = compute_avg_tax()
    
    if average_tax is not None:
        print(f'Average Tax: ${average_tax:.2f}')
    else:
        print("No data exists to compute average tax.")


def reset():
    global taxpayers

    if not taxpayers:
        print('No data exists')
        return

    taxpayers.clear


def display():
    global taxpayers

    if not taxpayers:
        print('No data exists.')
        return

    if taxpayers:
        print(display_result())
    else:
        print('No data to print.')

   

def search():
    global taxpayers

    if not taxpayers:
        print('No data exists.')
        return
    
    name = input('Enter name to search for >> ')
    if name in taxpayers:
        print_taxpayer(name)
    else: 
        print('No such name is present.')


# Main

quit = False
while not quit:
   print('1.Submit 2.Summary 3.Reset 4.Display 5.Search 6.Quit the app')
   choice = int(input('Enter 1, 2, 3, 4, 5 or 6 >'))
   if choice == 1:
       submit()
   elif choice == 2:
       summary()
   elif choice == 3:
       reset()
   elif choice == 4:
       display()
   elif choice == 5:
       search()
   elif choice == 6:
       quit = True
   else:
       print('Invalid choice! Choose 1, 2, 3, 4, 5 or 6.')
 
print('Thank you for using the App.\nHope you liked it!')
