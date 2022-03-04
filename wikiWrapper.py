import requests

hosts = {
    "wikipedia": "https://en.wikipedia.org/w/api.php",
    "wikidata": "https://www.wikidata.com/w/api.php",
    "wikibooks": "https://en.wikibooks.org/w/api.php"
}
responses = {
    "wikipedia": "https://en.wikipedia.org/?curid=",
    "wikidata": "https://en.wikidata.org/?curid=",
    "wikibooks": "https://en.wikibooks.org/?curid="
}


class SearchQuery:
    def __init__(self, search, host="wikipedia", srnamespace=0, srlimit=10, sroffset=0, srqiprofile="classic",
                 rtn_format="json"):
        self.host = host
        self.search = search
        self.rtn_format = rtn_format
        self.search = search
        self.srnamespace = srnamespace
        self.srlimit = srlimit
        self.sroffset = sroffset
        self.srqiprofile = srqiprofile
        self.url = None
        self.response = None
        self.__GET()

    def __GET(self):
        payload = {
            "action": "query",
            "list": "search",
            "format": self.rtn_format,
            "srsearch": self.search,
            "srnamespace": self.srnamespace,
            "srlimit": self.srlimit,
            "sroffset": self.sroffset,
            "srqiprofile": self.srqiprofile
        }
        try:
            r = requests.get(hosts[self.host], params=payload)
        except KeyError:
            raise RuntimeError("Invalid host specified")
        self.url = get_wiki_url(r, self.host)
        self.response = r


def get_wiki_url(pid, response):
    if type(pid) is not requests.models.Response:
        raise TypeError("Argument must be a requests object")
    try:
        pid = pid.json()["query"]["search"][0]["pageid"]
    except IndexError:
        return None
    return f"{responses[response]}{pid}"
