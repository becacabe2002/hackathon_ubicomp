from dataclasses import field
from src.constants.interpret import actions
from src.constants.promts_LLM import system_prompt_interpret
from pydantic import BaseModel
from typing import Any, Dict, Literal, List
from src.third_parties.llm import comp, comp_structure

class InterpretResult(BaseModel):
    sample_sql_result: str = field(default="The sample sql result will be here")
    intent: List[Literal[
        "identify_user",
        "list_records",
        "download_records",
        "modify_records",
        "count",
        "aggregate_metric",
        "grouped_breakdown",
        "time_series",
        "compare_groups",
        "topk_ranking",
        "retrieve_metadata"
    ]]

def interpret_user_query(query: str) -> InterpretResult:

    result:InterpretResult = comp_structure(
        user_prompt=f"User query: {query}",
        system_promt=system_prompt_interpret,
        text_format = InterpretResult
    )

    # Logic
    record_actions = []
    for itent in result.intent:
        record_action = [action for action in actions if action["itent"] == itent][0]
        record_actions.append(record_action)
        if record_action["decision"] == "deny":
            return record_action

    return record_actions[0]