# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
current_month = 1


while principal > 0:
    principal = principal * (1+rate/12)
    if principal > payment:
        principal -= payment
    else:
        principal = 0
    if current_month >= extra_payment_start_month and current_month <= extra_payment_end_month:
        if principal > extra_payment:
            principal -= extra_payment
            total_paid = total_paid + payment + extra_payment
    else:
        total_paid += payment
    print(f'{current_month} {total_paid} {round(principal, 2)}')
    current_month += 1

print(f'Total paid {round(total_paid,2)}')
print(f'Months {current_month - 1}')