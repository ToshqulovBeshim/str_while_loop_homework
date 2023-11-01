def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    d=0
    while a<len(s):
        if s[a].isupper():
            d+=1
        a+=1
    return d
s="uhvingjfHYUHJuhij"
print(main(s))