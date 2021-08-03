from flask import Blueprint, jsonify
from .get_data import *

main_bp = Blueprint("main_bp", __name__, static_folder="static/data")

@main_bp.route("/")
def base():
    return "Hello World"

@main_bp.route("/date/<date>", methods=["GET"])
def get_data(date):
    available_dates = get_all_available_dates()
    if date not in available_dates:
        return jsonify("Date is not available, please try again")
    result = {
        "customers": get_number_customers_by_date(date),
        "total_discount_amount": get_total_discount_amount_by_date(date),
        "items": get_total_number_items_sold_by_date(date),
        "order_total_avg": get_average_order_total_by_date(date),
        "discount_rate_avg": get_average_discount_rates_by_date(date),
        "commissions" : {
            "promotions": get_total_commissions_per_promotion_by_date(date),
            "total": get_total_commissions_by_date(date),
            "order_average": get_average_commission_per_order_by_date(date)
        }

    }
    return jsonify(result)