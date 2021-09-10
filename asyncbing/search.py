import asyncio
import aiohttp
from .exceptions import BadAuth
from .bingresponse import BingResponse


class Search:
    """The searching part of asyncbing"""

    def __init__(self, auth: str, session: aiohttp.ClientSession=None):
        self.headers = {'Ocp-Apim-Subscription-Key': auth}
        self.bing = 'https://api.bing.microsoft.com/v7.0/search'
        if not session:
            self.session = asyncio.run(self.session_setup())
        else:
            self.session = session

    async def session_setup(self) -> aiohttp.ClientSession:
        async with aiohttp.ClientSession() as session:
            return session

    async def fetch(self, search: str) -> BingResponse:
        """Searches with the bing api for the search string provided, with the global market set."""
        async with self.session.get(self.bing, headers=self.headers, params={'q': search}) as resp:
            return BingResponse((await resp.json()))

    # "alias"
    async def search(self, *args, **kwargs) -> fetch:
        """An alias for Search.fetch()"""
        return await self.fetch(*args, **kwargs)
