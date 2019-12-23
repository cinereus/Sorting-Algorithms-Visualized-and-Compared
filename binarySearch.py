"""
Muhammet Furkan MUŞTU
160403041

"""
""" Binary search """
# Returns index of x in arr if present, else -1 
def binarySearch (array, left, right, x): 
  
    # Check base case 
    if right >= left: 
  
        mid = int(left + (right - left)/2)
  
        # If element is present at the middle itself 
        if array[mid] == x: 
            return str(mid+1)
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif array[mid] > x: 
            return binarySearch(array, left, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(array, mid+1, right, x) 
  
    else: 
        # Element is not present in the array 
        return "Not Found !!"