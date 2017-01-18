
import csv
import requests
import random

from core import WrongQueryParameterException
from data_reference import CASH_FLOWS_STATEMENT, INCOME_STATEMENT, BALANCE_SHEET_STATEMENT, AVAILABLE_RANGES, GET_TIMERANGE

# key ratios example
# http://financials.morningstar.com/ajax/exportKR2CSV.html?t=FB

# detailed table example
# http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=TWTR&reportType=is&period=12&dataType=A&order=asc&columnYear=5&number=3

class WrongQueryParameterException(Exception):
    pass


class UnofficialTerminal(object):

    def __init__():
        self.current_data = None
        self.current_query = {}

    def _build_url():
        pass

    def get_ratios_summary(**kwargs):
        pass

    def get_table(**kwargs):
        self.current_query = kwargs
        pass

    def smart_hacky_get():
        pass

