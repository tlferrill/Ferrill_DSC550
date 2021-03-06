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

# main function to obtain list of first 10 3-shingles in the sentence
def main():
    # variable for the sentence, initialized as a string
    sentence = 'The most effective way to represent documents as sets, for the purpose of identifying lexically similar documents is to construct from the document the set of short strings that appear within it.'
    
    # variable for substring length
    k = 3
    
    # try block for execution
    try:
        # print sentence
        print('\nSentence:\n' + sentence)
        
        # step through sentence and create list of 10 groups of three letters each
        sentence_list = [sentence[i:i + k] for i in range(0,10)]
        
        # step through list and print each list value         
        print('\nFirst 10 3-shingles in sentence (based on letters):\n')        
        for i in range(0, len(sentence_list)):
            print(str(i+1) + ': [' + sentence_list[i] + ']\n')
        
        # split the sentence into words
        tokens = sentence.split()
        # step through words and create list of 10 groups of three words each
        word_list = [tokens[i:i + k] for i in range(0,10)]
        
        # step through list and print each list value
        print('\nFirst 10 3-shingles in sentence (based on words):\n')
        for i in range(0, len(word_list)):
            print(str(i+1) + ': ' + str(word_list[i]) + '\n')
        
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