from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go(input("Ban muon di dau ?"))
        bot.select_dates(check_in_date=input("Ngay nhan phong la gi ?"),
                         check_out_date=input("Ngay tra phong la gi ?"))
        bot.select_adults(int(input("Bao nhieu nguoi ?")))
        bot.click_search()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise