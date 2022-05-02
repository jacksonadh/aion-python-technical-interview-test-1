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
	def total_revenue():
		for sale in sale_order_db:
			total_sale = sale.get("purchased_products")
			for product in product_db:
				total_product = product.get("product_id")
				print("este é o total_sale: ", total_sale)
				print("este é o total_product: ", total_product)
				


	# Return the kpi values following the variable format below:
	kpis = {
		'total_revenue': total_revenue(),
		'cancellation': None,
	}

	return kpis

kpis = get_kpis('2021-07-01', '2021-07-08')
print(kpis)

# To run this file just type the command below in the console:
# python test.py
