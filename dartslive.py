import requests
import asyncio
from urllib.error import HTTPError

import logging
LOGGER = logging.getLogger('DartsLive')

import json, os

dir_path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(dir_path, 'user.json')) as json_file:
    data = json.load(json_file)

class Dartslive(object):
    def __init__(self, email, password) -> None:
        self._session = requests.Session()
        self._email = email
        self._password = password
        self._response = ''
        self._accessKey = ''
        self._accountId = 0
        self._playerId = 0
        self._checkDLAuthURL="https://homeapi.dartslive.com/dlhome/action.jsp?actionid=checkDLAuth"
        self._getPlayerURL="https://homeapi.dartslive.com/dlhome/action.jsp?actionid=getPlayer"
        self._healthCheckURL="https://homeapi.dartslive.com/dlhome/action.jsp?actionid=healthCheck"
        self._getAccountMenuURL="https://homeapi.dartslive.com/dlhome/action.jsp?actionid=getAccountMenu"
        self._gameStart="https://homeapi.dartslive.com/dlhome/action.jsp?actionid=gameStart"
        self._gameEnd="https://homeapi.dartslive.com/dlhome/action.jsp?actionid=gameEnd"
    
    def oepn_jsonfile(self, filename):
        data = {}
        dir_path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(dir_path+'/game_template', filename)) as json_file:
            data = json.load(json_file)

        return data

    async def post(self, url, data={}):
        try:
            response = self._session.post(url, json=data)
            response.raise_for_status()
        except HTTPError as http_err:
            LOGGER.info(f'HTTP error occurred: {http_err}')
            return False
        except Exception as err:
            LOGGER.info(f'Other error occurred: {err}')
            return False
        else:
            await asyncio.sleep(int(2))
            self._response = response.json()
            return True

    async def login(self):
        jsondata = self.oepn_jsonfile('checkDLAuth_request.json')
        jsondata['mail'] = self._email
        jsondata['password'] = self._password

        # Login
        if await self.post(self._checkDLAuthURL, jsondata):
            self._accessKey = self._response['accessKey']
            self._accountId = self._response['accountId']
        else:
            LOGGER.error('Login Error')
            return False

        jsondata = self.oepn_jsonfile('getPlayer_request.json')
        jsondata['account_id'] = self._accountId
        jsondata['access_key'] = self._accessKey
        # PlayerId
        if await self.post(self._getPlayerURL, jsondata):
            # get first player
            self._playerId = self._response['player'][0]['id']
        else:
            LOGGER.error('PlayerId Error')
            return False

        return True
