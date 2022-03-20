import PySimpleGUI as sg
import datetime
import calendar
import config
from pyowm.owm import OWM


class GUI:
    def __init__(self):
        self.blink_count = 0

        sg.set_options(border_width=0, text_color='white',
                       background_color='black', text_element_background_color='black')

        # Create clock layout
        clock = [[sg.Text('', pad=(0, config.screen_height/6)),
             sg.Image(data=config.ledblank[22:], key='-hour1-'),
             sg.Image(data=config.ledblank[22:], key='-hour2-'),
             sg.Image(data=config.ledblank[22:], key='-colon-'),
             sg.Image(data=config.ledblank[22:], key='-min1-'),
             sg.Image(data=config.ledblank[22:], key='-min2-')],]

        # Create the weather columns layout
        weather_cols = []
        for i in range(config.num_days_forecast):
            weather_cols.append(
                [[sg.Text('', size=(4, 1), font='Any 20',
                          justification='center', key='-DAY-' + str(i)), ],
                 [sg.Image(data=config.w1[22:], background_color='black',
                           key='-icon-' + str(i), pad=((4, 0), 3)), ],
                 [sg.Text('--', size=(3, 1), justification='center',
                          font='Any 20', key='-high-' + str(i), pad=((10, 0), 3))],
                 [sg.Text('--', size=(3, 1), justification='center',
                          font='Any 20', key='-low-' + str(i), pad=((10, 0), 3))]])

        # Create the overall layout
        layout = [[sg.Col(clock, background_color='black')],
                  [sg.Col(weather_cols[x], background_color='black')
                   for x in range(config.num_days_forecast)]]

        # Create the window
        self.window = sg.Window(f"{config.pet_name}'s App ", layout, finalize=True,
                                background_color='black', use_default_focus=False, no_titlebar=True, keep_on_top=True,
                                location=(0, 0), size=(config.screen_width, config.screen_height), element_justification='c')

        self.colon_elem = self.window['-colon-']
        self.hour1 = self.window['-hour1-']
        self.hour2 = self.window['-hour2-']
        self.min1 = self.window['-min1-']
        self.min2 = self.window['-min2-']

    def update_clock(self):
        # update the clock
        now = datetime.datetime.now()
        real_hour = now.hour - 12 if now.hour > 12 else now.hour
        hour1_digit = config.led_digits[real_hour // 10]
        self.hour1.update(data=hour1_digit[22:])
        self.hour2.update(data=config.led_digits[real_hour % 10][22:])
        self.min2.update(data=config.led_digits[int(now.minute) % 10][22:])
        self.min1.update(data=config.led_digits[int(now.minute) // 10][22:])
        # Blink the :
        if self.blink_count % 2:
            self.colon_elem.update(data=config.ledcolon[22:])
        else:
            self.colon_elem.update(data=config.ledblank[22:])
        self.blink_count += 1

    def update_weather(self):
        owm = OWM(config.owm_api_key)
        mgr = owm.weather_manager()
        one_call = mgr.one_call(lat=config.latitude, lon=config.longitude, units=config.units)
        daily_forecast = one_call.forecast_daily

        today_weekday = datetime.datetime.today().weekday()

        daily_icons = []
        max_temps = []
        min_temps = []
        for day in range(0, config.num_days_forecast):
            daily_data = daily_forecast[day]

            daily_icons.append(daily_data.status)
            max_temps.append(int(daily_data.temp.get('max')))
            min_temps.append(int(daily_data.temp.get('min')))

            day_element = self.window['-DAY-' + str(day)]
            max_element = self.window['-high-' + str(day)]
            min_element = self.window['-low-' + str(day)]
            icon_element = self.window['-icon-' + str(day)]
            day_element.update(calendar.day_abbr[(today_weekday + day) % 7])
            max_element.update(max_temps[day])
            min_element.update(min_temps[day])
            icon_element.update(data=config.weather_icon_dict[daily_icons[day]][22:])


def led_clock():
    # Get the GUI object that is used to update the window
    gui = GUI()

    # ---------- EVENT LOOP ----------
    last_update_time = 0
    while True:
        # Wake up once a second to update the clock and weather
        event, values = gui.window.read(timeout=1000)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # update clock
        gui.update_clock()
        # update weather once ever 6 hours
        now = datetime.datetime.now()
        if last_update_time == 0 or (now - last_update_time).seconds >= config.weather_update_frequency:
            print('*** Updating Weather ***')
            last_update_time = now
            gui.update_weather()


if __name__ == '__main__':
    led_clock()
