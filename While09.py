def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    d=0
    while a<len(s):
        if s[a].isdigit():
            d+=int(str(s[a]))
        a+=1
    return d
s="2345"
print(main(s))