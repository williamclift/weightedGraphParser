'''
  Scanner
      @author William Clift
      @date   20 April 2021
    Prin. Prog. Lang. - Dr. Mongan

    Run:
      python scanner.py
'''

'''
Samples to Run (Include the quotations):
	'someNode - 5 > anotherNode'
	'someNode - > anotherNode'
	'someNode - 5 > anotherNode < - aFinalNode'


'''

This program takes in a string input that describes a simple graph structure which can be directed and weighted. It does this by parsing '- >' as a singular directed edge between nodes of any name (with no spaces) or '- # >' as a weighted and directed edge between nodes. It also has the capability of going the other way by using the inverse arrow. When inputting, be sure to include quotation marks around the graph structure or else it will not properly read the '<' or '>' symbols.
Since these constants are multiple characters with spaces inbetween, there was extra work needed to look ahead and see if there were weights to add as well or not. 


Conclusion about the Assignment:

I spend about two hours on this assignment so that I could be creative. I think that this is really good practice for parsing strings are trying to determine which objects from the input are keywords or other variable names. I was not entirely sure how to format the output, so what I did was print out the arrays when they are full (they will be backwards because I used push and pop to process them) and then when outputting, I grabbed the nodes each in order with the codes of the reserved operators inbetween. 






	

