# ------------------------------------------------------------------
#   File: Ferrill_Week_02_Exercise_4-3.1.1.py
#   Name: Teresa Ferrill_Week_02_Exercise_4-3
#   Date: 6/14/2020
# Course: DSC550-T302 Data Mining
#   Desc: Compute the Jaccard Similarities of each pair of three sets
#  Usage: Jaccard Similarity of Sets is the ratio of the size of the
#         intersection of sets divided by their union
# ------------------------------------------------------------------

# import statements
import traceback

# initialize variables
# variables for sets, initialized as lists
set_1 = {1,2,3,4}
set_2 = {2,3,5,7}
set_3 = {2,4,6}

# function to compute and print jaccard similarity based on two sets
def report_jaccard_similarity(list1_name, list1, list2_name, list2):
    # compute intersection
    intersection = len(list(set(list1).intersection(list2)))
    # compute union
    union = (len(list1) + len(list2)) - intersection
    # compute jaccard similarity
    js = round(float(intersection) / union,3)
    # print lists and results of computation
    print("\n" + list1_name + ": " + str(list1))
    print(list2_name + ": " + str(list2))
    print("Jaccard Similarity between " + list1_name + " and " + list2_name + ": " + str(intersection) + " / " + str(union) + " or " + str(js))

# main function to compute jaccard similarity between three sets of numbers
def main():
    # try block to compute and report on jaccard similarity using three sets of numbers
    try:
        # call to compute jaccard similarity using combinations of the three sets
        report_jaccard_similarity('Set 1', set_1, 'Set 2', set_2)
        report_jaccard_similarity('Set 1', set_1, 'Set 3', set_3)
        report_jaccard_similarity('Set 2', set_2, 'Set 3', set_3)
    # exception block to catch any exceptions during execution
    except Exception as exception:
        print('exception')
        # print the traceback of the exception
        traceback.print_exc()
        # list name of exception and any arguments
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));    

if __name__ == '__main__':
    main()