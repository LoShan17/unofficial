
import csv
import requests
import os
import datetime as dt

from data_reference import DATABASE_LOCATION, KeyRatiosSummary, FinancialStatement, StatementsParams

# key ratios example
# http://financials.morningstar.com/ajax/exportKR2CSV.html?t=FB

# detailed table example
# http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=TWTR&reportType=is&period=12&dataType=A&order=asc&columnYear=5&number=3

# historical quotes
# http://globalquote.morningstar.com/globalcomponent/RealtimeHistoricalStockData.ashx?ticker=F&showVol=true&dtype=his&f=d&curry=USD&range=1900-1-1|2014-10-10&isD=true&isS=true&hasF=true&ProdCode=DIRECT

class WrongQueryParameterException(Exception):
    pass

class UnofficialTerminal(object):
    """
    Class that acts as terminal and that performs requests to the API 
    managing and storing the result of responses.
    """

    def __init__(self):
        self.current_data = None
        self.current_query = {}
        self.current_response_text = None
        self.current_parsed_csv = False
        self.local_storage = {}
        self.today = dt.date.today()
        self.today_string = self.today.strftime('%d%m%Y')

    def get_ratios_summary(self, t, region):
        """
        Get request for the ratio summary csv
        """
        func_params = {'t': t, 'region': region}
        self.current_query = func_params
        response = requests.get(KeyRatiosSummary.ADDRESS, params=func_params)
        if response.ok:
            self.current_response_text = response.text.encode('utf-8')
            reader = csv.reader(self.current_response_text.split('\n'))
            self.current_parsed_csv = list(reader)
        else:
            self.current_response_text = None
            self.current_parsed_csv = None
            ## could use warnings here instead of this            
            print("Error executing request: " + response.reason)

    def get_statement(self, t, region, reportType, period, dataType='A', order='asc', columnYear=10, number=3):
        """
        Standard Get request to get the requested financial summary
        parameters for the request that must be specified:
        - t (ticker)
        - region
        - reportType (refer to data_reference)
        - period (refer to data_reference)
        """
        func_params = {'t': t, 'region': region, 'reportType': reportType, 'period': period, 
                       'dataType': dataType, 'order': order, 'columnYear': columnYear, 'number': number}
        self.current_query = func_params
        response = requests.get(FinancialStatement.ADDRESS, func_params)
        if response.ok:
            self.current_response_text = response.text.encode('utf-8')
            reader = csv.reader(self.current_response_text.split('\n'))
            self.current_parsed_csv = list(reader)
        else:
            self.current_response_text = None
            self.current_parsed_csv = None
            ## could use warnings here instead of this            
            print("Error executing request: " + response.reason)

    def last_response_csv_dump(self):
        """
        dump the result of the last request to the API
        in a csv file in the specified file
        """
        if self.current_query and self.current_response_text:
            data = self.current_response_text
            if 'reportType' in self.current_query:
                file_name = (self.current_query['reportType'] + '_' + FinancialStatement.CSV_NAME + 
                            '_' + self.current_query['t'] + '_' + self.current_query['region'] + '_' +
                            str(self.current_query['period']) + 'months_' + self.today_string + '.csv')                
            else:
                file_name = (KeyRatiosSummary.CSV_NAME + '_' + self.current_query['t'] + '_' + 
                            self.current_query['region'] + '_' + self.today_string + '.csv')
            outpath = os.path.join(DATABASE_LOCATION, file_name)
            with open(outpath, 'w') as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                for line in self.current_parsed_csv:
                    writer.writerow(line)
        else:
            print('NO recent query to dump in csv')

    def change_data_dump_location(self, new_path):
        global DATABASE_LOCATION
        try:
            #write a stupid file and delete it
            DATABASE_LOCATION = new_path
        except:
            pass
            # if gives an exception pass the exception along

    def last_response_to_json(self):
        """
        return a json from the last received csv table
        """
        pass

    def pp_last_request(self):
        """
        pretty print to the terminal the test from the 
        last received csv
        """
        pass



