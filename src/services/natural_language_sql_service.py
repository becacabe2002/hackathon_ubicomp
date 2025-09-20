from src.third_parties.database import run_sql_query
from src.third_parties.llm import comp, comp_structure
from src.third_parties.cache import set_cache, get_cache, clear_cache
from src.constants.promts_LLM import system_prompt_sql_generator, system_prompt_guardrail
from pydantic import BaseModel, Field
from typing import Literal

class ClassificationResult(BaseModel):
    classification: Literal["accept", "reject"]
    reason: str = Field(..., description="Reason why the query is rejected")

def guardail_user_query(query: str) -> Literal["accept", "reject"]:
    """
    A guardrail function to check if the user query is valid.
    """

    result:ClassificationResult = comp_structure(
        system_promt=system_prompt_guardrail,
        user_prompt=f"User query: {query}",
        text_format=ClassificationResult
    )

    return result

def perform_sql_query_and_return_result(query: str) -> list[dict]:
    clear_cache("current_search_result")

    result_guardail:ClassificationResult = guardail_user_query(query)
    if result_guardail.classification == "reject":
        return {
            "ai_response": result_guardail.reason,
            "sql_response_available": False
        }

    query = comp(
        system_promt=system_prompt_sql_generator,
        user_prompt=f"User query: {query}"
    )

    output = run_sql_query(query)

    set_cache(key="current_search_result", value=output)

    return {
        "ai_response": "Success, The result is below",
        "sql_response_available": True
    }

def get_current_search_result() -> list[dict]:
    return get_cache("current_search_result")