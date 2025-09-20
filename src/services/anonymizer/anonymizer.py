from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig


def anonymize_data(original_text, analyzered_text):
    # operators = {
    #     "PHONE_NUMBER": OperatorConfig("replace", {"new_value": "PHONE_NUMBER"}),
    #     "DEFAULT": OperatorConfig("replace", {"new_value": "<ANONYMIZED>"}),
    # }
    anonymizer = AnonymizerEngine()

    anonymized_text = anonymizer.anonymize(
        text=original_text,
        analyzer_results=analyzered_text,
        # operators=operators
    ).text
    return anonymized_text
