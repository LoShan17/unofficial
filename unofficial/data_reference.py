
import os
import datetime as dt

USER_DIR = os.path.expanduser("~")
#DATABASE_LOCATION = os.path.join(USER_DIR, 'unofficial_data')
DATABASE_LOCATION = os.path.join('S:', os.path.sep, 'ETF', 'Daniel', 'Spread_Monitoring', 'unofficial_data')

today = dt.datetime.now().date()
TODAY_STR = today.strftime("%d/%m/%Y") 

class KeyRatiosSummary(object):
    address = 'http://financials.morningstar.com/ajax/exportKR2CSV.html'
    csv_name = 'KeyRatios'

class FinancialStatement(object):
    address = 'http://financials.morningstar.com/ajax/ReportProcess4CSV.html'
    csv_name = 'Statement'

CASH_FLOWS_STATEMENT = 'cf'
INCOME_STATEMENT = 'is'
BALANCE_SHEET_STATEMENT = 'bs'
_AVAILABLE_RANGES = [3, 6, 9, 12]

def GET_TIMERANGE(months_range):
    
    if months_range not in _AVAILABLE_RANGES:
        raise WrongQueryParameterException("months_range must be one of :" + str(_AVAILABLE_RANGES))
