import os
import urllib2,json

from flask import Flask

from pylexa.app import alexa_blueprint
from pylexa.intent import handle_intent
from pylexa.response import PlainTextSpeech


app = Flask(__name__)
app.config['app_id'] = os.getenv('ALEXA_APP_ID')
app.register_blueprint(alexa_blueprint)


@handle_intent('WhoIsInTheHouse')
def handle_echo_intent(request):
    print(request)
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/" + CHANNEL_ID + "/feeds/last.json?api_key=" + READ_API_KEY)
    response = conn.read()
    data=json.loads(response)
    print (data['field2']) #print works fine when tested in IDLE.
    conn.close()
	return PlainTextSpeech(request.slots.get('message', data['field2']))


if __name__ == '__main__':
    app.run(debug=True)
