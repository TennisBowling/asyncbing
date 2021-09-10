from .exceptions import NotEnoughResults
from typing import Tuple
from .Searchresult import BingSearchResult


class BingResponse:
    def __init__(self, data):
        self.data = data
        self.resulNum = 0

    @property
    def originalQuery(self) -> str:
        """Returns a string if for some reason you forgot what you searched for"""
        return self.data['queryContext']['originalQuery']

    @property
    def matches(self) -> int:
        """Returns the amount of **estimated** matches found for your search query"""
        return self.data['webPages']['totalEstimatedMatches']

    @property
    def searchUrl(self) -> str:
        """Returns the bing search url you would get if you were to type in the query in the bing website directly."""
        return self.data['webPages']['webSearchUrl']

    @property
    def getOne(self) -> BingSearchResult:
        """Gets the top search result and returns a BingSearchResult."""
        if not len(self.data['webPages']['value']) >= 1:
            raise NotEnoughResults("There weren't enough search results to give a BingSearchResult.")
        return BingSearchResult((self.data['webPages']['value'][0]))

    @property
    def getThree(self) -> Tuple[BingSearchResult, BingSearchResult, BingSearchResult]:
        """Gets the top three search results and returns a tuple of BingSearchResult"""
        if not len(self.data['webPages']['value']) >= 1:
            raise NotEnoughResults("There weren't enough search results to give a BingSearchResult.")
        return (BingSearchResult(self.data['webPages']['value'][0]), BingSearchResult(self.data['webPages']['value'][1]), BingSearchResult(self.data['webPages']['value'][2]))
