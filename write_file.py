# Program to show various ways to 
# write data to a file using with statement 
  
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"] 
  
# Writing to file 
with open("myfile3.txt", "w") as file1: 
    # Writing data to a file 
    file1.write("Hello \n") 
    file1.writelines(L) 
  
# Reading from file 
with open("myfile3.txt", "r+") as file1: 
    # Reading form a file 
    print(file1.read()) 