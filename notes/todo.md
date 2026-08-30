Soon:
* Write a generator for primes that dynamically expands
* Rewrite primality / other intensive tests in C++, use a Python wrapper to call them
    * Have a checker that determines if the input is of the appropriate size for C++; not larger than long long, but longer than the cutoff point where C++ + 2ms overhead is faster
* Fix up the `partitions` function in `experiments.ipynb` to be iterative
* Implement the "how many ways to write n as a sum of terms" function from prob077.py
    * Make a bottom-up implementation of this
* Make a continued fraction function
    * Clean this up from prob066.py

Distant:
* Implement the Miller-Rabin primality test
* Eventually make `is_prime` a wrapper function that calls all the other primality testers using heuristics for which will be fastest as well as user input
