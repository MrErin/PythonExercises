class Calculator():
    '''Performs basic mathematical operations

    Methods:
        add(number, number)
        subtract(number, number)
        multiply(number, number)
        divide(number, number)
        '''

    def add(self, first_num, second_num):
        '''Adds two numbers

        Arguments:
            first_num: any number
            second_num: any number
            '''
        return first_num + second_num

    def subtract(self, first_num, second_num):
        '''Subtracts two numbers

        Arguments:
            first_num: any number
            second_num: any number
            '''
        return first_num - second_num

    def multiply(self, first_num, second_num):
        '''Multiplies two numbers

        Arguments:
            first_num: any number
            second_num: any number
            '''
        return first_num * second_num

    def divide(self, first_num, second_num):
        '''Dividess two numbers

        Arguments:
            first_num: any number
            second_num: any number
            '''
        return first_num / second_num


myCalc = Calculator

print(myCalc.add(1, 1))
print(myCalc.subtract(10, 1))
print(myCalc.multiply(1, 6))
print(myCalc.divide(6, 3))
