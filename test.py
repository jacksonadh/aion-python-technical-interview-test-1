from product_db import product_db
from sale_order_db import sale_order_db

def get_kpis(selected_date_from, selected_date_to):
	# Your goal is to develop a function that returns the following kpis between two given dates as inputs:
	# - total revenue
	# - average ticket (average value of a sale order)
	# - margin (total gross cost / total revenue)
	# The variable product_db contains a list of all products, where each item is a dictionary with the product's id, full price and gross cost.
	# And sale_order_db contains a list of sale orders, where each item is a dictionary with the sale's id, customer's id, a list of purchased products, sale's date and cancelation's date (if there was any).

	# Return the kpi values following the variable format below:
	kpis = {
		'total_revenue': None,
		'average_ticket': None,
		'margin': None
	}

	# Write your solution here

	return kpis

kpis = get_kpis('2021-07-1', '2021-07-8')
print(kpis)
# To run this file just type the command below in the console:
# python test.py