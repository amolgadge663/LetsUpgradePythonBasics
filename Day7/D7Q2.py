#
#Question 2:
#Take a list of tuple as shown below.
#[(1,2), (3,4), (5,6),(4,5)]
#Make a new list which contains the sum of the number of tuples.
#For example
#Input
#[(1,2), (3,4), (5,6)]
#Output
#[3, 7, 11]
#

ls1 = [(1,2), (3,4), (5,6),(4,5)]
ls2 = []
for n in ls1:
    ls2.append(n[0] + n[1])
    
print(ls2)