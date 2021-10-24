import aiohttp
import asyncio
from .searchresponse import SearchResponse

class Search:
    """The searching part of asyncbing.\n
    If you manually initialize this class, you won't be able to use the async with syntax. It's recommended to use :meth:`asyncbing.search`.
    """
    def __init__(self, auth: str, *, session: aiohttp.ClientSession=None):
        self.headers = {'Ocp-Apim-Subscription-Key': auth}
        self.bing = 'https://api.bing.microsoft.com/v7.0/search'

        async def create_session():
            self.session = session or aiohttp.ClientSession()

        asyncio.get_event_loop().run_until_complete(create_session())

    async def fetch(self, search: str) -> SearchResponse:
        """|coro|\n
        Searches with the bing api for the search string provided, with the global market set."""
        async with self.session.get(self.bing, headers=self.headers, params={'q': search}) as resp:
            return SearchResponse((await resp.json()))

    # "alias"
    async def search(self, search: str) -> SearchResponse:
        """|coro|\n
        An alias for :meth:`asyncbing.Search.fetch`"""
        return await self.fetch(search)
    
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

def search(auth: str, *, session: aiohttp.ClientSession=None):
    """Takes a `auth` token, as well as an optional aiohttp session.\n
        It is recommended to use this function instead of :class:`asyncbing.Translate` as it returns it, and you can use ``async with`` syntax in it.\n
        example:\n
        .. code-block:: python
        
          async with asyncbing.search('AUTHTOKEN') as searching:
            await searching.fetch...
        """
    return Search(auth, session=session)
