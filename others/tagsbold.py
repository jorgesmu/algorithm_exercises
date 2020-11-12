def addBoldTag(s, dict):
    """
    :type s: str
    :type dict: List[str]
    :rtype: str
    """
    bold = [False for si in range(len(s))]
    for i in range(len(s)):
        for word in dict:
            if (i + len(word)-1) < len(s):
                if s[i:i+len(word)] == word:
                    for j in range(i, i+len(word)):
                        bold[j] = True
    import itertools
    ans = []
    for incl, grp in itertools.groupby(zip(s, bold), lambda z: z[1]):
        import pdb; pdb.set_trace()
        if incl: ans.append("<b>")
        ans.append("".join(z[0] for z in grp))
        if incl: ans.append("</b>")
    return "".join(ans)
print(addBoldTag("aaabbcc", ["aaa","bc" ]))