def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dict ={}
    for num in nums:
        dict[num] = nums.count(num)
    max_val = max(dict.values())
 #   print(max_val)
    for(num, val) in dict.items():
        if val == max_val:
            return num