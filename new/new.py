
from flask import Flask

from pylexa.app import alexa_blueprint
from pylexa.intent import handle_intent
from pylexa.response import PlainTextSpeech

import urllib2,json

app = Flask(__name__)
app.config['app_id'] = 'amzn1.ask.skill.858f0ecb-96b1-436c-9ce6-01f5e3fef821'
app.register_blueprint(alexa_blueprint)


@handle_intent('WhoIsInTheHouse')
def handle_WhoIsInTheHouse_intent(request):
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/" + CHANNEL_ID + "/feeds/last.json?api_key=" + READ_API_KEY)
    response = conn.read()
    data=json.loads(response)
    print (data['field2']) #print works fine when tested in IDLE.
    conn.close()
    return PlainTextSpeech(request.slots.get(data['field2'], 'Nothing to echo'))
