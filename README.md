#wikiWrapper
##ABOUT
wikiWrapper is a basic python module designed to make working with the mediawiki action API easier.
##Usage
###Install:
```cmd
git clone https://github.com/git-shr4pnel/wikiWrapper/
cd wikiWrapper
python3 -m pip install -r requirements.txt
```
After this, just place wikiWrapper.py in your working directory and import it into your program.
###Creating a search:
```py
import wikiWrapper
query = wikiWrapper.SearchQuery(search="Penguin")
```
SearchQuery parameters:

```search```: This should be a string containing the search you are enacting. It is the only mandatory parameter

```host```: This should be a string. It chooses which member of the WikiMedia foundation you wish to make the search to. The default value of this parameter is "wikipedia". Accepted values are ```("wikipedia", "wikibooks", "wikidata")```

```srnamespace```: This should be an integer or a string. It chooses which namespace on the wikimedia pages you wish to execute your search on. For all namespaces, use ```"*"```. The default value of this parameter is ```0```. 

```srlimit```: This should be an integer or a string. The amount of pages to return from a search. The default value of this parameter is ```10```.

```sroffset```: This should be an integer or a string. Shifts results forward by specified amount. The default value of this parameter is ```0```

```srqiprofile```: This should be a string. Chooses the algorithm used by the MediaWiki API to find your search results. The default value of this parameter is ```"classic"```. Accepted values are ```("classic", "classic_noboostlinks", "empty", "wsum_inclinks", "wsum_inclinks_pv", "popular_inclinks_pv", "popular_inclinks", "engine_autoselect")```

###Accessing data from API call:
Your API call has 2 useful attributes, ```url``` and ```response```.

```py
import wikiWrapper
query = wikiWrapper.SearchQuery("Don Quixote")
print(query.url, query.response)
>>> https://en.wikipedia.org/?curid=8237 <Response [200]>
```
Response is a ```requests``` object. The documentation for ```requests``` can be found [here](https://docs.python-requests.org/). ```url``` points directly to the page using the page ID itself. 