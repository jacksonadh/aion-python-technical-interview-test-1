from datetime import datetime

from product_db import product_db
from sale_order_db import sale_order_db

def get_kpis(selected_date_from, selected_date_to):
	# Your goal is to develop a function that returns the following kpis between two given dates as inputs:
	# - total revenue before cancellation (sale's total income, sum of the product's full price, counting the canceled orders as well)
	# - cancellation (canceled sale orders / total amount of sale orders)
	# The variable product_db contains a list of all products, where each item is a dictionary with the product's id, full price and gross cost.
	# And sale_order_db contains a list of sale orders, where each item is a dictionary with the sale's id, customer's id, a list of purchased products, sale's date and is_canceled boolean value.

	# A little help:
	selected_date_from = datetime.strptime(selected_date_from, '%Y-%m-%d')
	selected_date_to = datetime.strptime(selected_date_to, '%Y-%m-%d')

	# Write your solution here

	# [
	# {
  #      "sale_order_id": 420351,
  #     "customer_id": 343556,
  #      "purchased_products": [188024, 188047, 188048, 188023],
  #      "sale_order_purchased_at": datetime(2021, 6, 30, 0, 0),
  #      "is_canceled": False,
  #  },]

	#product_db = [
  #  {"product_id": 188086, "full_price": 69.0, "gross_cost": 33.15},


# primeiro acessar o vetor de sale_order_db - Ok
# segundo para cada item do vetor de sale_order_db vericar qual tipo de carrinho (cancelado ou não) - Ok
# terceiro acessar o vetor de purchased_products
# quarto checar se cada item de purchased_products existe em product_db
# quinta se o item existir somar o valor de full_price (canelado ou não)
# 


	def total_revenue():
		total_canceled = 0
		total_not_canceled = 0
		for sale in sale_order_db:
			if sale["is_canceled"] == True:
				for i in sale["purchased_products"]:
					for product in product_db:
						if i == product["product_id"]:
							total_canceled = total_canceled + product["full_price"]
							print("total_canceled: ", total_canceled) 
			else:
				for i in sale["purchased_products"]:
					for product in product_db:
						if i == product["product_id"]:
							total_not_canceled = total_not_canceled + product["full_price"]
							print("total_not_canceled: " ,total_not_canceled) 


	# Return the kpi values following the variable format below:
	kpis = {
		'total_revenue': total_revenue(),
		'cancellation': total_canceled(),
	}

	return kpis

kpis = get_kpis('2021-07-01', '2021-07-08')
print(kpis)

# To run this file just type the command below in the console:
# python test.py
