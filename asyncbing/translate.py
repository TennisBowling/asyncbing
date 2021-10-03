import uuid
import aiohttp
from .translateresponse import TranslateResponse

class Translate:
    """The translating part of asyncbing. If you use this class, you won't be able to use the async with syntax."""
    def __init__(self, auth: str, *, region: str=None, session: aiohttp.ClientSession=None):
        self.auth = auth
        self.bing = 'https://api.cognitive.microsofttranslator.com/translate'
        if not region:
            import warnings
            warnings.warn("You haven't set a region. asyncbing will default to us-central.")
            self.region = 'centralus'
        else:
            self.region = region

        if session:
            self.session = session
        else:
            self.session = aiohttp.ClientSession() # find a way to make this async
    
    async def translate(self, query: str, *, tolang: str='en', fromlang: str=None) -> TranslateResponse:
        """|coro|
        Translate the given query with an optional `tolang` language to translate to, as well as an optional `fromlang` language to translate from.
        If `tolang` isn't provided, it will auto translate to english. If `fromlang` isn't provided, it will auto translate from autodetect."""
        if not fromlang:
            params = {'api-version': '3.0', 'to': [tolang]}
        else:
            params = {'api-version': '3.0', 'to': [tolang], 'from': fromlang}
        async with self.session.post(self.bing, params=params, headers={'Ocp-Apim-Subscription-Key': self.auth, 'Ocp-Apim-Subscription-Region': self.region, 'Content-type': 'application/json', 'X-ClientTraceId': str(uuid.uuid4())}, json=[{'text': query}]) as resp:
            return TranslateResponse((await resp.json()))
        
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

def translate(auth: str, *, region: str=None, session: aiohttp.ClientSession=None) -> Translate:
    """Takes a `auth` token, as well as an optional aiohttp session.\n
    It is recommended to use this instead of manually initializing :class:`asyncbing.Translate` because you can use the ``async with`` syntax, and it returns :class:`asyncbing.Translate`.\n
    example:\n
    .. code-block:: python

      async with asyncbing.Translate('AUTHTOKEN', region='eastus') as translating:
          await translating.translate...
    """
    return Translate(auth, region=region, session=session)