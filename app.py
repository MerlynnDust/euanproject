from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
app = Flask(__name__)

database1 = {}

@app.route('/ip')
def front_page(name=None):
    return render_template('front_page.html', name=name)

@app.route('/ip', methods=["POST"])
def hello_world():
    ip_text = request.form['IP']
    reason_text = request.form['Reason']
    duration_text = request.form['Duration']

    return render_template('form_submitted.html',ip_text=ip_text,reason_text=reason_text,duration_text=duration_text)

@app.route("/check_ip", methods=["GET"])
def get_my_ip():
    if request.remote_addr in database1:
        return jsonify({'ip': request.remote_addr,'reason':})
    else

    return jsonify({'ip': request.remote_addr}), 200

if __name__ == '__main__':
    app.run()



