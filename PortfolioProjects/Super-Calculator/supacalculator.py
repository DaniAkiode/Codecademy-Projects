class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers 

    def add(self, numbers):
        total = 0
        for num in numbers:
            total += num 
        return total
    
    def subtract(self, numbers):        
        if numbers:
            total = numbers[0]
            for num in numbers[1:]:
                total -= num 
        else:
            total = 0
        return total 

    def multply(self, numbers):
        total = 0
        for num in numbers:
            total *= num 
        return total
    
    def divide(self, numbers):
        if not numbers:
            return 0
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                raise ValueError("Division By Zero")
            result /= num
        return result
                    
    def modulo(self, numbers):
        if not numbers:
            return 0     
        result = numbers[0] 
        for num in numbers[1:]:
            if num == 0:
                raise ValueError("Modulation by Zero")
            result %= num
        return result
