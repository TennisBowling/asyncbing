class SearchResult:
    """Represents a Bing Search Result (like url, snippet, name, etc)
    .. warning::
        You must not manually initialize this!"""
    def __init__(self, data):
        self.data = data
    
    @property
    def name(self) -> str:
        """Returns the name of the Search Response."""
        return self.data['name']
    
    @property
    def url(self) -> str:
        """Return the url of the Search Response."""
        return self.data['url']
    
    @property
    def isFamilyFriendly(self) -> bool:
        """Returns a bool if the Search Response is family friendly."""
        return self.data['isFamilyFriendly']
    
    @property
    def displayUrl(self) -> str:
        """The display url of the Search Response.
        I don't actually know what this is, I think it is a trimmed version of the url"""
        return self.data['displayUrl']
    
    @property
    def snippet(self) -> str:
        """Returns a snippet of the content on the webpage. It's the description/snippet below the url and name."""
        return self.data['snippet']
    
    @property
    def dateLastCrawled(self) -> str:     # TODO: get this as a datatime.datetime
        """Returns when the page was last crawled by Bing."""
        return self.data['dateLastCrawled']
    
    @property
    def language(self) -> str:
        """Returns what language the page is in."""
        return self.data['language']
    
    @property
    def isNavigational(self) -> bool:
        """I have no idea what this is. Returns a bool if page is navigational."""
        return self.data['isNavigational']
