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
def jaccard_similarity(x,y):
    # determine intersection
    i = intersection_cardinality(x,y)
    # determin union
    u = union_cardinality(x,y)
    # compute and return similiarty
    return round(float(i) / u,3)

# function to compute intersection of two lists
def intersection_cardinality(x,y):
    set_x = set(x)
    set_y = set(y)
    #return len(list(set(x).intersection(y)))
    return len(set_x.intersection(set_y))

# function to compute union of two lists
def union_cardinality(x,y):
    #return (len(x) + len(y)) - intersection_cardinality(x,y)
    set_x = set(x)
    set_y = set(y)
    return (len(set_x.union(set_y)))
 
# function to reverse columns and rows within the sets, filling a single ilst
def create_set_data():
    # variable to hold matrix
    matrix = []
    # loop through the sets and create matrix of sets, placing column values in rows
    for i in range(0, len(s1)):
        matrix.append([s1[i], s2[i], s3[i], s4[i]])
    print('\nRow Set Data: ' + str(matrix))
    return matrix
    
# function to create signature matrix
def minhash(data, hashfuncs):
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
    # initialize rows, columns, and signature rows variables
    rows = len(data)
    cols = len(data[0])
    sigrows = len(hashfuncs)
    # initialize signature matrix with maxsize
    sigmatrix = []
    # loop through rows to fill the signature matrix
    for i in range(sigrows):
        sigmatrix.append([sys.maxsize] * cols)
    # loop through rows using hash functions to fill columns
    for r in range(rows):
        hashvalue = list(map(lambda x: x(r), hashfuncs))
        # if data != 0 and signature > hash value, replace signature with hash value
        for c in range(cols):
            if data[r][c] == 0:
                continue
            for i in range(sigrows):
                # if the sigmatrix value is greater than the hashvalue, replace with hashvalue
                if sigmatrix[i][c] > hashvalue[i]:
                    sigmatrix[i][c] = hashvalue[i]
    return sigmatrix    
        

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
        
        print('\nHash List 1: ' + str(hash_list_1))
        print('Hash List 2: ' + str(hash_list_2))
        print('Hash List 3: ' + str(hash_list_3))
        
        # generate full matrix of elements, sets, and hash of elements
        create_full_matrix(hash_list_1, hash_list_2, hash_list_3)
        
        # generate minhash signature
        # question (a)
        print('\n(a) Compute the minhash signature for each column using three hash functions.')
        minhash_sig = minhash(create_set_data(), [h1, h2, h3])
        print('\nFinal Minhash Signature: ' + str(minhash_sig))
        
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
        
        print('\nCol 1 and Col 2: ' + str(intersection_cardinality(s1, s2)) + ' / ' + str(union_cardinality(s1,s2)) + str(' or ' + str(jaccard_similarity(s1, s2))))
        print('Col 1 and Col 3: ' + str(intersection_cardinality(s1, s3)) + ' / ' + str(union_cardinality(s1,s3)) + str(' or ' + str(jaccard_similarity(s1, s3))))
        print('Col 1 and Col 4: ' + str(intersection_cardinality(s1, s4)) + ' / ' + str(union_cardinality(s1,s4)) + str(' or ' + str(jaccard_similarity(s1, s4))))
        print('Col 2 and Col 3: ' + str(intersection_cardinality(s2, s3)) + ' / ' + str(union_cardinality(s2,s3)) + str(' or ' + str(jaccard_similarity(s2, s3))))
        print('Col 2 and Col 4: ' + str(intersection_cardinality(s2, s4)) + ' / ' + str(union_cardinality(s2,s4)) + str(' or ' + str(jaccard_similarity(s2, s4)))) 
        print('Col 3 and Col 4: ' + str(intersection_cardinality(s3, s4)) + ' / ' + str(union_cardinality(s3,s4)) + str(' or ' + str(jaccard_similarity(s3, s4))))
         
        # similarities of signatures 
        # establish columns of signatures
        minhash_1 = [minhash_sig[0][0], minhash_sig[1][0], minhash_sig[2][0]]
        minhash_2 = [minhash_sig[0][1], minhash_sig[1][1], minhash_sig[2][1]]
        minhash_3 = [minhash_sig[0][2], minhash_sig[1][2], minhash_sig[2][2]]
        minhash_4 = [minhash_sig[0][3], minhash_sig[1][3], minhash_sig[2][3]]
        
        # similarities of signatures 1 & 2, 1 & 3, 1 & 4, 2 & 3, 2 & 4, 3 & 4
        print('\nSig 1 and Sig 2: ' + str(intersection_cardinality(minhash_1, minhash_2)) + ' / ' + str(union_cardinality(minhash_1, minhash_2)) + str(' or ' + str(jaccard_similarity(minhash_1, minhash_2))))
        print('Sig 1 and Sig 3: ' + str(intersection_cardinality(minhash_1, minhash_3)) + ' / ' + str(union_cardinality(minhash_1, minhash_3)) + str(' or ' + str(jaccard_similarity(minhash_1, minhash_3))))
        print('Sig 1 and Sig 4: ' + str(intersection_cardinality(minhash_1, minhash_4)) + ' / ' + str(union_cardinality(minhash_1, minhash_4)) + str(' or ' + str(jaccard_similarity(minhash_1, minhash_4))))
        print('Sig 2 and Sig 3: ' + str(intersection_cardinality(minhash_2, minhash_3)) + ' / ' + str(union_cardinality(minhash_2, minhash_3)) + str(' or ' + str(jaccard_similarity(minhash_2, minhash_3))))
        print('Sig 2 and Sig 4: ' + str(intersection_cardinality(minhash_2, minhash_4)) + ' / ' + str(union_cardinality(minhash_2, minhash_4)) + str(' or ' + str(jaccard_similarity(minhash_2, minhash_4))))
        print('Sig 3 and Sig 4: ' + str(intersection_cardinality(minhash_3, minhash_4)) + ' / ' + str(union_cardinality(minhash_3, minhash_4)) + str(' or ' + str(jaccard_similarity(minhash_3, minhash_4))))
        
        # summary of comparision of Jaccard Similarities of columns and signatures
        print('\nThe estimated Jaccard similarities are not close to the true ones.')
    
    # exception block to catch any exceptions during execution
    except Exception as exception:
        print('exception')
        # print the traceback of the exception
        traceback.print_exc()
        # list name of exception and any arguments
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));    

if __name__ == '__main__':
    main()