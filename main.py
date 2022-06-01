import asyncio
import os, json

import logging

from dartslive import Dartslive

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
LOGGER = logging.getLogger('main')

async def main():
    email = []
    password = []
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir_path, 'user.json')) as json_file:
        data = json.load(json_file)
        for item in data:
            email.append(item['email'])
            password.append(item['password'])
    
    LOGGER.info('Start DartsLive Home Auto Finish Mission...')
    for index in range(len(email)):
        LOGGER.info('Email: '+email[index])
        dartslive = Dartslive(email[index], password[index])
        if await dartslive.login() :
            LOGGER.info('Account ID :'+str(dartslive._accountId)+', Player ID:'+str(dartslive._playerId)+', Access Key:'+dartslive._accessKey)
        await dartslive.playgame()
        LOGGER.info(dartslive._missionClear)

    LOGGER.info('All Done, Sleep 8 Hours...')
    await asyncio.sleep(8*60*60)


if __name__ == "__main__":
    while True:
        asyncio.run(main())