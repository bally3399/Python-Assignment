class BackToSender:
    def percentage_rate(self, number_of_parcel_delivered):
        number_of_packages_assigned_daily = 100
        rate = (number_of_parcel_delivered / number_of_packages_assigned_daily) * 100
        return rate

    def calculate_daily_wage(self, percentage_rate):
        if percentage_rate < 0 or percentage_rate > 100:
            raise ValueError("Input invalid")
        if percentage_rate > 0 and percentage_rate < 50:
            return self.get_daily_wage(percentage_rate, 160)
        elif percentage_rate > 50 and percentage_rate <= 59:
            return self.get_daily_wage(percentage_rate,200)
        elif percentage_rate > 59 and percentage_rate <= 69:
            return self.get_daily_wage(percentage_rate, 250)
        elif percentage_rate >= 70:
            return self.get_daily_wage(percentage_rate, 500)

    def get_daily_wage(self, percentage_rate, amount_per_parcel):
        base_pay = 5000
        return percentage_rate * amount_per_parcel + base_pay