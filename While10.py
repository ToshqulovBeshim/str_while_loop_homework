def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
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
                d+=int(str(s[a]))
        a+=1
    return d
s="345623"
print(main(s))
