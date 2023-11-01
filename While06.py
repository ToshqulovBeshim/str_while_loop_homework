def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    f=0
    d=0
    while f<len(s):
        if s[f].isalpha() and not s[f]=="a" and not s[f]=="o" and not s[f]=="i" and not s[f]=="u" and not s[f]=="e":
            d+=1
        f+=1
    return d
s="i67RFBohnv"
print(main(s))