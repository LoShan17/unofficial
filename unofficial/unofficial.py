
import csv
import requests
import random

from data_reference import CASH_FLOWS_STATEMENT, INCOME_STATEMENT, BALANCE_SHEET_STATEMENT, GET_TIMERANGE

# key ratios example
# http://financials.morningstar.com/ajax/exportKR2CSV.html?t=FB

# detailed table example
# http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=TWTR&reportType=is&period=12&dataType=A&order=asc&columnYear=5&number=3

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
        self.local_storage = {}

    def get_ratios_summary(t, region):
        """
        Get request for the ratio summary csv
        """
        # design attempt not super sure about this
        func_params = locals()

        self.current_query = {KeyRatiosSummary : func_params}
        response = requests.get(KeyRatioSummary, params=func_params)
        if response.ok:
            self.current_response_text = response.text
        else:
            self.current_response_text = None
            ## could use warnings here instead of this
            print("Error executing request: " + response.reason)

    def last_response_csv_dump(self, outpath):
        """
        dump the result of the last request to the API
        in a csv file in the specified file
        """
        # find a way to properly output this
        with open(outpath, 'w') as csvFile:
            writer = csv.writer(csvFile, delimiter=',')
            for line in data.split('\n'):
                writer.writerow(line.split(','))

    def last_response_to_json(self):
        """
        return a json from the last received csv table
        """
        pass

    def get_table(self, **kwargs):
        """
        Standard Get request to get the requested financial summary
        parameters for the request are:
        -
        - 
        """
        self.current_query = kwargs
        pass

    def pp_last_request(self):
        """
        pretty print to the terminal the test from the 
        last received csv
        """
        pass



