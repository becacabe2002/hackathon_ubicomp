from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any

from src.services.anonymizer.anonymizer import anonymize_data
from src.services.analyzer.analyzer import analyzer
from src.services.ner import anonymize_text
from src.services.interpret.interpret_query import interpret_user_query
from .routers import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str

class AnonymizeRequest(BaseModel):
    text: str
    analyzer_results: List[Any]

class AnonymizeResponse(BaseModel):
    anonymized_text: str

app.include_router(router, prefix="/natural_sql_service", tags=["natural_sql_service"])

@app.post("/analyze")
def analyze_endpoint(request: AnalyzeRequest):
    results = analyzer(request.text)
    anonymized = anonymize_data(request.text, results)
    result_2 = anonymize_text(anonymized)

    for r in results:
        r.entity_value = request.text[r.start:r.end]

    return {
        "analysed_data": results,
        **result_2,
    }

    
    
@app.post("/test_interpret")
def test_interpret_endpoint(request: AnalyzeRequest):
    results = interpret_user_query(request.text)
    return {
        "interpret": results,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
