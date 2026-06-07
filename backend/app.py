from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'status': 'ok', 'service': '工单智能校核系统-后端'})


@app.route('/api/audit', methods=['POST'])
def audit():
    """校核工单接口"""
    data = request.get_json()
    # TODO: 语义分析与双智能体推理
    return jsonify({'code': 0, 'msg': '待实现'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
