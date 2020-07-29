#
#Question 3:
#Take a list as shown below
#[(1,2,3), [1,2], ['a','hit','less']]
#The List contains tuple and lists. Make the elements of inner lists and tuples to outer list
#

list1=[(1,2,3),[1,2],['a','hit','less']]

list2=[i for each in list1 for i in each]
print (list2)