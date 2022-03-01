

class TranslateResponse:
    """The class for the Bing Translate Response.
    
    .. warning::
        You must not manually initialize this!"""
    def __init__(self, data: dict):
        self.data = data[0]
    
    @property
    def detected_language(self) -> str:
        """Returns the translated output of the query."""
        return self.data['detectedLanguage']['language']

    @property
    def translated_output(self) -> str:
        """Returns the translated output."""
        return self.data['translations'][0]['text']

    @property
    def translated_language(self) -> str:
        """Returns the language of the translated output."""
        return self.data['translations'][0]['to']

