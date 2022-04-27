# wikiWrapper
## About
wikiWrapper is a basic python module designed to make working with the Mediawiki action API easier.
## Usage
Just place wikiWrapper.py in your working directory and import it into your program. Alternatively, install via pypi on the command line using your preferred package manager.
### Install (pip)
#### Windows:
```cmd
py -m pip install wikiWrapper
```
Note: by default, python will be placed in your PATH environment variable directly as 'py'. If python is not present in your PATH, reinstall python, add it manually, or install in your python directory.

#### MacOS & Linux:
```bash
python310 -m pip install wikiWrapper
```
Note: assumes you are using Python version 3.10. Substitute 310 for your version of python, i.e python39.
### Creating a search:
```py
import wikiWrapper
query = wikiWrapper.SearchQuery("Penguin")
```
SearchQuery parameters:

```def __init__(self, search_q, host="wikipedia", srnamespace=0, srlimit=10, sroffset=0, srqiprofile="classic", _format="json")```

```search_q```: This should be a string containing the search you are enacting. It is the only mandatory parameter

```host```: This should be a string. It chooses which member of the WikiMedia foundation you wish to make the search to. The default value of this parameter is "wikipedia". Accepted values are ```("wikipedia", "wikibooks", "wikidata")```

```srnamespace```: This should be an integer or a string. It chooses which namespace on the wikimedia pages you wish to execute your search on. For all namespaces, use ```"*"```. The default value of this parameter is ```0```. 

```srlimit```: This should be an integer or a string. The amount of pages to return from a search. The default value of this parameter is ```10```.

```sroffset```: This should be an integer or a string. Shifts results forward by specified amount. The default value of this parameter is ```0```

```srqiprofile```: This should be a string. Chooses the algorithm used by the MediaWiki API to find your search results. The default value of this parameter is ```"classic"```. Accepted values are ```("classic", "classic_noboostlinks", "empty", "wsum_inclinks", "wsum_inclinks_pv", "popular_inclinks_pv", "popular_inclinks", "engine_autoselect")```

```_format```: The format you want your data back in. Default value is ```"json"```

### Methods

```query.search()```:
Returns raw HTTP request from the wikipedia page.

```query.content_summary()```: 
Returns the content summary of the search_q parameter's wiki page.

```query.extlinks(page_limit=None)```
Returns a json dictionary containing every outwards facing link on the page (usually references). Method takes one optional parameter, an integer between 1 and 500.