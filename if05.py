def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a1 = n%10
    a2 = (n%100)//10
    a3 = (n%1000)//100
    a4 = (n%10000)//1000
    a5 = n//10000
    m = a1
    if a2>m:
        m = a2
    if a3>m:
        m = a3
    if a4>m:
        m = a4
    if a5>m:
        m = a5

    return m 