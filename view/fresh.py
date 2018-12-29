# -*- coding: utf-8 -*-
from flask import jsonify, request
from core import app
from config import Config



@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/tms/syncCollectionStatus/')
def sync_status():
    response = {
        "msg": "成功",
        "success": "true"
    }
    return jsonify(response)


@app.route('/api/tms/decrypt/')
def decrypt():
    response = {
        "msg": "成功",
        "success": "true",
        "data": "15210910321"
    }

    return jsonify(response)


@app.route('/api/tms/collectionStatus/')
def get_status():
    response = {
        "msg": "成功",
        "success": "true",
        "status": 1
    }
    return jsonify(response)


@app.route('/api/tms/collection/')
def get_detail():
    collection_id = request.args.get('collectionId')
    config = Config()
    result = config.fresh_detail
    result['data']['collectionId'] = collection_id
    result['data']['orderItems'][0]['orderId'] = '6' + str(int(time.time()))
    result['data']['orderItems'][1]['orderId'] = '7' + str(int(time.time()))

    return jsonify(result)