import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, rec):
        self.records.append(rec)

    def get_today_stats(self):
        today = dt.date.today()
        return sum(rec.amount for rec in self.records
                   if rec.date == today)

    def get_week_stats(self):
        today = dt.date.today()
        delta = dt.timedelta(weeks=1)
        week_ago = today - delta
        return sum(rec.amount for rec in self.records
                   if week_ago <= rec.date <= today)

    def get_remained(self):
        return self.limit - self.get_today_stats()


class Record:
    def __init__(self, amount=0, comment='', date=None):
        self.amount = float(amount)
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = int(self.get_remained())
        if calories_remained > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с '
                    f'общей калорийностью не более {calories_remained} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):

    USD_RATE = 74.74
    EURO_RATE = 88.09
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        cash_remained = self.get_remained()
        if cash_remained == 0:
            return 'Денег нет, держись'
        money_dict = {'usd': ('USD', self.USD_RATE),
                      'eur': ('Euro', self.EURO_RATE),
                      'rub': ('руб', self.RUB_RATE)
                      }
        if currency not in money_dict:
            return 'Введите правильную валюту'
        name, rate = money_dict.get(currency)
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            return f'На сегодня осталось {cash_remained} {name}'
        else:
            cash_remained = abs(cash_remained)
            return ('Денег нет, держись: твой долг '
                    f'- {cash_remained} {name}')
