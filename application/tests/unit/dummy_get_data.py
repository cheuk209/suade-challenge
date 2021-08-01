import pandas as pd
from collections import OrderedDict

orders_data = pd.read_csv('orders.csv')
order_lines_data = pd.read_csv('order_lines.csv')

# identify orders that were placed given a date
def get_order_ids_by_date(date: str) -> list:
    order_ids = orders_data.loc[orders_data["created_at"].str[:10] == date, "id"].tolist()
    return order_ids

# identify orderlines and return quantity given order ID's
def get_orderlines_by_ids(order_ids: list) -> list:
    orderlines_quantity = order_lines_data[order_lines_data['order_id'].isin(order_ids)]['quantity'].tolist()
    return orderlines_quantity

# identify orders placed on date, then return total number of items sold on those orders
def get_total_number_items_sold_by_date(date: str) -> int:
    order_ids = get_order_ids_by_date(date)
    orderlines_quantity = get_orderlines_by_ids(order_ids)
    number_of_items_sold = sum(orderlines_quantity)
    return number_of_items_sold

# identify orders placed on date, return number of unique customer ID's on those orders
def get_number_customers_by_date(date: str) -> int:
    customer_ids =  orders_data.loc[orders_data["created_at"].str[:10] == date, "customer_id"].tolist()
    customer_ids = list(set(customer_ids))
    unique_number_customers = len(customer_ids)
    return unique_number_customers

# identify orderlines on date, sum on discounted amount
def get_total_discount_amount_by_date(date: str) -> int:
    order_ids = get_order_ids_by_date(date)
    orderlines_discount = order_lines_data[order_lines_data['order_id'].isin(order_ids)]['discounted_amount'].tolist()
    return sum(orderlines_discount)

# identify orderlines on date, get all discount rates and average them by number of orderlines
def get_average_discount_rates_by_date(date: str) -> float:
    order_ids = get_order_ids_by_date(date)
    orderlines_discount_rates = order_lines_data[order_lines_data['order_id'].isin(order_ids)]['discount_rate'].tolist()
    if not orderlines_discount_rates:
        return 0
    average_discount_rate = sum(orderlines_discount_rates) / len(orderlines_discount_rates)
    return round(average_discount_rate, 4)

# identify all order lines, get total amount for all of them, then average them by number of orderlines
def get_average_order_total_by_date(date: str) -> float:
    order_ids = get_order_ids_by_date(date)
    orderlines_total_amount = order_lines_data[order_lines_data['order_id'].isin(order_ids)]['total_amount'].tolist()
    if not orderlines_total_amount:
        return 0
    average_order_total = sum(orderlines_total_amount) / len(orderlines_total_amount)
    return round(average_order_total, 4)