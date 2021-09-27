import asyncio
import aiohttp

class Translate:
    """The translating part of asyncbing"""
    def __init__(self, auth: str, *, session: aiohttp.ClientSession=None, loop=asyncio.new_event_loop()):
        self.headers = {'Ocp-Apim-Subscription-Key': auth}
        self.bing = 'https://api.bing.microsoft.com/v7.0/search'
        if not session:
            loop.create_task(self.session_setup())
        else:
            self.session = session

    async def session_setup(self) -> aiohttp.ClientSession:
        async with aiohttp.ClientSession() as session:
            self.session = session
    