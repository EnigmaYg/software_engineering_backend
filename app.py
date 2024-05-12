import json

from flask import Flask, request
from static import *
from static.Scheduling import scheduling
from static.Scheduling import modify_switch
from static.some_func import find_numbers_in_order

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

    destination = destination.lower()

    tp = scheduling(departure, destination, 4, start_time)
    print(tp.toJSON())
    with open('plan.txt', 'w') as f:
        json.dump(tp.toJSON(), f, indent=4)
    return json.loads(tp.toJSON())

@app.route('/chat/modify', methods=['POST'])
def modify_chat():
    # data = request.json
    demand = request.args.get('demand')
    plan = request.args.get('demo_plan')

    demand = demand.lower()
    print(demand)
    if 'switch' in demand:
        numbers_found = find_numbers_in_order(demand)
        if len(numbers_found) != 2:
            return None
        int1 = int(numbers_found[0])
        int2 = int(numbers_found[1])
        tp = modify_switch(int1, int2, plan)

    return tp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091, debug=True)
