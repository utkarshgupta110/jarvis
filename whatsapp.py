import pywhatkit

def send_msg(command):
    msg = command
    pywhatkit.sendwhatmsg_instantly(
    "+916307239024",
    msg,
    wait_time=10,
    tab_close=True
)