import threading
cv = threading.Condition()

class Messenger:
    message = {"a": "b"}
    listened = {"a": []}

def __make_setup(channel):
    if channel not in Messenger.message:
        Messenger.message[channel] = ""
    if channel not in Messenger.listened:
        Messenger.listened[channel] = []

def new_msg(message,channel):
    """
        Send a message to all users that have received a livestream with the "channel" value.  
    """
    __make_setup(channel)
    cv.acquire()

    Messenger.message[channel] = message
    Messenger.listened[channel] = []

    cv.notify_all()
    cv.release()

def answer(channel):
    """
        Create a generator to make a livestream through Flask.  
        Generators with matching "channel" input will receive the same messages.
    """
    __make_setup(channel)
    while True:
        cv.acquire()

        while threading.current_thread() in Messenger.listened[channel]:
            cv.wait()

        important_message = Messenger.message[channel]
        Messenger.listened[channel].append(threading.current_thread())
        cv.release()

        yield f'data: {important_message} \n\n'
        