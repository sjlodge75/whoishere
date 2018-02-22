import urllib2,json

READ_API_KEY='F4OA1IJI4U0BMH3E'
CHANNEL_ID='420847'
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
           'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(speechlet_response):
    return {
        'version': '1.0',
        'response': speechlet_response
    }

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """
    print("Started")
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("Launch")
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def get_welcome_response():
    print("WelcomeResponse")
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Jon, Liz and Phil are here in the house"
    should_end_session = True
    return build_response(build_speechlet_response(
 card_title, speech_output, None, should_end_session))

def on_intent(intent_request, session):
    print("onIntent")
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "WhoIsInTheHouse":
        return run_thingspeak(intent, session, link)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# --------------- Functions that control the skill's behavior ------------------

def handle_session_end_request():
    print("SessionEnded")
    card_title = "Session Ended"
    speech_output = "I hope you haven't lost anyone."
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# Run the Thingspeak connection and reply
def run_thingspeak(intent, session, link):
    print("RunThingspeak")
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    
    f = urllib2.urlopen(link) # Get your data
    result = f.read()
    speech_output = result       
       
    return build_response(build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


def main():
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/" + CHANNEL_ID + "/feeds/last.json?api_key=" + READ_API_KEY)
    response = conn.read()
    data=json.loads(response)
    print data['field2'] #print works fine when tested in IDLE. Try 'return' when hosted online
    speech_output = data['field2']
    conn.close()
    return build_response(build_speechlet_response('Welcome',
        speech_output, 'AskMe', should_end_session))

if __name__ == '__main__':
    main()
    speech_output = result       
       
    


 