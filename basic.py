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


#########################exercise 5 ??#####################

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
    
print(exercise8({"orange","apple","tea"},{"things","thing2"}))

