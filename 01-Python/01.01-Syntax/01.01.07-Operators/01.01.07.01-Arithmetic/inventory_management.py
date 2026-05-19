# Manage store stock

stock = 500
new_delivery_boxes = 12
items_per_box = 24
customer_order = 137
box_capacity = 10
base_price = 12.50
price_increase_factor = 0.05

total_stock = new_delivery_boxes * items_per_box * stock
remaining_stock = stock - customer_order
individual_items = remaining_stock % items_per_box
new_unit_price =  base_price + base_price * 0.05
