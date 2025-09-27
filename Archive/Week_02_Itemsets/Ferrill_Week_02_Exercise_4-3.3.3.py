# ------------------------------------------------------------------
#   File: Ferrill_Week_02_Exercise_4-3.3.3.py
#   Name: Teresa Ferrill
#   Date: 6/14/2020
# Course: DSC550-T302 Data Mining
#   Desc: Compute minhash signature for columns within a matrix
#  Usage: MinHash is a technique for quickly estimating how similar two sets are
#    Ref: https://www.bogotobogo.com/Algorithms/minHash_Jaccard_Similarity_Locality_sensitive_hashing_LSH.php
#         https://www.youtube.com/watch?v=96WOGPUgMfw
# ------------------------------------------------------------------

# import statements
# import traceback to support exception handling
import traceback
# import pandas to support dataframe processing
import pandas as pd
# import sys to support high volume/value processing
import sys

# initialize variables
# variable for element list
elements = [0,1,2,3,4,5]
# variables for each set in matrix
s1 = (0,0,1,0,0,1)
s2 = (1,1,0,0,0,0)
s3 = (0,0,0,1,1,0)
s4 = (1,0,1,0,1,0)
# variable for dictionary of sets
set_dict = {'S1': s1, 'S2': s2, 'S3': s3, 'S4': s4}
# variable for DataFrame of set dictionary
set_df = pd.DataFrame(data=set_dict)
# variable for dictionary of hash functions
hf = {'h1', 'h2', 'h3'}

# return first hash formula as a function
def h1(x):
    return ((2 * x) + 1) % 6
    
# return second hash formula as a function
def h2(x):
    return ((3 * x) + 2) % 6
    
# return third hash formula as a function
def h3(x):
    return ((5 * x) + 2) % 6

# compile hash of element list using first hash function
def hash_1(ele_list):
    # list variable to capture hash results
    hash_list = []
    # compute hash and add to hash list
    for i in ele_list:  
        hash_list.append(((2 * i) + 1) % 6)
    return hash_list

# compile hash of element list using second hash function
def hash_2(ele_list):
    # list variable to capture hash results
    hash_list = []
    # compute hash and add to hash list
    for i in ele_list:      
        hash_list.append(((3 * i) + 2) % 6)
    return hash_list    

# compile hash of element list using third hash function
def hash_3(ele_list):
    # list variable to capture hash results
    hash_list = []
    # compute hash and add to hash list
    for i in ele_list:    
        hash_list.append(((5 * i) + 2) % 6)
    return hash_list
    
# function to create matrix of elements, sets, and hash lists
def create_full_matrix(hash_list_1, hash_list_2, hash_list_3):
    # dataframe to hold full matrix, with column headers
    matrix = pd.DataFrame(columns=['element', 's1', 's2', 's3', 's4', 'h1', 'h2', 'h3'])
    # loop through elements, construct full matrix
    for i in range(0, len(elements)):
        # fill rows in dataframe
        matrix.loc[i] = [elements[i], s1[i], s2[i], s3[i], s4[i], hash_list_1[i], hash_list_2[i], hash_list_3[i]]
    # list full matrix
    print('\nMatrix of Elements, Sets, Hash of Elements:\n' + str(matrix))
    return matrix
    
# function to determine true permutation of the elements list
def compare_hash_element_list(hash_list_name, hash_list):
    # sort the lists
    hash_list.sort()
    elements.sort()
    # compare elements to determine and report on permutation
    if hash_list == elements:
        print(hash_list_name + ' is a true permutation of elements list')
    else:
        print(hash_list_name + ' is not a true permutation of elements list')

# function to compute Jaccard Similarity of two lists  
def compute_js(list1, list1_name, list2, list2_name):
    # variable for intersection
    match = 0
    # set total (union of jaccard similarity) 
    # check to see if the lists are estimated or true
    if(list1_name.find('Sig') != -1):
        # length of minhash signagures
        total = len(hf)        
    else:
        # length of sets
        total = len(set_dict)
    # loop through the list and set match (intersection)
    for i in range(0, len(list1)):
        # intersection for minhash signatures
        # count if the two elemeents match, otherwise do nothing
        if(list1_name.find('Sig') != -1):
            if(list1[i] == list2[i]):
                match += 1
            else:
                pass
        else:
            # intersection for boolean set lists, do not count if both columns equal zero
            if(list1[i] == 0 & list2[i] == 0):        
                pass
            # count the intersection only if the two list elements match
            else:
                if(list1[i] == list2[i]):
                    match += 1
                else:
                    pass
    # return string list of jaccard similarities values            
    return (list1_name + ' and ' + list2_name + ': ' + str(match) + ' / ' + str(total) + ' or ' + str(round(match/total, 3)))    

# function to reverse columns and rows within the sets, filling a single ilst
def create_set_data():
    # variable to hold matrix
    matrix = []
    # loop through the sets and create matrix of sets, placing column values in rows
    for i in range(0, len(s1)):
        matrix.append([s1[i], s2[i], s3[i], s4[i]])
    print('\nRow Set Data: ' + str(matrix))
    return matrix

#function to create signature matrix
def minhash(data):
    ''' pesudo-code for minhash    
    for each row r do begin
        for each hash function hi do
            compute hi(r)   (do this only once...)
        for each column c
            if c has 1 in row r
                for each hash function hi do
                    if h1(r) is smaller than M(i,c) then 
                        M(i,c) := hi(r)  (replace)
    '''
    # establish variables for columns and DataFrame
    columns = data.columns
    new_data = pd.DataFrame({})
    # fill DataFrame with computed has function values
    new_data['h1'] = h1(data.index)
    new_data['h2'] = h2(data.index)
    new_data['h3'] = h3(data.index)
    # set index from DataFrame columns
    index = new_data.columns
    # set up DataFrame for minhash
    sig_data = pd.DataFrame(index=index, columns=columns)
    # fill the NaN elements with a value
    sig_data = sig_data.fillna(10000)
    # loop through each row
    for r in data.index:
        # loop through each column
        for c in data.columns:
            # if the row, column value is zero, do nothing
            if data.at[r,c] == 0:
                continue
            # loop through hash functions can set values based on hash values
            for h in ['h1','h2','h3']:
                # if the hash function value is greater than existing value, update value
                if sig_data.at[h,c] > new_data.at[r,h]:
                    sig_data.at[h,c] = new_data.at[r,h]
    # return list DataFrame as a list
    return sig_data.values.tolist()

# main function to obtain list of first 10 3-shingles in the sentence
def main():
    # try block for execution
    try:
        # list sets
        print('\nColumn Set 1: ' + str(s1))
        print('Column Set 2: ' + str(s2))
        print('Column Set 3: ' + str(s3))
        print('Column Set 4: ' + str(s4))
        
        # obtain and hash lists of the elements based on hash functions
        hash_list_1 = hash_1(elements)
        hash_list_2 = hash_2(elements)
        hash_list_3 = hash_3(elements)
        
        # list hash lists
        print('\nHash List 1: ' + str(hash_list_1))
        print('Hash List 2: ' + str(hash_list_2))
        print('Hash List 3: ' + str(hash_list_3))
        
        # generate full matrix of elements, sets, and hash of elements
        create_full_matrix(hash_list_1, hash_list_2, hash_list_3)
        
        # generate minhash signature
        # question (a)       
        print('\n(a) Compute the minhash signature for each column using three hash functions.')     
        print('\nHash Function 1: ((2 * x) + 1) % 6')
        print('Hash Function 2: ((3 * x) + 2) % 6')
        print('Hash Function 3: ((5 * x) + 2) % 6')
        
        # set minhash signature
        minhash_sig = minhash(set_df)
        # print each row of minhash signature
        print('\nFinal Minhash Signature: ')
        for i in range(len(minhash_sig)):
            print('h' + str(i+1) + ': ' + str(minhash_sig[i]))
        
        # determine which hash function is true permutation
        # question (b)
        print('\n(b) Which of these hash functions are true permutations?')
        compare_hash_element_list('\nHash 1', hash_list_1)
        compare_hash_element_list('Hash 2', hash_list_2)
        compare_hash_element_list('Hash 3', hash_list_3)
        
        #compare estimated Jaccard similarities to true Jaccard similarities
        # question (c)
        print('\n(c) How close are the estimated Jaccard Similarities to the true Jaccard Similarities?')
        # similarities of columns 1 & 2, 1 & 3, 1 & 4, 2 & 3, 2 & 4, 3 & 4
           
        # similarities of signatures 
        # establish columns of signatures
        m1 = [minhash_sig[0][0], minhash_sig[1][0], minhash_sig[2][0]]
        m2 = [minhash_sig[0][1], minhash_sig[1][1], minhash_sig[2][1]]
        m3 = [minhash_sig[0][2], minhash_sig[1][2], minhash_sig[2][2]]
        m4 = [minhash_sig[0][3], minhash_sig[1][3], minhash_sig[2][3]]
        
        print('\nEstimated Jaccard Similarities computed using MinHash\n(sig/sig = Numbers of common minhash signatures/total numbers of minhash signatures):')
        # similarities of signatures 1 & 2, 1 & 3, 1 & 4, 2 & 3, 2 & 4, 3 & 4
        print(compute_js(m1, 'Sig 1', m2, 'Sig 2'))
        print(compute_js(m1, 'Sig 1', m3, 'Sig 3'))
        print(compute_js(m1, 'Sig 1', m4, 'Sig 4'))
        print(compute_js(m2, 'Sig 2', m3, 'Sig 3'))
        print(compute_js(m2, 'Sig 2', m4, 'Sig 4'))
        print(compute_js(m3, 'Sig 3', m4, 'Sig 4'))
        print(compute_js(m3, 'Sig 3', m4, 'Sig 4'))
        
        print('\nTrue Similarities computed using original Sets\n(col/col = Numbers of common columns/total numbers of columns):')        
        # similarities of columns of sets
        print(compute_js(s1, 'Col 1', s2, 'Col 2'))
        print(compute_js(s1, 'Col 1', s3, 'Col 3'))
        print(compute_js(s1, 'Col 1', s4, 'Col 4'))
        print(compute_js(s2, 'Col 2', s3, 'Col 3'))
        print(compute_js(s2, 'Col 2', s4, 'Col 4'))
        print(compute_js(s3, 'Col 3', s4, 'Col 4'))
  
        # summary of comparision of Jaccard Similarities of columns and signatures
        print('\nThe estimated Jaccard similarities are not close to the true ones.')
    
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