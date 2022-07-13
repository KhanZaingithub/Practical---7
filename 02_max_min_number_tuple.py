# initializing list  
list = [(2, 3), (4, 7), (8, 11), (3, 6)]
  
# printing original list
print ("The original list is : " + str(list))
  
# using min() and max()
# to get min and max in list of tuples
res1 = min(list)[0], max(list)[0]
res2 = min(list)[1], max(list)[1]
  
# printing result 
print ("The min and max of index 1 :  " +  str(res1))
print ("The min and max of index 2 :  " +  str(res2))