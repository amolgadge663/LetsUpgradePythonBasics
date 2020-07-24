#
#Question 2 :
#list1=[10,20,40,60,70,80] sorted list
#list2=[5,15,25,35,45,60] sorted list
#Merge these two sorted lists to produce one sorted list, but use only loop either while or for only one time.
#

ls1 = [10,20,40,60,70,80]
ls2 = [5,15,25,35,45,60]

ls3 = ls1 + ls2

print(sorted(ls3))
