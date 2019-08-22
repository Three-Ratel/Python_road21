"""
使用redis，用于存储 app 和 toy 未读的聊天记录条数
1. set_msg: 用户发送语音消息时，toy 为接收的消息数量
2. get_msg: toy 获取未读语音消息时，清空计数器
3. get_msg_count: 用于app端获取未读消息的条数
"""

import json

from config import RDB


def set_msg(sender, receiver):
    msg_count = RDB.get(receiver)
    # print(msg_count)
    if msg_count:
        msg_dict = json.loads(msg_count)
        if msg_dict.get(sender):
            msg_dict[sender] += 1
        else:
            msg_dict[sender] = 1
    else:
        msg_dict = {sender: 1}
    # print(msg_dict)
    RDB.set(receiver, json.dumps(msg_dict))


def get_msg(sender, receiver):
    msg_count = RDB.get(receiver)
    count = 0
    msg_dict = {'count': 0}

    if msg_count:
        msg_dict = json.loads(msg_count)
        count = msg_dict.get(sender, 0)

        if count == 0:
            for sender_id, chat_count in msg_dict.items():
                if chat_count != 0:
                    sender = sender_id
                    count = chat_count
                    break

    msg_dict[sender] = 0
    RDB.set(receiver, json.dumps(msg_dict))
    return count, sender


def get_msg_count(receiver):
    chat_dict = RDB.get(receiver)
    count = 0
    if chat_dict:
        chat_dict = json.loads(chat_dict)
        count = sum(chat_dict.values())
    else:
        chat_dict = {}
    chat_dict['count'] = count
    return chat_dict
