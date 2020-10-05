from math import log, trunc, pow, ceil
import argparse

parser = argparse.ArgumentParser(description='Loan calculator')
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()

if args.type == 'diff':
    if args.interest is None:
        print('Incorrect parameters')
    elif args.interest is not None:
        P = args.principal
        n = args.periods
        i = args.interest / (12 * 100)
        sum = 0
        for m in range(1, n + 1):
            D = ceil(P / n + i * (P - (P * (m - 1)) / n))
            print(f'Month {m}: payment is {D}')
            sum += D
            overpayment = sum - P
        print(f'\nOverpayment = {overpayment}')

if args.type == 'annuity':
    if args.interest is None:
        print('Incorrect parameters')
    elif args.interest is not None:

        if not args.periods:
            P = args.principal
            i = args.interest / (12 * 100)
            a = args.payment
            n = ceil(log(a / (a - i * P), 1 + i))
            if n >= 12:
                years = trunc(n / 12)
                months = n % 12
                if years == 1 and months == 1:
                    print(f'It will take {years} year and {months} month to repay this credit!')
                elif years == 1 and months > 1:
                    print(f'It will take {years} year and {months} months to repay this credit!')
                elif years > 1 and months > 1:
                    print(f'It will take {years} years and {months} months to repay this credit!')
                else:
                    print(f'It will take {years} years to repay this credit!')
            else:
                if n == 1:
                    print(f'It will take {n} month to repay this credit!')
                print(f'It will take {n} months to repay this credit!')

            overpayment = (n * a) - P
            print(f'Overpayment = {overpayment}')

        if not args.payment:
            P = args.principal
            n = args.periods
            i = args.interest / (12 * 100)

            a = P * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
            print(f'Your monthly payment = {ceil(a)}!')

        if not args.principal:
            n = args.periods
            i = args.interest / (12 * 100)
            a = args.payment

            P = trunc(a / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
            print(f'Your credit principal = {P}!')
            overpayment = (n * a) - P
            print(f'Overpayment = {overpayment}')