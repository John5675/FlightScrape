from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.select_airport("HND")
        bot.select_dates(
            check_in_date="4 December 2023", check_out_date="12 January 2024"
        )
        bot.search_button()

except Exception as e:
    if "in PATH" in str(e):
        print("There is a problem running this program from the command line interface")
    else:
        raise
