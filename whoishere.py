
import urllib2,json
READ_API_KEY='F4OA1IJI4U0BMH3E'
CHANNEL_ID=420847 
def main():
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))
    response = conn.read()
    print "http status code=%s" % (conn.getcode())
    data=json.loads(response)
    print data['field2'],data['created_at']
    conn.close()
if __name__ == '__main__':
    main()
