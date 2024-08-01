import sys
# import sys: Imports the sys module, which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
import requests
# import requests: Imports the requests library, which allows you to send HTTP requests using Python. It is commonly used to interact with web APIs.
import json
# import json: Imports the json module, which provides methods for parsing JSON (JavaScript Object Notation), a popular data format used for APIs.
def main():
    if len(sys.argv) != 3:
        sys.exit()
        # sys.exit(): If the number of arguments is not 3, the program exits.
    get_songs(10,"Arjit")
        
def get_songs(no_of_songs,artist_name):    
    responce = requests.get("https://itunes.apple.com/search?entity=song&limit="+ str(no_of_songs) +"&term="+artist_name)
    # above instruction Sends an HTTP GET request to the iTunes API to search for songs by the specified artist, limited to the specified number of results.
    '''
    print(json.dumps(responce.json(),indent=2))
    '''
    obj = responce.json()
    # obj = responce.json(): Parses the JSON response from the API into a Python dictionary.

    for result in obj["results"]:
        print(result["trackName"])
        
if __name__ == "__main__":
    main()
    # if __name__ == "__main__":: Ensures that the main function is called only when the script is run directly (not when imported as a module).