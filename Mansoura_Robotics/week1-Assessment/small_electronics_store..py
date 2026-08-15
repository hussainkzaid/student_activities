import numpy as np


product_names = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"]

month = np.array(['Jan', 'Feb', 'Mar'])
#Units sold per product for Jan, Feb, Mar
units_sold = [
[50, 60, 75], # Laptop
[200, 240, 210], # Mouse
[150, 160, 140], # Keyboard
[40, 45, 50], # Monitor
[180, 190, 200] # Webcam
]

# Price per unit for each product
price_per_unit = [1200, 25, 75, 300, 50]

product_names_arr = np.array(product_names)

units_sold_arr = np.array(units_sold)

price_per_unit_arr = np.array(price_per_unit)

print(f" The Shape Of Unit Sold Array Is: {units_sold_arr.shape}")
print(f" The Shape Of Price Per Unit Array Is: {price_per_unit_arr.shape}")

#for unit sold array it has 5 rows and 3 columns the 5 rows represent the 5 products (Laptop,Mouse,Keyboard,Monitor,Webcam)
# and the 3 columns represent the Units sold per product for (Jan,Feb,Mar)

#for price per unit array it has 5 rows which represent the price of each product in order (Laptop,Mouse,Keyboard,Monitor,Webcam)


price_per_unit_arr = price_per_unit_arr.reshape(5,1)
monthly_revenue = units_sold_arr * price_per_unit_arr
print(f"Monthly Revenue:\n{monthly_revenue}")

print("*"*45)

total_product_revenue = monthly_revenue.sum(axis = 1)
print(f"Total Product Revenue:\n{total_product_revenue}")

print("*"*45)

print(f"The Product With The Most Total Revenue Is {product_names[total_product_revenue.argmax()]} With Total Revenue {total_product_revenue.max()}")

print("*"*45)

high_value_products_index = total_product_revenue > 15000
high_value_products = product_names_arr[high_value_products_index]
print(f"The Products That Generated More Than $15,000 In Total Revenue Is:\n{high_value_products}")

print("*"*45)

best_month_keyboard_index = units_sold_arr[2].argmax()
print(f"The Month Were The Most Keyboard Sold Is {month[best_month_keyboard_index]}"
      f" With Monthly Revenue = {monthly_revenue[2][best_month_keyboard_index]}")