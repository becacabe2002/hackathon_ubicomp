interface AnalysisExplanation {
  recognizer: string;
  pattern_name: string | null;
  pattern: string | null;
  original_score: number;
  score: number;
  textual_explanation: string;
  score_context_improvement: number;
  supportive_context_word: string;
  validation_result: string | null;
  regex_flags: string | null;
}

interface RecognitionMetadata {
  recognizer_name: string;
  recognizer_identifier: string;
}

interface AnalysedData {
  entity_type: string;
  entity_value: string;
  start: number;
  end: number;
  score: number;
  analysis_explanation: AnalysisExplanation;
  recognition_metadata: RecognitionMetadata;
}

interface SanitizationResponse {
  analysed_data: AnalysedData[];
  anonymized_text: string;
}

export { 
  type SanitizationResponse,
  type AnalysedData,
};