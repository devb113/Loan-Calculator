import argparse
import math

# store the value
parser = argparse.ArgumentParser(description="Find the differentiated and annuity payment")

parser.add_argument("--type", help="choose from diff and annuity")
parser.add_argument("--principal", type=int, help="")
parser.add_argument("--periods", type=int, help="")
parser.add_argument("--interest", type=float, help="")
parser.add_argument("--payment", type=int, help="")

# To fetch the input values

args = parser.parse_args()
# print(args)
# condition's that are invalid

# If --type is specified neither as "annuity" nor as "diff" or not specified at all
if args.type != "diff" and args.type != "annuity":
    print("Incorrect parameters.")

# If --type is specified neither as "annuity" nor as "diff" or not specified at all
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters.")

# These parameters are incorrect because --interest is missing in annuity
elif args.type == "annuity" and args.interest is None:
    print("Incorrect parameters.")

# fewer than four parameters are provided
elif args.type == "annuity" or args.type == "diff":
    if args.payment is None and args.periods is None:
        print("Incorrect parameters.")
    elif args.periods is None and args.principal is None:
        print("Incorrect parameters.")
    elif args.principal is None and args.payment is None:
        print("Incorrect parameters.")
    # an error message when negative values are entered
    elif args.payment is not None:
        if args.payment <= -1:
            print("Incorrect parameters.")
    elif args.periods is not None:
        if args.periods <= -1:
            print("Incorrect parameters.")
    elif args.principal is not None:
        if args.principal <= -1:
            print("Incorrect parameters.")
    elif args.interest is not None:
        if args.interest <= -1:
            print("Incorrect parameters.")
            
# Differentiate payment
if args.type == "diff" and args.principal is not None and args.periods is not None and args.interest is not None and args.payment is None:
    ist = args.interest / 1200
    extra = 0
    for i in range(1, args.periods+1):
        result1 = ((args.principal / args.periods) + ist * (args.principal - (args.principal * (i-1))/args.periods))
        print(f'Month {i}: payment is {math.ceil(result1)}')
        extra += math.ceil(result1)
        over = extra - args.principal
    print(f'Overpayment = {over}')
    
# Annuity payment    
if args.type == "annuity" and args.principal is not None and args.periods is not None and args.interest is not None:
    ist = args.interest / 1200
    res = args.principal * ((ist * pow((1 + ist), args.periods)) / (pow((1 + ist), args.periods) - 1))
    print(f'Your annuity payment = {math.ceil(res)}!')
    extra = math.ceil(res) * args.periods
    over = extra - args.principal
    print(f'Overpayment = {over}')

# Loan principal
if args.type == "annuity" and args.payment is not None and args.periods is not None and args.interest is not None:
    ist = args.interest / 1200
    res = args.payment / ((ist * pow((1 + ist), args.periods)) / (pow((1 + ist), args.periods) - 1))
    print(f'Your loan principal = {math.floor(res)}!')
    extra = args.payment * args.periods
    # assert isinstance(extra, object)
    over = extra - res
    print(f'Overpayment = {math.ceil(over)}')
    
# Time period
if args.type == "annuity" and args.payment is not None and args.principal is not None and args.interest is not None:
    ist = args.interest / (12 * 100)
    res = math.log((args.payment / (args.payment - args.principal * ist)), (1 + ist))
    year = round(res) / 12
    month = round(res) % 12
    if month != 0 and year != 0:
        print(f'It will take {round(year)} years and {math.ceil(month)} months to repay this loan!')
    if month == 0 and year != 0:
        print(f'It will take {round(year)} years to repay this loan!')
    if month != 0 and year == 0:
        print(f'It will take {round(month)} months to repay this loan!')
    extra = (year * 12 + month) * args.payment
    over = extra - args.principal
    print(f'Overpayment = {math.ceil(over)}')
