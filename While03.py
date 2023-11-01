def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    d=0
    while a<len(s):
        if not s[a].isalpha() and not s[a].isdigit() and s[a]!=' ':
            d+=1
        a+=1
    return d
s="@#$$$$$56tynhvjrm454ghbvn"
print(main(s))