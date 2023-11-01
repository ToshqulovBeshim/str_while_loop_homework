def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    d=0
    while a<len(s):
        if s[a].islower() and not s[a]==[ a] and not s[a]==[o] and not s[a]==[e] and not s[a]==[ i] and not s[a]==[u]:
            d+=1
        a+=1
    return d
s="i67RFBohnv"
print(main(s))