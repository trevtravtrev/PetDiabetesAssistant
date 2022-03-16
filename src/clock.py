import config
from datetime import datetime
from time import sleep


def get_current_time():
    now = datetime.now()
    return now


def convert_time_to_string(current_time):
    """
    Convert datetime time object into displayable time string in hours:minutes format
    :param current_time: datetime object, current time
    :return: displayable time string in hours:minutes format
    """
    return current_time.strftime("%H:%M")


def check_alarms(current_time):
    """
    Check if any alarm times match with current time.
    *** Cannot have the same times in medicine_alarm_times and food_alarm_times. If so, medicine alarms will take
    *** priority and same time food alarm will not be triggered.
    :param current_time: current time
    :param food_alarm_times: list of food alarms set in config.py
    :param medicine_alarm_times: list of medicine alarms set in config.py
    :return: if an alarm matches current_time return list [alarm_type, alarm_time], else False
    """
    for medicine_time in config.medicine_alarm_times:
        if medicine_time == current_time:
            return ["medicine", medicine_time]
    for food_time in config.food_alarm_times:
        if food_time == current_time:
            return ["food", food_time]
    return False


def get_seconds_passed(previous_time, current_time):
    time_passed = current_time - previous_time
    return int(time_passed.total_seconds())


if __name__ == '__main__':
    start_time = get_current_time()
    sleep(5)
    current_time = get_current_time()
    print(get_seconds_passed(start_time, current_time))
