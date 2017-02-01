
import os
import datetime as dt

USER_DIR = os.path.expanduser("~")
#DATABASE_LOCATION = os.path.join(USER_DIR, 'unofficial_data')
DATABASE_LOCATION = os.path.join('S:', os.path.sep, 'ETF', 'Daniel', 'Spread_Monitoring', 'unofficial_data')

today = dt.datetime.now().date()
TODAY_STR = today.strftime("%d/%m/%Y") 

class KeyRatiosSummary(object):
    ADDRESS = 'http://financials.morningstar.com/ajax/exportKR2CSV.html'
    CSV_NAME = 'KeyRatios'

class FinancialStatement(object):
    ADDRESS = 'http://financials.morningstar.com/ajax/ReportProcess4CSV.html'
    CSV_NAME = 'Statement'

class StatementsParams(object):
    CASH_FLOWS_STATEMENT = 'cf'
    INCOME_STATEMENT = 'is'
    BALANCE_SHEET_STATEMENT = 'bs'
    _AVAILABLE_RANGES = [3, 6, 9, 12]
