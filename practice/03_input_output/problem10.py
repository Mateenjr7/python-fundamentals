#Q10. Bill Calculator

#Take:

#item price
#quantity
#discount percentage

#Calculate the final bill.

#Example

#Input:
#Price: 500
#Quantity: 3
#Discount: 10

#Output:
#Original Bill: 1500
#Discount: 150
#Final Bill: 1350

num = float(input("Enter the item price: "))
quantity = int(input("Enter the quantity: "))
discount = float(input("Enter the discount percentage: "))

original_bill = num * quantity
discount_amount = (discount / 100) * original_bill
final_bill = original_bill - discount_amount

print("Original Bill:", original_bill)
print("Discount:", discount_amount)
print("Final Bill:", final_bill)