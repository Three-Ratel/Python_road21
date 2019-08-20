import requests

server_url = 'http://openapi.tuling123.com/openapi/api/v2'

data = {

    "perception": {
        "inputText": {
            "text": "附近的酒店"
        }
    },

    "userInfo": {
        "apiKey": "2213889293634c759484cac88a91c170",
        "userId": "110"
    }
}


def run(txt='你好！'):
    data['perception']['inputText']['text'] = txt
    res = requests.post(server_url, json=data).json().get('results')[0].get('values').get('text')
    print(res)
    return res


if __name__ == '__main__':
    run()
