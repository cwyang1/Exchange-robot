#-*- coding=utf-8 -*-
import hashlib
import random
import time
from time import sleep
from datetime import datetime
from requests import request

class robot():
    def get_timestamp(self):
        now = datetime.now()
        float_timestamp = time.mktime(now.timetuple())
        _stamp = str(float_timestamp)
        try:
            _index = _stamp.find('.')
            if _index >= 0:
                return _stamp[: _index]
        except:
            pass
        return _stamp

    def get_data_sign(self,datano_time_sign,secret_key):
        data=datano_time_sign
        #把时间戳添加到data
        data['time']= self.get_timestamp()
        _keys = data.keys()
        _keys = sorted(_keys, key = str.lower)
        _args = []
        for _key in _keys:
            if data[_key]:
                _args.append(_key)
                _args.append(str(data[_key]))
        _str = ''.join(_args)
        _sign=_str+secret_key
        # print(_sign)
        m = hashlib.md5()
        m.update(_sign.encode('utf-8'))
        # 把sign添加到data
        data['sign']=m.hexdigest()
        return data

    def creat_oder(self,data,url,secret_key):
        data = self.get_data_sign(data,secret_key)
        print(data)
        headers = {"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
        res = request(method='post', url=url, data=data,
                      headers=headers, verify=False)
        print(res.text)

    def get_ticker(self,url):
        res= request(method='get', url=url, verify=False).json()
        return res['data']

    def run_robot(self,symbol,apikey_='18a09aba9cda6fdffdae35c0c3608077',secret_key_='4d31d11c351ee336a62a0c585eec41eb'):
        url1 = 'https://openapi.bitfires.com/open/api/get_ticker?symbol='+symbol
        res = self.get_ticker(url1)
        price_buy = float(res['buy'])
        price_sell = float(res['sell'])

        data1 = {
            'side': 'SELL',
            'type': '1',
            'volume': random.randint(1, 9),
            'price': price_buy + round(random.uniform(1, 10), 2),
            'symbol': symbol,
            'api_key': apikey_
        }

        data2 = {
            'side': 'BUY',
            'type': '1',
            'volume': random.randint(1, 9),
            'price': price_sell + round(random.uniform(1, 10), 2),
            'symbol': symbol,
            'api_key': apikey_
        }
        url = 'https://openapi.bitfires.com/open/api/create_order'
        secret_key = secret_key_
        sleep(1)
        self.creat_oder(data1, url, secret_key)
        sleep(1)
        self.creat_oder(data2, url, secret_key)




