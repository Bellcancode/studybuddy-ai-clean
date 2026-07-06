from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
from pathlib import Path
from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text
from quiz_generator import generate_quiz
from planner import generate_study_plan
import os

# Load environment variables
load_dotenv()

# Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# FastAPI app
app = FastAPI()

# Upload folder
UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

# Store latest uploaded PDF text
current_pdf_text = ""

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    message: str


# ---------------- CHAT ---------------- #

@app.post("/chat")
async def chat(request: ChatRequest):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.message,
    )

    return {"response": response.text}


# ---------------- PDF UPLOAD ---------------- #

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global current_pdf_text

    file_path = UPLOAD_FOLDER / file.filename

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    current_pdf_text = extract_text_from_pdf(file_path)

    return {
        "message": "PDF uploaded successfully.",
        "filename": file.filename,
    }


# ---------------- SUMMARY ---------------- #

@app.get("/summary")
async def get_summary():
    global current_pdf_text

    if not current_pdf_text:
        return {"summary": "Please upload a PDF first."}

    return {
        "summary": summarize_text(current_pdf_text)
    }


# ---------------- QUIZ ---------------- #

@app.get("/quiz")
async def get_quiz():
    global current_pdf_text

    if not current_pdf_text:
        return {"quiz": "Please upload a PDF first."}

    return {
        "quiz": generate_quiz(current_pdf_text)
    }


# ---------------- STUDY PLANNER ---------------- #

@app.get("/planner")
async def get_planner():
    global current_pdf_text

    if not current_pdf_text:
        return {"planner": "Please upload a PDF first."}

    return {
        "planner": generate_study_plan(current_pdf_text)
    }