def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    d=0
    a=0
    while a<len(s):
        if s[a].isdigit():
            if int(str(s[a]))%2==0:
                d+=1
        a+=1
    return d
s="568788976"
print(main(s))
    