# NUMBER 1(ii)
def sum_of_odd_numbers():
    numbers = [4, 7, 2, 9, 12, 15]
    total = 0
    
    for number in numbers:
        if number % 2 != 0:  
            total += number   
    
print("The sum of odd numbers is: {total}")
sum_of_odd_numbers()
