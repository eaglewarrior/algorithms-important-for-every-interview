a=[1,2,32,33,24,22]#the list from where we search our number
def linear_search(a,num):
  for i in range(len(a)):
    if a[i]==num:
      print "The number "+str(num)+" is present at index "+str(i)
      
      
linear_search(a,24)
#Worst-case performance 	O(n)
#Best-case performance 	O(1)
#Average performance 	O(n)
