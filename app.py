# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

# USPTO

from uspto.peds.client import UsptoPatentExaminationDataSystemClient

# Background Process

from rq import Queue
from worker import conn

q = Queue(connection=conn)

from utils import count_words_at_url

result = q.enqueue(count_words_at_url, 'http://heroku.com')

@app.route('/getpatent/', methods=['GET'])
def getpatent():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    client = UsptoPatentExaminationDataSystemClient()

    expression = 'appCustNumber:(157691)'
    result     = client.search(expression)

    # xml = dicttoxml(loads(result))

    return jsonify(result)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, ssl_context='adhoc')
