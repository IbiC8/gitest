#Ask for hours and pay rate, you have to pay 1.5 times when the worker works more than 40.
hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter pay rate:')
r = float(rate)
if h <= 40 :
    Pay = h * r
    print(Pay)
else :
    Pay = 40 * r
    xtra = (h - 40) * (r*1.5)
    print(Pay + xtra)
