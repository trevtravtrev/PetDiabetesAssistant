"""
/////////////////////////////
General Settings
/////////////////////////////
"""
# your pet's name :)
pet_name = 'mypet'


"""
/////////////////////////////
Alarm Settings
/////////////////////////////
"""
# ** cannot have same times for food and medicine
# food alarm times (24 hour format, military time)
food_alarm_times = ['8:57', '20:57']
# medicine alarm times (24 hour format, military time)
medicine_alarm_times = ['9.27', '21:27']


"""
/////////////////////////////
Alarm Safety Settings
/////////////////////////////
"""
# time in seconds, if alarm has not been deactivated, starts louder alarm sound
critical_alarm_sound_timer = 5*60
# time in seconds, if alarm has not been deactivated, sends out critical notifications to text/email
critical_alarm_notification_timer = 7*60


"""
/////////////////////////////
Sound Settings
/////////////////////////////
"""
# string, alarm audio file path to play before medicine_audio_prompt text to speech
medicine_audio_chime = 'medicine.wav'
# string, text to speech string to be spoken after medicine_audio_chime
medicine_audio_prompt = f"Time for {pet_name}'s medicine!"

# string, alarm audio file path to play before food_audio_prompt text to speech
food_audio_chime = 'food.wav'
# string, text to speech string to be spoken after food_audio_chime
food_audio_prompt = f'Time for {pet_name} to eat!'


"""
/////////////////////////////
Notification Text/Email Sender Settings
/////////////////////////////
"""
# email accounts are used to send both text and email notifications to numbers/emails specified in receive settings
# ********** ENSURE EMAIL ACCOUNTS ARE SET TO ALLOW 3RD PARTY APPS **********
# main email credentials to use for sending notifications
main_email = 'example@gmail.com'
main_email_password = 'password1234'
main_email_domain = 'smtp.gmail.com'
main_email_port = 587

# backup email credentials for redundancy to use for sending notifications
use_backup_email = True
backup_email = 'example2@gmail.com'
backup_email_password = 'password1234'
backup_email_domain = 'smtp.gmail.com'
backup_email_port = 587


"""
/////////////////////////////
Notification Text/Email Receiver Settings
/////////////////////////////
"""
# dictionary (yournumber:yourcarrier), phone numbers and supported phone carrier option to receive text notifications
phone_numbers = {
    0000000000: 'att',
    1111111111: 'tmobile',
    2222222222: 'verizon',
    3333333333: 'sprint',
    4444444444: 'virgin',
    5555555555: 'boost',
    6666666666: 'cricket',
    7777777777: 'metro',
    8888888888: 'us cellular',
    9999999999: 'xfinity'
}
# list, email addresses for email notifications to be sent to
email_addresses = ['email1@gmail.com', 'email2@gmail.com', 'email3@gmail.com']


"""
/////////////////////////////
Notification Message Settings
/////////////////////////////
"""
# string to be sent as sms and email notifications
sms_email_food_message = f'Warning: {pet_name} is overdue for food!'
sms_email_medicine_message = f'Warning: {pet_name} is overdue for medicine!'
