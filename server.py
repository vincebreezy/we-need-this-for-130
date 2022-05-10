from time import sleep
from fastapi import Body, FastAPI
import treeBasedDB
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
db = treeBasedDB.dataBase()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
        allow_headers=["*"],
    max_age=3600,
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/getwords")
def get_words(num: int = 2):
    words = db.getWords(num)
    ret=dict()
    for i in range(len(words)):
        ret.update({"word" + str(i): words[i]})
    return ret

@app.post("/comparewords")
def compare_words(payload: dict = Body(...)):
    # Send a post request of form:
    # {
    #   "word1": "Apple"
    #   "word2": "Bannana"
    # }
    
    #Sanatize the input to only keys that start with 'word': word0, word1, etc
    payload = {k:v for k,v in payload.items() if k[0:4] == 'word'}
    mostpopular, scores = db.getMostPopular(list(payload.values()))
    i = 0
    ret = {"popular": mostpopular}
    for i in range(len(payload.items())):
        ret.update({"wordscore" + str(i): scores[i]})
    return ret