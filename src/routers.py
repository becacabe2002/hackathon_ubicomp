from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.natural_language_sql_service import perform_sql_query_and_return_result, get_current_search_result

router = APIRouter()

class NaturalLanguageQueryRequest(BaseModel):
    query: str

@router.post("/natural-language-query")
def natural_language_query(request: NaturalLanguageQueryRequest):
    result = perform_sql_query_and_return_result(request.query)
    if not isinstance(result, dict):
        raise HTTPException(status_code=500, detail="Unexpected result format")
    return result

@router.get("/current-search-result")
def current_search_result():
    result = get_current_search_result()
    return result
