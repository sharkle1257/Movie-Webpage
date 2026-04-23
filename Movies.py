import requests
def getmovie(title, year):
    url = "http://www.omdbapi.com/?apikey=df3bbba2&"
    p = {
        "t": f"{title}" , "y" : f"{year}" , "plot" : "full" 
                }
    response = requests.get(url,params= p)
    data = response.json()
    print(data["Plot"])
    return data
