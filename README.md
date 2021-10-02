# AsyncBing
asyncbing is an asyncio api wrapper for the [Bing Search Api](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api). It uses a modern `async`/`await` python api. \
[Docs](https://asyncbing.readthedocs.io/en/latest/)

## Installing

`python -m pip install asyncbing` \
For the stable version of asyncbing. \
`python -m pip install git+https://github.com/TennisBowling/asyncbing/` \
For the unstable/cutting edge of asyncbing. Not recommended in production. \

## Usage

Import it with \
`from asyncbing import search` \
Then initialize asyncbing with your Bing Search Api key [guide](https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/create-bing-search-service-resource) like
`s = search.Search('APIKEYGOESHERE')`


## Sample usage
Searching
```
import asyncbing
import asyncio

async def main():
    async with asyncbing.Search('key') as s:
        resp = await s.fetch('cool search term')
        print(resp.matches)
        oneresult = resp.getOne()
        print(oneresult.name)
        print(oneresult.url)
        print(oneresult.snippet)

asyncio.run(main())
```
Translating

```
import asyncbing
import asyncio

async def main():
    async with asyncbing.Translate('key', region='useast') as t:
        resp = await t.translate('je veux traduire')
        print(resp.detected_language)
        print(resp.translated_output)
        print(resp.translated_language)

asyncio.run(main())
```



(Normally, searching isn't part of the Bing Api's. It's part of the Microsoft Cognitive Api's. Might as well rename this to asyncms, or asyncmsapi, no?)
