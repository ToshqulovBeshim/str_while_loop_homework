def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    d=0
    while a<len(s):
        if s[a].isalpha():
            d+=1
        a+=1
    return d
s="yy857 ghjk 84"
print(main(s))