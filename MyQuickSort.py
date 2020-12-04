from stackwithlist import mystack

def QuickSort(lst):
    if len(lst) == 1:
        return
    
    stack = mystack()
    stack.push( (0, len(lst) - 1) )
    while not stack.isEmpty():
        current_range = stack.pop()
        left, right = current_range  # tuple unpack
        loc = left  # selecting first element of current list to be pivot everytime
        pivot_element = lst[loc]
        
        # move pivot element to its correct position
        while left < right:
            if loc == left:  # need to search from right to loc
                while right != loc:
                    if lst[right] < pivot_element:
                        lst[right], lst[loc] = lst[loc], lst[right]
                        loc = right
                        break
                    right -= 1
                    
            else:  # need to search from left to loc
                while left != loc:
                    if lst[left] > pivot_element:
                        lst[left], lst[loc] = lst[loc], lst[left]
                        loc = left
                        break
                    left += 1
        
        if (loc - current_range[0]) > 1:  # if left subsequence has more than 1 element
            stack.push( (current_range[0], loc - 1) )
        if (current_range[1] - loc) > 1:  # if right subsequence has more than 1 element
            stack.push( (loc + 1, current_range[1]) )

# Test code
# lst = "11 55 77 90 40 60 99 22 88 66".split()
# print("List before sorting:", lst)
# QuickSort(lst)
# print("List after sorting:", lst)
