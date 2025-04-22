def from_n_to_zero(n):
    if n == 0:
        print("already Zero")
    elif n > 0:
        n = n - 1
        while n >= 0:
            print(n)
            n = n - 1
        print()
    else:
        while n <= 0:
            print(n)
            n = n + 1
        print()

from_n_to_zero(0)   
from_n_to_zero(4)   
from_n_to_zero(-3)  
