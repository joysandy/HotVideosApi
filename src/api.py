#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Sandy 2019/8/19
from flask import Flask, abort, request, jsonify

app = Flask(__name__)

# temp data

@app.route('/tiktok_video_list/', methods=['POST'])
def tiktok_video_list():
    if not request.json or 'sec_id' not in request.json or 'unique_id' not in request.json or 'uid' not in request.json:
        abort(400)
    result = {}
    return jsonify({'status': 200, 'result': result})


@app.route('/tiktok_video_detail/', methods=['POST'])
def get_task():
    if not request.args or 'vid' not in request.args:
        # 没有指定id则返回全部
        abort(404)
    result = {}
    return jsonify({'status': 200, 'result': result})


if __name__ == "__main__":
    # set host to 0.0.0.0，any external user can access
    app.run(host="0.0.0.0", port=5000, debug=True)