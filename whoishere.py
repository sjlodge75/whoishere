
import urllib,json

READ_API_KEY='F4OA1IJI4U0BMH3E'
CHANNEL_ID=420847 
def main():
    conn = urllib.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))
    response = conn.read()
    data=json.loads(response)
    print data['field2'] #Works in command line. Try 'return' for web
    #return data['field2']
    conn.close()
if __name__ == '__main__':
    main()
