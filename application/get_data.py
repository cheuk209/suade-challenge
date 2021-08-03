import pandas as pd
import pandas as pd
from collections import OrderedDict
import os


cwd = os.getcwd()
data_dir = cwd + '/application/static/data/'
orders_data = pd.read_csv(data_dir + 'orders.csv')
order_lines_data = pd.read_csv(data_dir + 'order_lines.csv')
commissions_data = pd.read_csv(data_dir + 'commissions.csv')
product_promotions_data = pd.read_csv(data_dir + 'product_promotions.csv')


# get all available dates
def get_all_available_dates() -> list:
    order_dates = orders_data['created_at'].str[:10].tolist()
    return order_dates


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

# get vendor ID based on order id and date
def get_vendor_ID_based_on_order_ID_and_date(order_id: int, date: str) -> int:
    vendor_id = orders_data.loc[ (orders_data['id'] == order_id) & (orders_data['created_at'].str[:10] == date), 'vendor_id'].tolist()
    try:
        return vendor_id[0]
    except:
        return 0

# get commission rate based on vendor ID and date
def get_commission_rate_based_on_vendor_ID_and_date(vendor_id: int, date: str) -> float:
    commission_rate = commissions_data.loc[ (commissions_data['date'] == date) & (commissions_data['vendor_id'] == vendor_id), 'rate'].tolist()
    try:
        return commission_rate[0]
    except:
        return 0

# identify all orders placed, get order ID's, get vendor ID's, for total amount on all order lines, multiplied by commission rate
# according to vendor ID's
def get_total_commissions_by_date(date: str) -> float:
    order_ids = get_order_ids_by_date(date)
    total_commission = 0
    for id in order_ids:
        orderline_total_amount = order_lines_data.loc[order_lines_data['order_id'] == id, 'total_amount'].tolist()
        orderline_total_amount = sum(orderline_total_amount)
        vendor_id = get_vendor_ID_based_on_order_ID_and_date(id, date)
        commission_rate = get_commission_rate_based_on_vendor_ID_and_date(vendor_id, date)
        commission = orderline_total_amount * commission_rate
        total_commission = total_commission + commission
    return round(total_commission, 4)

# get total commissions generated that day, then divided by number of orders placed that day
def get_average_commission_per_order_by_date(date: str) -> float:
    total_commission = get_total_commissions_by_date(date)
    num_of_orders = len(get_order_ids_by_date(date))
    if not num_of_orders:
        return 0
    average_commission = total_commission / num_of_orders
    return average_commission

# get products by their product IDs, that are being promoted by date
def get_promoted_products_by_date(date: str) -> dict:
    product_ids = product_promotions_data.loc[product_promotions_data['date'] == date, 'product_id'].tolist()
    promotion_ids = dict.fromkeys(product_ids)
    for id in product_ids:
        promotion_ids[id] = product_promotions_data.loc[
            (product_promotions_data['date'] == date)
            &
            (product_promotions_data['product_id'] == id),
            'promotion_id'
            ].iloc[0]
    return promotion_ids

# total commission per promotion, how many order lines are buying products on days when the products
# are being promoted? 
def get_total_commissions_per_promotion_by_date(date: str) -> dict:
    order_ids = get_order_ids_by_date(date)
    product_ids_dict = get_promoted_products_by_date(date)
    product_ids_list = list(product_ids_dict.keys())
    result = {"1":0, "2":0, "3":0, "4":0, "5":0}
    for order_id in order_ids:
        for product_id in product_ids_list:
            promoted_orderline_amount = order_lines_data.loc[
                (order_lines_data['order_id'] == order_id)
                &
                (order_lines_data['product_id']==product_id),
                'total_amount'
                ].tolist()
            if promoted_orderline_amount:
                promoted_orderline_amount = promoted_orderline_amount[0]
                promotion_id = product_ids_dict[product_id]
                vendor_id = get_vendor_ID_based_on_order_ID_and_date(order_id, date)
                commission_rate = get_commission_rate_based_on_vendor_ID_and_date(vendor_id, date)
                result[str(promotion_id)] = round(commission_rate * promoted_orderline_amount, 2)
    return result