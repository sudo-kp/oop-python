MONTHS_NUM = 12
DAYS_IN_YEAR_NUM = 365


class Days:
    """Class for storing number of days."""
    def __init__(self, day):
        if not isinstance(day, int):
            raise TypeError("wrong day.")
        self.day = day

    def __neg__(self):
        return Days(-self.day)


class Months:
    """Class for storing number of months."""
    def __init__(self, month):
        if not isinstance(month, int):
            raise TypeError("wrong day.")
        self.month = month

    def __neg__(self):
        return Months(-self.month)


class Years:
    """Class for storing number of years."""
    def __init__(self, year):
        if not isinstance(year, int):
            raise TypeError("wrong day.")
        self.year = year

    def __neg__(self):
        return Years(-self.year)


class Calendar:
    """Class for realization of calendar with fields: day, month and year, also boolean value is the year high.
    Fields are initializing by constructors parameters and year has properties for setting and getting data
    and determining if it is high. Assignment and comparison operators are overloaded."""
    day_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days_number_in_year = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    days_number_in_high_year = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

    def __init__(self, day, month, year):
        if not all(isinstance(date, int) for date in (day, month)):
            raise TypeError("Wrong date type.")
        if not 0 < month <= MONTHS_NUM:
            raise ValueError("Wrong month value.")
        if not 0 < day <= self.day_month.get(month):
            if month == 2 and not 0 < day <= self.day_month.get(month) + 1:
                raise ValueError("Wrong day value.")
        self.__day = day
        self.__month = month
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Wrong year type.")
        if year < 0:
            raise ValueError("Wrong year value.")
        self.__year = year
        if year % 4:
            self.__is_high = False
        elif not year % 100 and year % 400:
            self.__is_high = False
        else:
            self.__is_high = True

    def day_by_number(self, day_in_year):
        if not 0 < day_in_year <= DAYS_IN_YEAR_NUM + int(self.__is_high):
            raise ValueError("Wrong day.")
        days_in_year = self.days_number_in_year if not self.__is_high else self.days_number_in_high_year
        for item in days_in_year[1:]:
            if day_in_year <= item:
                self.__month = days_in_year.index(item)
                break
        self.__day = day_in_year - days_in_year[self.__month - 1]

    def add_days(self, days):
        new_day = self.days_number_in_year[self.__month - 1] + self.__day + days
        while not 0 < new_day <= DAYS_IN_YEAR_NUM + int(self.__is_high):
            if new_day <= 0:
                self.year -= 1
                new_day = DAYS_IN_YEAR_NUM + int(self.__is_high) + new_day
            if new_day > DAYS_IN_YEAR_NUM + int(self.__is_high):
                self.year += 1
                new_day -= DAYS_IN_YEAR_NUM + int(self.__is_high)
        self.day_by_number(new_day)

    def add_month(self, months):
        new_month = self.__month + months
        while not 0 < new_month <= MONTHS_NUM:
            if new_month <= 0:
                self.year -= 1
                new_month = MONTHS_NUM + new_month
            if new_month > 12:
                self.year += 1
                new_month -= MONTHS_NUM
        self.__month = new_month

    def __iadd__(self, other):
        if not isinstance(other, (Days, Months, Years)):
            return NotImplemented
        if isinstance(other, Days):
            self.add_days(other.day)
        if isinstance(other, Months):
            self.add_month(other.month)
        if isinstance(other, Years):
            self.year += other.year
        return self

    def __isub__(self, other):
        self.__iadd__(-other)
        return self

    def __str__(self):
        return f'{self.__day}.{self.__month}.{self.year}'

    def __eq__(self, other):
        if not isinstance(other, Calendar):
            return NotImplemented
        return (self.__day, self.__month, self.year) == (other.__day, other.__month, other.year)

    def __lt__(self, other):
        if self == other:
            return False
        if self.year > other.year:
            return True
        if self.year < other.year:
            return False
        if self.__month > other.__month:
            return True
        if self.__month < other.__month:
            return False
        if self.__day > other.__day:
            return True
        return False

    def __le__(self, other):
        return self < other or self == other

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


def main():
    obj = Calendar(1, 1, 2021)
    print(obj)
    obj -= Days(893)
    print(obj)


if __name__ == '__main__':
    main()
