def month():
    print("the Daily loan")
    print("")
    
    statement = float(input("loan amount: "))
    mon = float(input("month interest rate: "))
    months = int(input("amount of the months: "))
    
    daily_interest_amount = mon / 1600
    payment_of_days = months * 30
    daily_amount = statement * daily_interest_amount / (1 - (1 + daily_interest_amount) ** (-payment_of_days))
    
    print("Daily amount for this loan: " + str(daily_amount))
    
month()
    
    