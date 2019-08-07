import json

from redis import Redis

redis_cli = Redis(host='192.168.12.9', port=6379, db=6)
# redis_cli = Redis(host='127.0.0.1', port=6379, db=6)

# redis_cli.set('name', 'echo')
#
# res = redis_cli.get('name')
# print(res.decode('utf8'))

info = json.dumps({'name': 'henry', 'age': 18})
redis_cli.set('info', info)
# redis_cli.set('protected-mode', 'no')
res = redis_cli.get('info')
print(json.loads(res))
