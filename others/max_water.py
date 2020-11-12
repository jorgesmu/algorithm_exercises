def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_left = [height[0]]
    max_right = [height[-1]]
    total = 0
    for i in range(1, len(height)):
        max_left.append(max(max_left[-1], height[i]))
    for i in range(1, len(height)):
        max_right.insert(0, max(max_right[0], height[-1-i]))
    import pdb; pdb.set_trace()
    for i in range(1, len(height)-1):
        total += min(max_right[i], max_left[i]) - height[i]
    return total

trap([0,1,0,2,1,0,1,3,2,1,2,1])
