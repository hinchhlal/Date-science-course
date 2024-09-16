product_price=int(input("Enter the product_price :"))# This is input parameter
if product_price>1000:#if product_price is greater then 1000 you can won 20% off this is offer
	print("The product_price is :{} ".format(product_price*.8))#This is print statemant for calculation 20% off
elif product_price>=3000 and product_price<=4000:#This is geving 30% off if greater then 3000
	if product_price==3999:
		print('you geate job in this mole')
	print("The product_price is : {}".format(product_price*.7)) #This statemant for ge 30% off for offer
elif product_price>=4000:#This condition for 10% price 
	print("Your porduct price is : {}".format(product_price*.9))
else:
	print("Thank you better luck !")



