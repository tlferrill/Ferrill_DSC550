# ------------------------------------------------------------------
#   File: Ferrill_Week_02_Exercise_4-3.4.1.py
#   Name: Teresa Ferrill
#   Date: 6/14/2020
# Course: DSC550-T302 Data Mining
#   Desc: Evaluate S-curve
#  Usage: S-curve: 1 - (1 - s**r)**b; specified row and band values with s = 0.1, 0.2....0.9
#    Ref: Jure Leskovec, A. R. (2020). Minning of Massive Datasets. Cambridge: Cambridge University Press. 
# ------------------------------------------------------------------

# import statements
import traceback
import matplotlib.pyplot as plt 

# initialize variables
# variables for row and band values
r1 = 3
b1 = 10
r2 = 6
b2 = 20
r3 = 5
b3 = 50
# list of s values
s_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

def compute_s_curve(row, band):
    print('Row value: {}, Band value: {}'.format(row, band))
    s_curve = []
    for i in range(0, len(s_values)):
        s_curve.append(1-(1-s_values[i]**row)**band)
    return s_curve
    
def plot_s_curve(s_curve_list, row_name, band_name):
    # x axis values 
    x = s_values 
    # y axis values
    y = s_curve_list
    
    # plotting the points
    plt.plot(x,y)
    
    # x axis title
    plt.xlabel('S - Values') 
    # y axis title
    plt.ylabel('S - Curve')
    # graph title
    plt.title('Plotting S-Curve - Row: ' + row_name + ', Band: ' + band_name) 
    # show the plot 
    plt.show() 
    
# main function to obtain list of first 10 3-shingles in the sentence
def main():
    # try block for execution
    try:
        # call to compute and plot s-curve for all three sets of rows and bands
        plot_s_curve(compute_s_curve(r1, b1), str(r1), str(b1))
        plot_s_curve(compute_s_curve(r2, b2), str(r2), str(b2))
        plot_s_curve(compute_s_curve(r3, b3), str(r3), str(b3))
    # exception block to catch any exceptions during execution
    except Exception as exception:
        print('exception')
        # print the traceback of the exception
        traceback.print_exc()
        # list name of exception and any arguments
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));    

if __name__ == '__main__':
    main()