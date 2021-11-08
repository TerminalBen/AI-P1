import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def prod_or_sum(a:int,b:int)-> int:
    """Exercise 1: Given two integer numbers return their product only if the product is greater than 
        1000, else return their sum.
    """
    m = a*b
    s= a+b
    return m if m > 1000 else s
    


def sum_current_previous(a:int) ->int:
    """Exercise 2: Print the sum of the current number and the previous number

    Args:
        a (int)
    """
    return a+(a-1)

def check_first_last_list(a:list) ->bool:
    """Exercise 3:Check if the first and last number of a list is the same. Write a function to 
    return True if the first and last number of a given list is same. If numbers are 
    different then return False.

    Args:
        a (list): list of integers

    Returns:
        bool: true if same number false if different number
    """
    return True if a[0] == a[-1] else False

def multiply_user_input():
    """Exercise 4:Accept numbers from a user. Write a program to accept two numbers from the user 
    and calculate multiplication.
    """
    return( int(input()) * int(input()))


def exercise5():
    """Display numbers from a list using loop. Write a program to display only those 
        numbers from a list that satisfy the following conditions 
        Instructions Unclear (Condition ???)
    """
    pass

def exercise6(l1:list,l2:list)-> list:
    """Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-
    index element from the list l1 and even index elements from the list l2.

    Args:
        l1 (list)
        l2 (list)
        im assuming same lenght lists because zip() stops when the shortest list ends
    Returns:
        list: [contains elements from odd index of l1 and even index of l2]
    """
    l3 = []
    for a,b in zip(l1,l2):
        if l1.index(a)%2 == 0:
            l3.append(a)
        if l2.index(b)%2 != 0:
            l3.append(b)
    return l3


def exercise7(list:list)->list:
    """Write a program to remove the item present at index 4 and add it to the 2nd 
    position and at the end of the list.
    Assuming we want the same list with substitution of elements at the indexes

    Args:
        list (list):

    Returns:
        list:
    """
    elem = list[4]
    list[2],list[4],list[-1] = elem,None,elem
    return list

def exercise8(set1:set,set2:set)->set:
    if set1.issubset(set2):
        set2.remove(set1)
    if set1. issuperset(set2):
        set2.remove(set1)
    return set1
    
def exercise9():
    """Create a 5X2 integer array from a range between 100 to 200 such that the difference 
    between each element is 10.
    """
    pass

def exercise10():
    """Create two 2-D arrays and Plot them using matplotlib
    """
    T = [[11,12,5,2],[15,6,3,10],[10,8,2,5],[12,15,8,6]]
    plt.plot(T)
    plt.show()

def exercise11():
    """ From the given dataset print the first and last five rows
        Assuming the dataset is company_sales_data.csv
    Returns:
        [type]: [description]
    """
    data =  pd.read_csv('company_sales_data.csv')
    return data.head(),data.tail(5)

def exercise12():
    """Clean the dataset and update the CSV file.
        Instructions unclear
    """
    pass

def exercise13():
    
    data = pd.read_csv('Automobile_data.csv')
    name,max ='',0
    header = ['company','price']
    df1 = pd.DataFrame.from_records(data,columns=header)
    for _ ,row in df1.iterrows():
        if row[1]>max:
            name,max=row[0],row[1]
    return name,max

def exercise14():
    """Print All Toyota Cars details.
    """
    data = pd.read_csv('Automobile_data.csv')
    toyotas = data[data["company"]=='toyota']
    return toyotas

def exercise15():
    """Count total cars per company.
    """
    data = pd.read_csv('Automobile_data.csv')
    dict1 = {}
    for _,row in data.iterrows():
        if row[1] in dict1:
            dict1[row[1]] += 1
        else:
            dict1[row[1]] = 1
    return dict1

def exercise16():
    """Find each company’s Higesht price car."""
    pass


def exercise17():
    """ Find the average mileage of each car making company.
    """
    pass

def exercise18():
    """ Sort all cars by Price column.
    """
    data = pd.read_csv('Automobile_data.csv')
    return data.sort_values(by=['price'])

def exercise19():
    """Create two data frames using the following two Dicts, Merge two data frames, and 
    append the second data frame as a new column to the first data frame.
    INSTRUCTIONS UNCLEAR(which Dicts??)
    """
    pass    

def exercise20():
    """Read Total profit of all months and show it using a line plot 
    """
    data = pd.read_csv('company_sales_data.csv')
    row = data["total_profit"]
    plt.plot(row)
    plt.ylabel('Values')
    plt.xlabel('Month')
    plt.show()

def exercise21():
    """Get total profit of all months and show line plot with the following Style properties
        Instructions unclear which Style properties?
    """
    pass

def exercise22():
    """Read all product sales data and show it  using a multiline plot.
    """
    data = pd.read_csv('company_sales_data.csv')
    months = data['month_number']
    facecream = data['facecream']
    facewash=data['facewash']
    toothpaste=data['toothpaste']
    bathingsoap= data['bathingsoap']
    shampoo=data['shampoo']
    moisturizer=data['moisturizer']
    plt.plot(months,facecream,label ="facecream")
    plt.plot(months,facewash,label ="facewash")
    plt.plot(months,toothpaste,label ="toothpaste")
    plt.plot(months,bathingsoap,label ="bathingsoap")
    plt.plot(months,shampoo,label ="shampoo")
    plt.plot(months,moisturizer,label ="moisturizer")
    plt.legend()
    plt.xlabel("month")
    plt.ylabel("value")
    plt.show()

def exercise23():
    """Read toothpaste sales data of each month and show it using a scatter plot.
    """
    data = pd.read_csv('company_sales_data.csv')
    months = data['month_number']
    toothpaste=data['toothpaste']
    plt.scatter(months,toothpaste)
    plt.show()

def exercise24():
    """Read face cream and facewash product sales data and show it using the bar chart.
    """
    data = pd.read_csv('company_sales_data.csv')
    months = data['month_number']
    facecream = data['facecream']
    facewash=data['facewash']

    x = np.arange(len(months))  
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, facecream, width, label='Facecream')
    rects2 = ax.bar(x + width/2, facewash, width, label='Faewash')

    ax.set_ylabel('Values')
    ax.set_xlabel('Month')
    ax.set_xticks(x)
    ax.set_xticklabels(months)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()
