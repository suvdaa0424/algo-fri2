#asking for user input
string = input("Please Enter your own single word: ")
#what is that below? it's slicing and when you write it this way
#it starts from the end towards the first, using index values
if(string == string[:: -1]):
    print("True")
else:
    print("False")