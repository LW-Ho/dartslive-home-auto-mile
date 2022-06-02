import asyncio
import os, json

import logging
from random import randrange

from dartslive import Dartslive

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
LOGGER = logging.getLogger('main')

async def main():
    try:
        userdata = []
        dir_path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(dir_path, 'user.json')) as json_file:
            userdata = json.load(json_file)
        
        LOGGER.info('Start DartsLive Home Auto Finish Mission...')
        for item in userdata:
            LOGGER.info('Email: '+str(item['email']))
            dartslive = Dartslive(item['email'], item['password'])
            
            # Login then get mile and finish missions.
            if await dartslive.login() :
                LOGGER.info('Account ID :'+str(dartslive._accountId)+', Player Name and ID : '+str(dartslive._playerName)+', '+str(dartslive._playerId)+', Access Key:'+dartslive._accessKey)
                await dartslive.playgame()
                
            await dartslive.getAccountDetail()

            # Send Email
            if item['notify'] != '':
                try:
                    import gmail
                    gmail.notify(item['notify'], json.dumps(dartslive._missionClear))
                except Exception as e:
                    LOGGER.error(e)

            LOGGER.info(dartslive._missionClear)

    except Exception as e:
        LOGGER.error(e)

    hours = randrange(8,12)
    LOGGER.info('Sleep '+str(hours)+' Hours...')
    await asyncio.sleep(hours*60*60)


if __name__ == "__main__":
    while True:
        asyncio.run(main())