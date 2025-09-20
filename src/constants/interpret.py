actions = [
    {
        "itent": "identify_user",
        "decision": "deny",
        "reason": "Identify user is not allowed",
    },
    {
        "itent": "list_records",
        "decision": "deny",
        "reason": "List records is not allowed",
    },
    {
        "itent": "download_records",
        "decision": "deny",
        "reason": "Download records is not allowed",
    },
    {
        "itent": "modify_records",
        "decision": "deny",
        "reason": "Modify records is not allowed",
    },
    {
        "itent": "count",
        "decision": "allow_with_transform",
        "transforms": ["aggregate", "small_cell_suppression", "dp_noise"],
    },
    {
        "itent": "aggregate_metric",
        "decision": "allow_with_transform",
        "transforms": ["aggregate", "small_cell_suppression", "dp_noise"],
    },
    {
        "itent": "grouped_breakdown",
        "decision": "allow_with_transform",
        "transforms": ["aggregate", "small_cell_suppression", "dp_noise"],
    },
    {
        "itent": "time_series",
        "decision": "allow_with_transform",
        "transforms": ["aggregate", "small_cell_suppression", "dp_noise"],
    },
    {
        "itent": "compare_groups",
        "decision": "allow_with_transform",
        "transforms": ["aggregate", "small_cell_suppression", "dp_noise"],
    },
    {
        "itent": "topk_ranking",
        "decision": "allow_with_transform",
        "transforms": ["aggregate", "small_cell_suppression", "dp_noise"],
    }
]
