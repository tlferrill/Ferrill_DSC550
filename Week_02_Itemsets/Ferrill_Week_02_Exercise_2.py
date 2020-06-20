# ------------------------------------------------------------------
#   File: Ferrill_Week_02_Exercise_2.py
#   Name: Teresa Ferrill
#   Date: 6/14/2020
# Course: DSC550-T302 Data Mining
#   Desc: Non-Derivable Itemset - compute whether an itemset is derivable or not
#  Usage: A itemset is non-derivable if its support cannot be deduced 
#         from the suports of its subsets
#    Ref: 
# ------------------------------------------------------------------
'''

Non Derivable Itemsest

Your goal here is to write a program to compute whether an itemset is derivable or not. The program should take as input the following two files:

    FILE1: A list of itemsets with their support values (one per line). See the file: itemsets.txt (the format is "itemset - support"; one per line)
    FILE2: A list of itemsets (one per line), whose support bounds have to be derived. See the file: ndi.txt

Your program should output for each itemset in FILE2 the following info:

itemset: [l,u] derivable/non-derivable

where l and u are the lower and upper-bounds on the support.



for x in itemsets:
    all_ys = get_powersets(x)
    for y in all_ys:
        if len(x-y) is even # this is the set difference
            compute bound and add to lower bound
        else
            compute bound and add to upper bound
            
compute bound(x,y,W,ds):
    # x is my current itemset
    # y is the current subset of my current itemset
    # W is a list of all subsets of x
    # ds this is a dict of itemsets : support built from itemsets.txt
    bound_val = 0
    for w in W:
        if y is a subset of w:
            calculate coefficient as -1 ^ (len(x-2) # this comes from eq 9.8 and 9.9. and is in the screenshot from Sam.
            it is SLIGHTLY different than inclusion/exclusion in eq 9.7
            get sub(w) by xrefing the itemset.txt file
            bound += coef * sup(w)
            
            
x.difference(y)
c-ad is even
c-ac is odd
c-cd is odd

tuple(itemsets) for key and value the support

all_ys will go through all the subsets of CAD and determine if the difference of the current subset and CAD is odd/even
Example 9.7 is actually quite helpful in that regard. 

W = all_ys = get_powersets(x)
then loop ==> 'for w in W:'
always adding/substracting sup(x), because every y is a subset of x

Example 9.7
x = ACD and y = AC, diff in len will be a - Odd
in the loop ==> 'for w in W'
AC is subset of AC and ACD, so
bound = 1xsup(AC) + 1xsup(ACD), which should have been only 1xsup(AC)

------------------

when len(x-w) - means number of elements in x that are not in w?
in calculate bound, wouldn't you have len(x\y) which would be the number of elements in the itemset that are not in the subset?

------------------
'''
import pandas as pd
import numpy as np
import sys
from itertools import combinations
 
#import numpy as np 
#import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules 

def createCombo(_list_, combos):
    comb_list = []    
    for i in combinations(_list_, combos):
        comb_list.append(i)    
    return comb_list
    
def calcItemsSet(supp, _list_, _dict_, n):
    val = 0.0
    for i in range(n-1,0,-1):
        combos= []
        combos = createCombo(_list_,i)
        
        for ii in combos:
            ck = all(item in ii for item in supp)
            if ck or supp == ():
                iii = int(_dict_[ii]) * pow(-1.0, (n+1) -i)
                val += iii                                       
    if supp == ():
        empty = 0
        for i in _dict_.values():
            empty += int(i)
        val += empty * pow(-1.0,(n+1) - 0)
    return val

def getUppLwrBounds(_list_, _dict_):
    upper = []
    lower = []
    n = len(_list_)
    llist = _list_.copy()
    for i in range(len(llist)):
        combos = createCombo(llist,i)
        isOdd = (n - len(combos[0]))%2
        for ii in combos:
            if isOdd:
                upper.append(calcItemsSet(ii, _list_, _dict_, n))                
            else:
                lower.append(calcItemsSet(ii, _list_, _dict_, n))
    if max(lower) == min(upper):
        deriv = 'derivable'
    else:
        deriv = 'non-derivable'
    results = '{}: [{},{}] {}'.format(_list_,max(lower), min(upper), deriv)
    return results

def main():
    df = pd.read_csv('itemsets.txt', header = None)
    ndi = pd.read_csv('ndi.txt', header = None)

    d = {}
    ndi_dict = {}
    
    for t, val in enumerate(df[0]):
        _list_ = []
        for i in val.split(' '):
            if i == ' - ':
                continue
            else:
                _list_.append(i)
        d[tuple(_list_[:-1])] = _list_[-1]
            
    for t, val in enumerate(ndi[0]):
        ndi_dict[t] = val.split(' ')
    
    for i in ndi_dict.values():
        print(getUppLwrBounds(i,d))
    
    empty = 0
    for i in d.values():
        empty += int(i)
    print(empty)

if __name__ == '__main__':
    main()