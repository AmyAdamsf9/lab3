"""""
list_of_ages = (20, 21, 24, 13, 15, 19, 22)
1. Add all ages together
2. Get number of list_of_ages
3. Take the sum from 1. and divide it by 2.
4. Return the output value in 3.

def average_age(ages_list:list):
    """

    :param ages_list: should be a list of ages, expecting the data type
    :return: average age in float


    sum_ages = sum(ages_list) # This will give us the sum of ages
    num_ages = len(ages_list) # Get number of ages in list
    avg_list = sum_ages / num_ages # This is the average age
    return avg_list

def employee_pay():
    hourly_rate = input(f'Please enter your hourly rate, e.g 10.59: ')
    man_hours_worked = float (input(f'Please enter your number of hours worked, eg. 21.5:'))
    emp_pay = hourly_rate * num_hours_worked
    emp_pay = f'£ {emp_pay}'
    return emp_pay

empy_pay = employee_pay()
print(f' Employee Pay is {empy_pay}')
