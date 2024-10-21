def user_input():
    print('Enter some numbers separated by commas: ')
    txt = input()
    
    x = [float(i) for i in txt.split(",")]
    return x

def calculate_average_temperature(numbers):
    avg = sum(numbers) / len(numbers)
    return avg
def calc_min_max_temperature(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    return lowest, highest


numbers_list = user_input()
min,max= calc_min_max_temperature(numbers_list)

avg1 = calculate_average_temperature(numbers_list)


print('Average:', avg1)
print('Lowest number:', min)
print('Highest number:', max)