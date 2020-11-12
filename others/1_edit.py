def edit(s,t):
    if abs(len(s) - len(t)) > 1:
        return False
    if s == t:
        return True

    if len(s) < len(t):
        shortest = s
        longest = t
    else:
        shortest = t
        longest = s
    import pdb; pdb.set_trace()
    for i in range(len(shortest)):
        if shortest[i] != longest[i]:
            if len(shortest) != len(longest):
                shortest = shortest[0:i] + longest[i] + shortest[i:]
            else:
                shortest = shortest[0:i] + longest[i] + shortest[i+1:]
            return s == t
    # should never happen
    return False

edit('a', '')