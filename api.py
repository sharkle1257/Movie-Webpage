from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import Movies as ms

app = FastAPI(title="Movie API")

# In-memory playlist
playlist = {}

# CORS (frontend friendly)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# MOVIE SEARCH
# --------------------
@app.get("/movie")
def search_movie(title: str, year: str = ""):
    data = ms.getmovie(title, year)

    return {
        "Title": data["Title"],
        "Year": data["Year"],
        "Rated": data["Rated"],
        "Runtime": data["Runtime"],
        "Plot": data["Plot"],
        "Poster": data["Poster"],
        "Language": data["Language"],
        "imdbRating": data["imdbRating"],
    }

# --------------------
# ADD TO PLAYLIST
# --------------------
@app.post("/playlist/add")
def add_playlist(title: str, year: str = ""):
    data = ms.getmovie(title, year)
    imdb_id = data["imdbID"]

    playlist[imdb_id] = {
        "Title": data["Title"],
        "Year": data["Year"],
        "Rated": data["Rated"],
        "Runtime": data["Runtime"],
        "Plot": data["Plot"],
        "Poster": data["Poster"],
        "Language": data["Language"],
        "imdbRating": data["imdbRating"],
    }

    return {
        "message": "Added successfully!",
        "imdb_id": imdb_id
    }

# --------------------
# GET PLAYLIST
# --------------------
@app.get("/playlist")
def get_playlist():
    return playlist

# --------------------
# DELETE FROM PLAYLIST
# --------------------
@app.delete("/playlist/delete")
def delete_from_playlist(title: str, year: str):
    for imdb_id, movie in list(playlist.items()):
        if movie["Title"] == title and movie["Year"] == year:
            del playlist[imdb_id]
            return {"success": True}

    return JSONResponse(
        status_code=404,
        content={"error": "Movie not found"}
    )
