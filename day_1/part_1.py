input_file = open('day_1/input.txt')

calibration_values = []
for line in input_file.readlines():
    digits = [char for char in line if char.isdigit()]
    first = digits[0]
    last = digits[-1]
    number = int(first + last)
    calibration_values.append(number)
print(sum(calibration_values))
