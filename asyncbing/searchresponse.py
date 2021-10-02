from exceptions import NotEnoughResults
from typing import Tuple
from searchresult import SearchResult

class SearchResponse:
    """Represents a Bing Response (not a search result response)
    
    ```{caution}
    You must not manually initialize this!
    ```"""
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

    def getOne(self) -> SearchResult:
        """Gets the top search result and returns a :class:`asyncbing.SearchResult`."""
        if not len(self.data['webPages']['value']) >= 1:
            raise NotEnoughResults("There weren't enough search results to give a BingSearchResult.")
        return SearchResult((self.data['webPages']['value'][0]))

    def getThree(self) -> Tuple[SearchResult, SearchResult, SearchResult]:
        """Gets the top three search results and returns a tuple of :class:`asyncbing.SearchResult`"""
        if not len(self.data['webPages']['value']) >= 3:
            raise NotEnoughResults("There weren't enough search results to give a BingSearchResult.")
        return (SearchResult(self.data['webPages']['value'][0]), SearchResult(self.data['webPages']['value'][1]), SearchResult(self.data['webPages']['value'][2]))
    
    def getMany(self, amount: int, *, start: int=0) -> Tuple[SearchResult]:
        """Returns as many :class:`asyncbing.SearchResult` as you want as the max defined by the int passed into the function. has an optional ``start`` kwarg. Defaults to 0."""
        if not len(self.data['webPages']['value']) >= amount:
            raise NotEnoughResults("There weren't enough search results to give a BingSearchResult for the specified amount.")
        return ([SearchResult(self.data['webPages']['value'][x]) for x in range(start, amount)])
