def divisors(n):
    list = []
    for i in range(n) :
        if n % (i+1) == 0 and (i+1) != 1 and n != (i+1) :
            list.append(i+1)
        elif n == (i+1) and len(list) == 0 and n != 1 :
            return f'{n} is prime'
        elif n == 1 :
            print('use nums > 1')
            break
    return list

# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).