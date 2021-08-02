import pandas as pd
import os
from dummy_get_data import *

def test_get_order_ids_by_date():
    orders_expected = get_order_ids_by_date('2021-08-01')
    assert orders_expected == [2,3]

def test_get_orderlines_by_ids():
    order_ids = get_order_ids_by_date('2021-08-01')
    orderlines_quantity_expected = get_orderlines_by_ids(order_ids)
    assert orderlines_quantity_expected == [30, 12, 40, 10, 10, 56]

def test_get_number_items_sold_by_date():
    assert get_total_number_items_sold_by_date('2021-08-01') == 158
    assert get_total_number_items_sold_by_date('2012-09-12') == 0

def test_get_number_customers_by_date():
    assert get_number_customers_by_date('2021-08-01') == 2
    assert get_number_customers_by_date('2021-08-02') == 2
    assert get_number_customers_by_date('2012-09-12') == 0

def test_get_total_discount_amount_by_date():
    assert get_total_discount_amount_by_date('2021-07-31') == 0
    assert get_total_discount_amount_by_date('2021-08-01') == 43

def test_get_average_discount_rates_by_date():
    assert get_average_discount_rates_by_date('2021-07-31') == 0
    assert get_average_discount_rates_by_date('2021-08-01') == 0.2167
    assert get_average_discount_rates_by_date('2021-08-02') == 0.15

def test_get_average_order_total_by_date():
    assert get_average_order_total_by_date('2021-07-31') == 0
    assert get_average_order_total_by_date('2021-08-01') == 41.8333
    assert get_average_order_total_by_date('2021-08-02') == 50.8

def test_get_vendor_ID_based_on_order_ID_and_date():
    assert get_vendor_ID_based_on_order_ID_and_date(2, '2021-08-01') == 3
    assert get_vendor_ID_based_on_order_ID_and_date(3, '2021-08-01') == 4
    assert get_vendor_ID_based_on_order_ID_and_date(6, '2021-08-03') == 9

def test_get_commission_rate_based_on_vendor_ID_and_date():
    assert get_commission_rate_based_on_vendor_ID_and_date(2, '2021-08-01') == 0.07
    assert get_commission_rate_based_on_vendor_ID_and_date(3, '2021-08-01') == 0.27

def test_get_total_commissions_by_date():
    assert get_total_commissions_by_date('2021-07-31') == 0
    assert get_total_commissions_by_date('2021-08-01') == 55.55
    assert get_total_commissions_by_date('2021-08-02') == 30.22
    assert get_total_commissions_by_date('2021-08-03') == 1.4

def test_get_average_commission_per_order_by_date():
    assert get_average_commission_per_order_by_date('2021-07-31') == 0
    assert get_average_commission_per_order_by_date('2021-08-01') == 27.775
    assert get_average_commission_per_order_by_date('2021-08-03') == 1.4

def test_get_promoted_products_by_date():
    assert get_promoted_products_by_date('2021-08-01') == {572: 3, 242:4, 139:4, 98:3, 835: 5}

def test_get_total_commissions_per_promotion_by_date():
    assert get_total_commissions_per_promotion_by_date('2021-07-31') == {"1":0, "2":0, "3":0, "4":0, "5":0}
    assert get_total_commissions_per_promotion_by_date('2021-08-01') ==  {"1":0, "2":0, "3":11.2, "4":1.96, "5":0}
    assert get_total_commissions_per_promotion_by_date('2021-08-02') ==  {"1":1.3, "2":2.76, "3":0.6, "4":0, "5":0}