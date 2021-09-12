# AsyncBing
asyncbing is an asyncio api wrapper for the [Bing Search Api](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api). It uses a modern `async`/`await` python api.

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
```
import asyncbing
import asyncio

s = asyncbing.Search('key')

async def main():
    resp = await s.fetch('cool search term')
    print(resp.matches)
    oneresult = resp.getOne()
    print(oneresult.name)
    print(oneresult.url)
    print(oneresult.snippet)

asyncio.run(main())
```
