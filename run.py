from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()

except Exception as e:
    if "in PATH" in str(e):
        print("There is a problem running this program from the command line interface")
    else:
        raise
