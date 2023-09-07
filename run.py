from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.select_airport("HND")

        check_in_date = "1 April 2024"
        check_out_date = "15 April 2024"

        for _ in range(15):
            bot.select_dates(check_in_date, check_out_date)
            bot.search_button()
            bot.report_results()
            check_in_date, check_out_date = bot.increment_date_and_search(
                check_in_date, check_out_date
            )
        bot.get_report_list()
except Exception as e:
    if "in PATH" in str(e):
        print("There is a problem running this program from the command line interface")
    else:
        raise
