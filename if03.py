def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a>c or a<b and a<c:
        return a
    
    elif b>c and b>a or b<c and b<a:
        return b
    
    else:
        return c

print(main(1,-3,6))
    