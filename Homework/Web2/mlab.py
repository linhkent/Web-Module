import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds331135.mlab.com:31135/bike

host = "ds331135.mlab.com"
port = 31135
db_name = "bike"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())