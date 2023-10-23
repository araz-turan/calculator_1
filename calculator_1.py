import math
continue_operation = '1'
while continue_operation == '1':
    def input_control_num1():
        while True:
            input_1 = input('Enter a number: ')
            if input_1.isdigit():
                return int(input_1)
            else:
                try:
                    input_1 = float(input_1)
                    return input_1
                except:
                    print('Enter a valid number')
    num1 = input_control_num1()
    def oper_input_control():
        oper_elements = ['+', '-', '*', '/', '**', 'sqrt', 'factorial', 'floor', 'ceil', 'log.10', 'log.e', 'log(x,y)']
        oper = input('Enter one of these operations {+,-,*,/,**,sqrt,factorial,floor,ceil,log.10,log.e,log(x,y)}: ')
        while oper not in oper_elements:
            print('You must enter an operation!')
            oper = input('Enter one of these operations {+,-,*,/,**,sqrt,factorial,floor,ceil,log.10,log.e,log(x,y)}: ')
        else:
            return oper
    oper = oper_input_control()
    oper_list = ['sqrt', 'factorial', 'ceil', 'floor', 'log.10', 'log.e']
    if oper not in oper_list:
        def input_control_num2():
            while True:
                input_2 = input('Enter a number: ')
                if input_2.isdigit():
                    return int(input_2)
                else:
                    try:
                        input_2 = float(input_2)
                        return input_2
                    except:
                        print('Enter a valid number')
        num2 = input_control_num2()
    else:
        num2 = None
    def calculator(num1,oper,num2):
        if oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
        elif oper == '*':
            return num1 * num2
        elif oper == '/':
            if num2 == 0:
                return 'This operation cannot be performed'
            else:
                return num1 / num2
        elif oper == '**':
            return num1 ** num2
        elif oper == 'sqrt':
            if num1 >= 0:
                return math.sqrt(num1)
            else:
                return 'This operation cannot be performed'
        elif oper == 'factorial':
            if num1 >= 0: 
                return math.factorial(num1)
            else:
                return 'This operation cannot be performed'
        elif oper == 'floor':
            return math.floor(num1)
        elif oper == 'ceil':
            return math.ceil(num1)
        elif oper == 'log.10':
            if num1 >= 0 :
                return math.log(num1, 10)
            else:
                return 'This operation cannot be performed'
        elif oper == 'log.e':
            if num1 >= 0:
                return math.log(num1)
            else:
                return 'This operation cannot be performed'
        elif oper == 'log(x,y)':
            if (num1 >= 0) and (num2 >= 0):
                return math.log(num1,num2)
            else:
                return 'This operation cannot be performed'
    print('Result = {}'.format(calculator(num1,oper,num2)))
    continue_operation = input('Do you want to continue the operation? \n 1.Yes \n 2.No \n \t :')
else:
    print('The operation has ended...')