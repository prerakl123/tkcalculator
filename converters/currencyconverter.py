import os
import requests
import json
import urllib.request
import time
import inspect


class CurrencyConverter:
    """
    Currency converter which converts from one currency to
    another based on the data from `URL` below.
    """
    
    # Constants
    URL = 'https://api.exchangerate-api.com/v4/latest/'
    "URL for getting all the conversion info"
    
    currencies = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN',
                  'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF',
                  'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN',
                  'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD',
                  'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD',
                  'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD',
                  'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN',
                  'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR',
                  'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP',
                  'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD',
                  'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD',
                  'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW']
    "Names of Currencies"
    
    def __init__(self):
        """
        Initialize the converter. Check all the JSON files.
        Connect to `self.URL` and download necessary
        conversion data.
        """
        self.from_currency = ''
        self.to_currency = ''
        self.conversion_dict = dict()
        self.module_folder = os.path.dirname(os.path.abspath(inspect.getsourcefile(self.__class__)))
        self.module_folder = self.module_folder.replace('/', '\\').rstrip('\\')

        # The function below can be called parallel to any other by multiprocessing or threading
        # self.update_currencies()

    def convert(self, amount: float or int, decimals=4) -> float or str:
        """
        Convert `amount` from `from_currency` to `to_currency`

        :param amount: the amount which is to be converted
        :param decimals: decimals upto which amount is to round-offed
        """
        amount = round(amount * self.conversion_dict['rates'][self.to_currency], decimals)
        # limiting the precision to `n` decimal places
        return amount

    def from_json(self, currency) -> dict:
        """
        Can provide currency name or the JSON filename as
        parameter, both are acceptable.

        :param currency: The currency to access the
                         `currency`.json data file.
        """
        try:
            if not currency.endswith('.json'):
                currency += '.json'
            with open(currency, 'r') as file:
                _dict = json.load(file)
            return _dict
        except Exception as e:
            return {'error': e}

        except json.JSONDecodeError as jde_err:
            return {'error': jde_err}

    def get_currencies(self) -> list:
        """
        Get the currently set 'from' and 'to' currencies
        :return: list with 'from' and 'to' currencies
        """
        return [self.from_currency, self.to_currency]

    @staticmethod
    def is_connected() -> bool:
        """
        Check if internet is connected. By simply trying to
        open `google.com`.
        
        :returns: True if url opened without error else False
        """
        try:
            urllib.request.urlopen('http://www.google.com')
            return True
        except:
            return False

    def set_currencies(self, from_currency: str = None, to_currency: str = None):
        """
        Set the 'from' and 'to' currencies and load the JSON file of
        the 'from' currency.

        :param from_currency: the currency from which amount is to be converted
        :param to_currency: the currency in which amonut is to be converted
        :return: None
        """
        if from_currency:
            self.from_currency = from_currency
        if to_currency:
            self.to_currency = to_currency
        with open(f'{self.module_folder}\\currencies\\{from_currency}.json', 'r') as file:
            self.conversion_dict = json.load(file)

    def to_json(self, data: dict, name: str = None) -> bool:
        """
        Writes `data` dictionary to JSON file of `name`.

        :param data: the data dictionary
        :param name: Optional: name of the JSON file
        :param folder: name of the folder containing JSON files for conversions
        :returns: True if file.write() successful else False
        """
        try:
            if name:
                if not name.endswith('.json'):
                    name += '.json'
            else:
                name = data['base'] + '.json'
            json_object = json.dumps(data, indent=4)
            with open(f"{self.module_folder}\\currencies\\{name}", 'w') as file:
                file.write(json_object)
                file.close()
            return True

        except KeyError or ValueError as kv_err:
            print(kv_err)
            return False

        except json.JSONDecodeError as jde_err:
            print(jde_err)
            return False

        except Exception as e:
            print(e)
            return False

    def update_currencies(self):
        """
        Updates the current value of the currencies as per
        the current date.
        Note: The values are updated once everyday on the website
        :return: None
        """
        today = time.localtime()
        if len(str(today.tm_mday)) < 2:
            today = f"{today.tm_year}-{today.tm_mon}-0{today.tm_mday}"
        elif len(str(today.tm_mon)) < 2:
            today = f"{today.tm_year}-0{today.tm_mon}-{today.tm_mday}"
        else:
            today = f"{today.tm_year}-{today.tm_mon}-{today.tm_mday}"
        if self.is_connected():
            for cur in self.currencies:
                with open(f'{self.module_folder}\\currencies\\{cur}.json', 'r') as file:
                    dict_ = json.load(file)
                    if dict_['date'] == today:
                        pass
                    else:
                        data = requests.get(self.URL + cur).json()
                        self.to_json(data, name=cur)
        else:
            raise ConnectionError('No Internet Connection found. Currencies cannot be updated to the latest values.')


if __name__ == '__main__':
    converter = CurrencyConverter()
    converter.set_currencies('INR', 'USD')
    print(converter.convert(74.82, 5))
    # s = open(converter.module_folder + '\\currencies\\INR.json')
    # print(s.read())
    converter.update_currencies()
