import json

from config import RDB


def set_msg(sender, receiver):
    msg_count = RDB.get(receiver)
    if msg_count:
        msg_dict = json.loads(msg_count)
        if msg_dict.get(sender):
            msg_dict[sender] += 1
        else:
            msg_dict = {sender: 1}
    else:
        msg_dict = {sender: 1}

    RDB.set(receiver, json.dumps(msg_dict))


def get_msg(sender, receiver):
    msg_count = RDB.get(receiver)
    if msg_count:
        msg_dict = json.loads(msg_count)
        count = msg_dict.get(sender, 0)
        msg_dict[sender] = 0
        RDB.set(receiver, json.dumps(msg_dict))
        print(msg_dict)
    else:
        count = 0
    print(count)
    return count
