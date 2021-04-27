from datetime import date


class DifferenceDate:
    days = 0
    weeks = 0
    months = 0
    years = 0


class DateDifference:
    """
    Find difference between two dates in terms
    of years, months, weeks, days
    """
    month_numbers = {'january': 1, 'jan': 1, 'february': 2, 'feb': 2, 'march': 3, 'mar': 3, 'april': 4, 'apr': 4,
                     'may': 5, 'june': 6, 'jun': 6, 'july': 7, 'jul': 7, 'august': 8, 'aug': 8, 'september': 9,
                     'sept': 9, 'sep': 9, 'october': 10, 'oct': 10, 'november': 11, 'nov': 11, 'december': 12, 'dec': 12
                     }
    "possible month names into their respective numbers"

    def __init__(self):
        """Find difference between two dates"""
        self.difference_date = DifferenceDate()

    def find_difference(self, from_date: str, to_date: str) -> DifferenceDate:
        """
        Finds difference between `from_date` and `to_date` in terms
        of years, months, weeks, days
        Both the parameters should be one of the following forms:
            'yyyy-mm-dd' or 'yyyy-month_name-dd' or 'yyyy-m-d'

        :param from_date: date from which difference is to be calculated
        :param to_date: date upto which difference is to be calculated
        :return:
        """
        from_date = from_date.split('-') if '-' in from_date else from_date.split('/') if '/' in from_date else \
            from_date.split()
        to_date = to_date.split('-') if '-' in to_date else to_date.split('/') if '/' in to_date else to_date.split()

        if from_date[1].lower() in list(self.month_numbers.keys()):
            from_date[1] = self.month_numbers[from_date[1].lower()]

        if to_date[1].lower() in list(self.month_numbers.keys()):
            to_date[1] = self.month_numbers[to_date[1].lower()]

        if 0 > int(from_date[1]) > 12:
            raise ValueError('Month should be greater than 0 and less than 12 (0 < month < 12)')
        elif 0 > int(from_date[2]) > 31:
            raise ValueError('Day should be greater than 0 and less than 31 (0 < day < 31)')

        f_date = date(int(from_date[0]), int(from_date[1]), int(from_date[2]))
        t_date = date(int(to_date[0]), int(to_date[1]), int(to_date[2]))
        delta = abs(f_date - t_date)
        self.difference_date.days = delta.days
        self.difference_date.weeks = delta.days // 7
        self.difference_date.months = delta.days // 30
        self.difference_date.years = delta.days // 365
        return self.difference_date

    def add_to_date(self, _date: str, years: int = 0, months: int = 0, days: int = 0):
        pass

    def subtract_from_date(self, _date: str, years: int = 0, months: int = 0, days: int = 0):
        pass


if __name__ == '__main__':
    datediff = DateDifference()
    difference = datediff.find_difference('2000 April 20', '2000 Apr 20')
    print('days:', difference.days)
    print('months:', difference.months)
    print('weeks:', difference.weeks)
    print('years:', difference.years)
