import rrb3 as rrb
import websocket
import time
import logging
import sys
import robot_button as button

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

try:
    import thread
except ImportError:
    import _thread as thread

# raspberry pi IP Address
# IP_ADDRESS = sys.argv[1]
BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

# Configure the RRB
rr = rrb.RRB3(BATTERY_VOLTS, MOTOR_VOLTS)

# speed
half_speed = 0.3
back_speed = 0.2


def command(ws, message):
    if ',' in message:
        message = message.split(',')[1].replace('"', '').replace(']', '')
    
    if message == 'back':
        print('cmd', 'back', message)
        rr.forward(0, back_speed)

    elif message == 'right':
        print('cmd', 'right', message)
        rr.left(1.0, half_speed)

    elif message == 'left':
        print('cmd', 'left', message)
        rr.right(1.0, half_speed)

    elif message == 'stop':
        print('cmd', 'stop', message)
        rr.stop()
        ws.close()

    else:
        print('cmd', 'forward', message)
        rr.reverse(0, half_speed)


def on_message(ws, message):
    command(ws, message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print('### closed ###')


def on_open(ws):
    def run(*args):
        while True:
            time.sleep(20)
        ws.close()
        print('thread terminating...')
    thread.start_new_thread(run, ())

    
def main():
    websocket.enableTrace(True)
    url = 'wss://suika-terrasky.herokuapp.com/socket.io/?EIO=3&transport=websocket'
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    # if rr.sw1_closed() == False:
    #     rr.stop()
    #     ws.close()
    #     button.main()
    ws.on_open = on_open
    
    try:
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()


if __name__ == '__main__':
    main()

