def print_prime_factors(numbers):
    factor =2
   while factor <=  number:
       if number % factor ==0:
           print(factor)
           number = number / factor
       else :
           factor = factor+1
    return "Done"
