# Write a function called median that takes a list as an input and returns the median value of the list. For example: median([1, 1, 2]) should return 1.

## The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
## If the list contains an even number of elements, your function should return the average of the middle two.



def median(lst):
  totals_ele = len(lst)
  
  sorted_lst = sorted(lst)
  print sorted_lst
  if totals_ele % 2 == 0:
    m1 = sorted_lst[totals_ele/2]
    m2 = sorted_lst[totals_ele/2 - 1]
    return (m1 + m2) / 2.0
  else:  
  	return sorted_lst[totals_ele/2]
