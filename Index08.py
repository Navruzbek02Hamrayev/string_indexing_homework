def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0]=="*" or s[1]=="*" or s[2]=="*" or s[3]=="*":
        return s.index("*")
    if s[0]!="*" and s[1]!="*" and s[2]!="*" and s[3]!="*":
        return False
print(main("2*44"))
print(main("good"))
        