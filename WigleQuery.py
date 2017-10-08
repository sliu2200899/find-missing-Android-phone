#curl -X GET --header 'Accept: application/json' --header 'Authorization: Basic QUlEMDY1NzRkY2I0NjU5ZmJhZTUwY2RhNDRhZGQ0ODk0YjI6YjQ1MTEzN2ZkZWQ4MDg5MzdlYTIwMTNjNGRkNzFjZTc=' 'https://api.wigle.net/api/v2/network/detail?netid=9c%3A1c%3A12%3Ab6%3Ad4%3A81'
import json, requests
#from checkMail import Mail
import time



def queryWigle(bssid):
    url = 'https://api.wigle.net/api/v2/network/detail'
    headers = {'Accept': 'application/json',
    'Authorization': 'Basic QUlEMDY1NzRkY2I0NjU5ZmJhZTUwY2RhNDRhZGQ0ODk0YjI6YjQ1MTEzN2ZkZWQ4MDg5MzdlYTIwMTNjNGRkNzFjZTc='}
    params = dict(netid=bssid)

    resp = requests.get(url=url, params=params, headers=headers)
    print(resp)
    data = json.loads(resp.text)
    #print(data['results'])
    results = data['results']
    print('ssid: '+results[0]['ssid'])
    Long = results[0]['locationData'][0]['longitude']
    Lat = results[0]['locationData'][0]['latitude']
    strLong = '{:.8f}'.format(Long)
    strLat = '{:.8f}'.format(Lat)
    print('Longtitude: '+strLong)
    print('Latitude: '+strLat)
    #print(results[0]['latitude'])
    #for item in data['results']:
    #    print(item)

test_id = [' ' for i in range(0,8)]
test_id[0] = '04:bd:88:37:00:03';# ini
test_id[1] = '40:e3:d6:da:c0:03' # cic
test_id[2] = '00:1a:1e:8c:f6:41'
test_id[3] = '18:64:72:62:d6:23'
test_id[4] = '40:e3:d6:f3:e3:33'
test_id[5] = '00:1a:1e:87:3a:c1'
test_id[6] = '9c:1c:12:da:15:83'
test_id[7] = 'a8:bd:27:49:f1:c3'

for i in range(0,len(test_id)):
    queryWigle(test_id[i])


'''
{
  "gsm": false,
  "wifi": true,
  "success": true,
  "cdma": false,
  "results": [
    {
      "trilat": 40.44612122,
      "trilong": -79.94796753,
      "ssid": "CMU-SECURE",
      "qos": 0,
      "transid": "20161021-00490",
      "firsttime": "2016-10-22T01:23:41.000Z",
      "lasttime": "2016-10-21T22:29:03.000Z",
      "lastupdt": "2016-10-21T22:29:07.000Z",
      "housenumber": null,
      "road": null,
      "city": null,
      "region": null,
      "country": null,
      "netid": "9C:1C:12:B6:D4:81",
      "name": null,
      "type": "infra",
      "comment": null,
      "wep": "2",
      "channel": 6,
      "bcninterval": 0,
      "freenet": "?",
      "dhcp": "?",
      "paynet": "?",
      "userfound": null,
      "locationData": [
        {
          "alt": 253,
          "accuracy": 12,
          "lastupdt": "2016-10-21T22:29:03.000Z",
          "latitude": 40.44612122,
          "longitude": -79.94796753,
          "month": "201610",
          "ssid": "CMU-SECURE",
          "time": "2016-10-22T01:23:41.000Z",
          "signal": -74,
          "name": null,
          "netId": "171644386989185",
          "noise": 0,
          "snr": 0,
          "wep": "2",
          "encryptionValue": "WPA2"
        }
      ],
      "encryption": "wpa2"
    }
  ]
}
'''
