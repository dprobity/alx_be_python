# This program will give discount depending o the purchase


print("Hey welcome to X store kindly enter your purchase amount to apply a coupon discount")
# lets get the purchase amount by a customer

purchase_amount = int(input("Enter your total purchase amount in dollars"))

# lets know how much to give as discount

if purchase_amount >= 1000:
    discount_on_purchase = 0.1
    final_payment = purchase_amount - purchase_amount * discount_on_purchase
    print(f"Your payment is: ${final_payment}")
elif purchase_amount >= 500:
    discount_on_purchase = 0.05
    final_payment = purchase_amount - purchase_amount * discount_on_purchase
    print(f"Your payment is: ${final_payment}")
else:
    discount_on_purchase = 0
    final_payment = purchase_amount - purchase_amount * discount_on_purchase
    print(f"Your payment is: ${final_payment}")

