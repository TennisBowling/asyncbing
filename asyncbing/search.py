import aiohttp
from .searchresponse import SearchResponse

class Search:
    """The searching part of asyncbing"""
    def __init__(self, auth: str, *, session: aiohttp.ClientSession=None):
        self.headers = {'Ocp-Apim-Subscription-Key': auth}
        self.bing = 'https://api.bing.microsoft.com/v7.0/search'

        if session:
            self.session = session
        else:
            self.session = aiohttp.ClientSession() # find a way to make this async

    async def fetch(self, search: str) -> SearchResponse:
        """|coro|
        Searches with the bing api for the search string provided, with the global market set."""
        async with self.session.get(self.bing, headers=self.headers, params={'q': search}) as resp:
            return SearchResponse((await resp.json()))

    # "alias"
    async def search(self, *args, **kwargs) -> fetch:
        """|coro|
        An alias for Search.fetch()"""
        return await self.fetch(*args, **kwargs)
    
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

def search(auth: str, *, session: aiohttp.ClientSession=None):
    """Takes a `auth` token, as well as an optional aiohttp session.
        example:
        ``
        async with asyncbing.Search('AUTHTOKEN') as searching:
            await searching.fetch...
        ``"""
    return Search(auth, session=session)