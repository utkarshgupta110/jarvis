import pywhatkit

def send_msg(command):
    msg = command
    pywhatkit.sendwhatmsg_instantly(
    "+916307XXXXXX",
    msg,
    wait_time=10,
    tab_close=True
)