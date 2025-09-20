from presidio_analyzer import AnalyzerEngine

LANGUAGE = "en"


def analyzer(data, default_threshold=0.1):
    analyzer = AnalyzerEngine()
    results = analyzer.analyze(
        text=data,
        score_threshold=default_threshold,
        language=LANGUAGE,
        return_decision_process=True,
    )
    return results
