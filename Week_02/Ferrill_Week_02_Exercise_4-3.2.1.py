# ------------------------------------------------------------------
#   File: Ferrill_Week_02_Exercise_4-3.2.1.py
#   Name: Teresa Ferrill
#   Date: 6/14/2020
# Course: DSC550-T302 Data Mining
#   Desc: Find first ten 3-shingles in first sentence of section 3.2
#  Usage: Shingling of documents identifies lexically similar documents
#         by constructing sets of short strings that appear within it
#    Ref: http://stuartmyles.blogspot.com/2012/07/shingling-in-python.html
# ------------------------------------------------------------------

# import statements
import traceback

# initialize variables
# variable for the sentence, initialized as a string
sentence = 'The most effective way to represent documents as sets, for the purpose of identifying lexically similar documents is to construct from the document the set of short strings that appear within it.'
# variable for substring length
k = 3

# main function to obtain list of first 10 3-shingles in the sentence
def main():
    # try block for execution
    try:
        # print sentence
        print('\n' + sentence)
        # list first 10 3-shingles in the sentence
        print('\nFirst 10 3-shingles in sentence: ' + str([sentence[i:i + k] for i in range(0,10)]))
    # exception block to catch any exceptions during execution
    except Exception as exception:
        print('exception')
        # print the traceback of the exception
        traceback.print_exc()
        # list name of exception and any arguments
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));    

if __name__ == '__main__':
    main()