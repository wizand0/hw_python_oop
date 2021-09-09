import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, rec):
        self.records.append(rec)

    def get_today_stats(self):
        today = dt.date.today()
        stats = 0
        for rec in self.records:
            if rec.date == today:
                stats += rec.amount
        return stats

    def get_week_stats(self):
        today = dt.date.today()
        delta = dt.timedelta(weeks=1)
        week_ago = today - delta
        stats = 0
        for rec in self.records:
            if rec.date <= today and rec.date >= week_ago:
                stats += rec.amount
        return stats


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
        calories_remained = int(self.limit - self.get_today_stats())
        if calories_remained > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с '
                    f'общей калорийностью не более {calories_remained} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):

    USD_RATE = 74.74
    EURO_RATE = 88.09

    def get_today_cash_remained(self, currency):
        cash_remained = round(float(self.limit - self.get_today_stats()), 2)
        if cash_remained == 0:
            return 'Денег нет, держись'
        else:
            if currency == 'USD' or currency == 'usd' or currency == 'Usd':
                cash_remained = round(cash_remained / self.USD_RATE, 2)
                if cash_remained > 0.00:
                    return f'На сегодня осталось {cash_remained} USD'
                else:
                    cash_remained = abs(cash_remained)
                    return f'Денег нет, держись: твой долг - {cash_remained} USD'
            elif currency == 'Euro' or currency == 'euro' or currency == 'eur':
                cash_remained = round(cash_remained / self.EURO_RATE, 2)
                if cash_remained > 0.00:
                    return f'На сегодня осталось {cash_remained} Euro'
                else:
                    cash_remained = abs(cash_remained)
                    return f'Денег нет, держись: твой долг - {cash_remained} Euro'
            
            elif currency == 'Rub' or currency == 'rub' or currency == 'руб':
                cash_remained = round(cash_remained, 2)
                if cash_remained > 0:
                    return f'На сегодня осталось {cash_remained} руб'
                else:
                    cash_remained = abs(cash_remained)
                    return f'Денег нет, держись: твой долг - {cash_remained} руб'
            else:
                return 'Ошибка в выборе валюты'