def quick_sort(lst):
    # Base case: an empty list or a list with one element is already sorted
    if len(lst) <= 1:
        return lst
    
    # 1. Choose a pivot value (using the first element of the list)
    pivot = lst[0]
    
    # 2. Partition the input list into three sublists using list comprehensions
    less_than = [x for x in lst if x < pivot]
    equal_to = [x for x in lst if x == pivot]
    greater_than = [x for x in lst if x > pivot]
    
    # 3. Recursively sort sublists and concatenate them to produce the final list
    return quick_sort(less_than) + equal_to + quick_sort(greater_than)