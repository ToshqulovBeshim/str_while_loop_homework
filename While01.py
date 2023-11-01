def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    d=0
    while a<len(s):
        if s[a].isdigit():
            d+=1
        a+=1
    return d
s="python 2023"
print(main(s))