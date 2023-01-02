def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b and a<c:
        ans = a
    elif b<a and b<c:
        ans = b
    else:
        ans = c
    return ans

print(main(-11, -4, 6))