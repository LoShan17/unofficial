
CASH_FLOWS_STATEMENT = 'cf'
INCOME_STATEMENT = 'is'
BALANCE_SHEET_STATEMENT = 'bs'
AVAILABLE_RANGES = [3, 6, 9, 12]

def GET_TIMERANGE(months_range):
    
    if months_range not in AVAILABLE_RANGES:
        raise WrongQueryParameterException("months_range must be one of :" + str(AVAILABLE_RANGES))
