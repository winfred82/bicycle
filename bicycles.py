import random

class Bicycle():
	"""docstring for Bicycle"""
	def __init__(self, name,weight,cost):
		self.name=name
		self.weight=weight
		self.cost=cost

class BikeShop():
	"""docstring for BikeShop"""
	def __init__(self, name,bicycles):
		self.name=name
		inventories_list=[]
		for bi in bicycles:
			inventories_list.append({'bike_name':bi.name,'inventory':50})
		self.inventories=inventories_list

	def sell(bicycles):
		total_margin=0
		for bike in bicycles:
			total_margin+=bike.cost*0.2
			for invs in self.inventories:
				if invs['bike_name']==bike.name:
					invs['inventory']-=1
		return total_margin

class Customer():
	"""docstring for Customer"""
	def __init__(self, name,fund,bicycles):
		self.name = name
		self.fund=fund

	def can_buy_bike():
		for bike in bicycles:
			if self.fund>=bike.cost*1.2:
				return True
		return False

	def buy(bike):
		self.fund=self.fund-bike.cost*1.2

if __name__ == '__main__':
	
	
	Bicycle_A=Bicycle('Bicycle_A',30,100)
	Bicycle_B=Bicycle('Bicycle_B',30,150)
	Bicycle_C=Bicycle('Bicycle_C',30,120)
	Bicycle_D=Bicycle('Bicycle_D',30,800)
	Bicycle_E=Bicycle('Bicycle_E',30,450)
	Bicycle_F=Bicycle('Bicycle_F',30,360)
	bicycles=[Bicycle_A,Bicycle_B,Bicycle_C,Bicycle_D,Bicycle_E,Bicycle_F]

	bicycle_shop=BikeShop('My bike Shop',bicycles)

	Customer_A=Customer('Customer_A',200,bicycles)
	Customer_B=Customer('Customer_B',500,bicycles)
	Customer_C=Customer('Customer_C',1000,bicycles)

	customers=[Customer_A,Customer_B,Customer_C]

	
	affort_list=[]
	for customer in customers:
		customer_affort_list=[]
		print 'I am {}\n'.format(customer.name)
		print 'And I can afford following bikes\n'
		for bi in bicycles:
			if customer.fund>=bi.cost*1.2:
				print bi.name +'\n'
				customer_affort_list.append(bi)
		affort_list.append({'customer_name':customer.name,'can_buy_list':customer_affort_list})

	print 'Bike Shop now have {} bikes \n'.format(len(bicycles))

	print 'And we have bike inventory\n'

	for inventory in bicycle_shop.inventories:
		print 'Bike {}:{}'.format(inventory['bike_name'],inventory['inventory'])


	margin_sum=0
	for cus in customers:
		for affort in affort_list:
			if affort['customer_name']==cus.name:
				bike=affort['can_buy_list'][2]
				print '{} buy {} and spends ${}, then the fund only left'.format(cus.name,bike.name,bike.cost*1.2)
				print '{}'.format(cus.fund-bike.cost*1.2)
				margin=bicycle_shop.sell([bike])
				margin_sum+=margin
				for inventory in bicycle_shop.inventories:
					print 'Bike {}:{}'.format(inventory['bike_name'],inventory['inventory'])
	
				


	print '\n After customers bought three bikes, bike shop get {} profit'.format(margin_sum)
	
	

