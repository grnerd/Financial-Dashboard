from nselib import capital_market as cm
import nselib as nl


holiday = nl.trading_holiday_calendar()

#print(holiday)

total_equity = cm.bhav_copy_equities('1-3-2024')
print(total_equity)

stock = cm.deliverable_position_data('ITC', period='1W')
print(stock)

