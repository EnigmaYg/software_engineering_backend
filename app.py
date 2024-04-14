import json

from flask import Flask, request
from static import *
from static.Scheduling import scheduling

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name')  # 获取名为'name'的参数值
    return f'Hello, {name}!' if name else 'Hello, World!'


@app.route('/tourPlan', methods=['GET'])
def travel_planner():
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    # duration = request.args.get('dur')
    begin_date = request.args.get('start_time')

    tp = scheduling(departure, destination, 4, begin_date)

    return json.loads(tp.toJSON())


@app.route('/chat/simpleChat', methods=['POST'])
def simple_chat():
    # data = request.json
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    start_time = request.args.get('start_time')

    tp = scheduling(departure, destination, 4, start_time)
    print(tp)

    return json.loads(tp.toJSON())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091, debug=True)
