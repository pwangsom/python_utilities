import hashlib
import hmac
import json
import time
import requests
import requests_to_curl

def gen_sign(api_secret, payload_string=None):
    return hmac.new(api_secret.encode('utf-8'), payload_string.encode('utf-8'), hashlib.sha256).hexdigest()

def gen_query_param(url, query_param):
    req = requests.PreparedRequest()
    req.prepare_url(url, query_param)
    return req.url.replace(url,"")

if __name__ == '__main__':
    
    host = 'https://api.bitkub.com'
    path = '/api/v3/market/balances'
    api_key = '38408af4f42c75e772c615a34ca4731e84616aa0bf7a9e90cee8f5c08438e731'
    api_secret = '17447c62b012474ca5465b3502e6f804ae5fe223b58c4397a1d99435495ba3ffKW5s5V2WjTNDDPoZROCuJPfgYdlR'
    
    ts = str(round(time.time() * 1000))
    reqBody = {}

    payload = []
    payload.append(ts)
    payload.append('POST')
    payload.append(path)
    payload.append(json.dumps(reqBody))

    sig = gen_sign(api_secret, ''.join(payload))

    print(ts)
    print(sig)

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-BTK-TIMESTAMP': ts,
        'X-BTK-SIGN': sig,
        'X-BTK-APIKEY': api_key
    }

    response = requests.request('POST', host + path, headers=headers, data=json.dumps(reqBody), verify=False)
    requests_to_curl.parse(response) 
    
    #print(response.request.url)
    #print(response.request.body)
    #print(response.request.headers)
    #print(response.text)