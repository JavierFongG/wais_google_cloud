from fastapi import FastAPI
# from google.cloud import firestore

app = FastAPI()

# db = firestore.Client.from_service_account_json('serviceAccountKey.json')

@app.get("/")
async def root():
    return {"message": "Hello World"}