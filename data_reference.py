
KeyRatiosSummary = 'http://financials.morningstar.com/ajax/exportKR2CSV.html'


CASH_FLOWS_STATEMENT = 'cf'
INCOME_STATEMENT = 'is'
BALANCE_SHEET_STATEMENT = 'bs'
_AVAILABLE_RANGES = [3, 6, 9, 12]

def GET_TIMERANGE(months_range):
    
    if months_range not in _AVAILABLE_RANGES:
        raise WrongQueryParameterException("months_range must be one of :" + str(_AVAILABLE_RANGES))
