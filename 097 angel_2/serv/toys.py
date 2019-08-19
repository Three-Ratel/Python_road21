from flask import Blueprint, render_template, request, jsonify

from config import mongo

toys = Blueprint('toys', __name__)

"""返回模拟玩具 web端"""


@toys.route('/web')
def web():
    return render_template('WebToy.html')


@toys.route('/open_toy', methods=['post'])
def open_toy():
    device_key = request.form.get('device_key')
    # print(device_key)


    # 如果没有玩具的二维码，玩具未授权
    ret = {}

    toy = mongo.toys.find_one({'device_key': device_key})
    if toy:
        ret['code'] = 0
        ret['music'] = "Success.mp3"
        ret['toy_id'] = str(toy.get('_id'))
        ret['name'] = str(toy.get('toy_name'))
    else:
        # print(ret)
        device = mongo.devices.find_one({'device_key': device_key})
        if device:
            ret['code'] = 1
            ret['music'] = "Nobind.mp3"
        else:
            # print('玩具未授权', ret)
            ret['code'] = 2
            ret["music"] = "Nolic.mp3"

    return jsonify(ret)
