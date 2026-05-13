from fastapi import FastAPI

app = FastAPI()

@app.get("/") 
def home():
    return {"message": "Home route"}

@app.get("/about")
def about():
    return {"message": "About route"}



@app.get("/contact")
def contact():
    return {
        "name": "Gowtham",
        "role": "AI Backend Developer"
    }

@app.get("/Skills")
def skills():
    return {
        "skills": ["FastAPI", "Python"]
    }
