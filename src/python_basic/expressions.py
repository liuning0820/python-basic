

hour = input('How many hours you work every week?\n')
rate = input('Enter Rate:')
print(type(hour))
print(type(rate))
pay = int(hour) * float(rate)

print(f'Pay: {pay}')
