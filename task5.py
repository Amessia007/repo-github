a = int(input('input profit '))
b = int(input('input costs '))
if a > b:
    print('the company works with profit, profitability is: ', int(a/b))
    p = int(input('input people '))
    print('profitability per people: ', float(a/p))
else: print('the firm is operating at a loss')
