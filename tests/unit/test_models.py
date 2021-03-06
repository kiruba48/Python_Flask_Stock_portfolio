"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from project.models import Stock

def test_new_stock(new_stock):
    """
    GIVEN a Stock model
    WHEN a new Stock object is created
    THEN check the symbol, number of shares, and purchase price fields are defined correctly
    """
    assert new_stock.stock_symbol == 'BTC'
    assert new_stock.number_of_shares == 10
    assert new_stock.purchase_price == 1500000