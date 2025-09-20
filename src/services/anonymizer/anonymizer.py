from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig


def anonymize_data(original_text, analyzered_text):
    operators = {
        "DATE_TIME": OperatorConfig("keep"),
    }
    anonymizer = AnonymizerEngine()

    anonymized_text = anonymizer.anonymize(
        text=original_text, analyzer_results=analyzered_text, operators=operators
    ).text
    return anonymized_text
