from product_db import product_db
from sale_order_db import sale_order_db

def get_kpis(selected_date_from, selected_date_to):
	# Your goal is to develop a function that returns the following kpis between two given dates as inputs:
	# - total revenue
	# - average ticket (average value of a sale order)
	# - margin (total gross cost / total revenue)
	
	kpis = {
		'total_revenue': None,
		'average_ticket': None,
		'margin': None
	}

	# write your solution here

	return kpis

kpis = get_kpis('2021-07-1', '2021-07-8')
print(kpis)