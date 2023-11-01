def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    d=0
    while a<len(s):
        if s[a].isdigit():
            if int(str(s[a]))%2==1:
                d+=1
            a+=1
    return d
s="234567654"
print(main(s))