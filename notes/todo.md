Soon:
* Fix up the `partitions` function in `experiments.ipynb` to be iterative
* Implement euler totient function using the formula
* Implement the "how many ways to write n as a sum of terms" function from prob077.py
    * Make a bottom-up implementation of this
* Make a # of digits function
* Make a continued fraction function
    * Clean this up from prob066.py
* Fix prime_factors.py - this is very slow when there are large primes. Keep track of n / all primes so far, and only go up to the square root of that point before terminating and knowing the final number is a prime
    * Verify that I didn't break it; compare speed to original function
    * Figure out why my implementation that gets the factors then combines them is so much slower

Distant:
* Implement the Miller-Rabin primality test
* Eventually make `is_prime` a wrapper function that calls all the other primality testers using heuristics for which will be fastest as well as user input
