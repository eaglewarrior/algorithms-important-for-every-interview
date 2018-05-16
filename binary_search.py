a=[ 2, 3, 4, 20, 24]#the list from where we search our number
def binary_search(a,s,e,num):
  if s<=e:
     mid = s + (e - s)/2;
     if a[mid]==num:
         return mid
     elif a[mid] > num:
         return binary_search(a,s,mid-1,num)#as number is less than #mid so we donot have to include mid in our next search
     else:
          return binary_search(a,mid+1,e,num)#as number is greater than mid we dont have to consider the mid number
  else:
      return -1
result=binary_search(a,0,len(a),24)
print "Element is present at index %d" % result

