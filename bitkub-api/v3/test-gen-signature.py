import hashlib
import hmac
import time
import json

def gen_sign(api_secret, payload_string=None):
    return hmac.new(api_secret.encode('utf-8'), payload_string.encode('utf-8'), hashlib.sha256).hexdigest()


if __name__ == '__main__':

    host = 'https://api.bitkub.com'
    path = '/api/v3/market/balances'
    api_secret = '17447c62b012474ca5465b3502e6f804ae5fe223b58c4397a1d99435495ba3ffKW5s5V2WjTNDDPoZROCuJPfgYdlR'
    
    ts = str(round(time.time() * 1000))
    reqBody = {}

    payload = []
    payload.append(ts)
    payload.append('POST')
    payload.append(path)
    payload.append(json.dumps(reqBody))

    print(''.join(payload))

    sig = gen_sign(api_secret, ''.join(payload))

    print('')
    print(sig)