# ------------------------------------------------------------------
#   File: Ferrill_Week_02_Exercise_2.py
#   Name: Teresa Ferrill
#   Date: 6/14/2020
# Course: DSC550-T302 Data Mining
#   Desc: Non-Derivable Itemset - compute whether an itemset is derivable or not
#  Usage: A itemset is non-derivable if its support cannot be deduced 
#         from the suports of its subsets
#    Ref: Jure Leskovec, A. R. (2020). Minning of Massive Datasets. Cambridge: Cambridge University Press. 
# ------------------------------------------------------------------
# import statements
# support DataFrame
import pandas as pd
# support use of combinations
from itertools import combinations

# function to get list of combinations of itemset of length num_combinations
def get_combinations(itemset, num_combinations):
    # build list of combinations 
    combination_list = []
    # loop through itemset and find combinations based on size of desired combination
    for combination in combinations(itemset, num_combinations):
        combination_list.append(combination)
    return combination_list

# function to calculate the bound value given the subset, itemset, 
# frequent itemset dict, and length of subset
def calc_value(st, itemset, dictionary, n):
    # build subsets based on combinations
    value = 0.0
    for num in range(n-1, 0, -1):
        # build list of combinations
        subsets = get_combinations(itemset, num)
        # loop through combinations list
        for combination in subsets:
            # get all items in combination based on items in itemset
            ck = all(item in combination for item in st)
            # increment value to support validation, identification of upper and lower bounds
            if ck or st == ():
                i = int(dictionary[combination]) * pow(-1.0, (n+1) - num)
                value += i
    # if combination set is empty, update dictionary values
    if st == ():
        empty = 0
        for dict_value in dictionary.values():
            empty += int(dict_value)
        value += empty * pow(-1.0, (n+1))
        
    # return bound value
    return value

# function to obtain upper and lower bounds given the itemet and frequent itemset dictionary
def get_bounds(itemset, dictionary):
    # set variables to obtain and determin upper and lower bound per itemset
    upper_bounds = []
    lower_bounds = []
    lower_bound = 0
    upper_bound = 0
    n = len(itemset)
    # loop through itemset and break down the combinations into subsets
    for index in range(len(itemset)):
        subsets = get_combinations(itemset, index)
        # determin if the subset length is odd or even 
        boolean_Odd = (n - len(subsets[0]))%2
        # loop through each combination in the subset
        for combination in subsets:
            # if the length is odd, update upper bound list
            if boolean_Odd:
                upper_bounds.append(calc_value(combination, itemset, dictionary, n))
            # if length is even, update lower bound list
            else:
                lower_bounds.append(calc_value(combination, itemset, dictionary, n))
    # if the maximum number in the lower bound list is less than zero, set lower bound to zero
    if max(lower_bounds) < 0:
        lower_bound = 0
    # if maxium number is 0 or greater, set lower bound to that number
    else:
        lower_bound = max(lower_bounds)
    
    # set upper bound to the minumum number within the upper bound list
    upper_bound = min(upper_bounds)
    
    # if lower and upper bound number are equal, the set is derivable, otherwise it is non-derivable
    if lower_bound == upper_bound:
        d = 'derivable'
    else:
        d = 'non-derivable'
    
    # report findings with subset, the lower and upper bound value, and whether or not is it derivable
    return '{}: [{}, {}] {}'.format(itemset, lower_bound, upper_bound, d)
    
# main function for exercise three
def main():
    # try block for execution
    try:
        # prepare data
        itemset_df = pd.read_csv('itemsets.txt', header = None)
        ndi_df = pd.read_csv('ndi.txt', header = None)
        
        # process itemset dataframe into dictionary
        itemset_dict = {}
        for i, itemset_support in enumerate(itemset_df[0]):
            set_support_list = [] # list contains itemset and support where support is last element
            for val in itemset_support.split(' '):
                if val == '-':  # skip the hyphen
                    continue
                else:
                    set_support_list.append(val)
            # itemset becomes tuple key and is assigned to support
            itemset_dict[tuple(set_support_list[:-1])] = set_support_list[-1]
        # process ndi-df into dictionary
        ndi_dict = {}
        # dictionary is index as key with itemset as value
        for i, itemset in enumerate(ndi_df[0]):
            ndi_dict[i] = itemset.split(' ')
        # main loop to print bounds and derivablility
        for itemset in ndi_dict.values():
            print(get_bounds(itemset, itemset_dict))
    # exception block to catch any exceptions during execution
    except Exception as exception:
        print('exception')
        # print the traceback of the exception
        traceback.print_exc()
        # list name of exception and any arguments
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));   

# call to main function   
if __name__ == '__main__':
    main()