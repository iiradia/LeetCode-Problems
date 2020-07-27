class Solution:
    def countPrimes(self, n: int) -> int:
        
        """
        Primitive method, too slow
        
        Time complexity = O(n^2)
        """
        """
        if n<3:
            return 0
        ct=1
        # iterate through odds
        for i in range(3,n,2):
            ret=True
            for j in range(3,i):
                if i%j==0:
                    ret=False
                    break
            if ret:
                ct+=1
    
        return ct
        """
        """
        Trial division method
        
        Time complexity = O(n*sqrt(n))
        """
        """
        a = []
        
        for i in range(2,n):
            if isPrime(i):
                a.append(i)
        return len(a)
    
        """
        """
        Sieve of Eratosthenes method
        
        Time complexity = O(n*log(log(n)))
        """
        if n<3:
            return 0
        # create list of all prime numbers
        primes = [1 for i in range(n)]
        primes[0] = 0
        primes[1] = 0
        sqrt_n = int(n**0.5) + 1
        
        # iterate up to square root of n, since all primes can be found
        for i in range(2,sqrt_n):
            
            # if is prime
            if primes[i] == 1:
                
                # set all multiples to not prime
                for j in range(2,(n//i)+1):
                    try:
                        primes[i*j] = 0
                    except: continue
        
        # return all primes
        return primes.count(1)
        