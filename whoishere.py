
import json
import urllib.request as ur

READ_API_KEY='F4OA1IJI4U0BMH3E'
CHANNEL_ID='420847'
def main():
    conn = ur.urlopen("http://api.thingspeak.com/channels/" + CHANNEL_ID + "/feeds/last.json?api_key=" + READ_API_KEY)
    response = conn.read()
    data=json.loads(response)
    #print data['field2'] #Works in command line. Try 'return' for web
    return data['field2']
    conn.close()
if __name__ == '__main__':
    main()

	
	



