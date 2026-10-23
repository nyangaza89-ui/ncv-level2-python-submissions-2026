
def place_order(item):
    print(f'prepare order: your order {item}')
#eggs =>4
    #tot 
def calc_tot(item):
    base_price = 25.5
    VAT = 0.15
    tot_price =( base_price +len(item)) * 1.15
   
    return tot_price

def get_order():
    print('prepare order')
    return'Collect your order'
    
myFood = input("What would you like:")
place_order (myFood)

print(get_order())
order_tot = calc_tot(myFood)
print(f'Your order costs: R{round (order_tot,2)}')