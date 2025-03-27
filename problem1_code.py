def determine_primes(n: int):
    """
    Determines all prime numbers from 2 to n using the Sieve of Eratosthenes algorithm.
    
    Args:
        n: An integer representing the upper limit of the range to check for primes.
        
    Returns:
        A tuple containing:
            - A list of all prime numbers from 2 to n
            - The number of times the algorithm traversed the initial list of integers
            
    Raises:
        Exception: If the input is not an integer
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise Exception("Input must be an integer")
    
    # Create a list of all integers in the range (represented as boolean values)
    is_prime = [True] * (n + 1)
    
    # 0 and 1 are not prime numbers
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    
    # Counter for the number of traversals
    traversal_count = 0
    
    # Start with p = 2, the smallest prime number
    p = 2
    
    while p * p <= n:
        traversal_count += 1
        
        # If p is unmarked (prime), mark its multiples
        if is_prime[p]:
            # Mark all multiples of p as non-prime
            for i in range(2 * p, n + 1, p):
                is_prime[i] = False
        
        # Find the next unmarked number
        p += 1
        while p <= n and not is_prime[p]:
            p += 1
    
    # Collect all prime numbers
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    
    return (primes, traversal_count)
