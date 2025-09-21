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

interface Interpret {
  itent: string;
  decision: string;
  reason: string;

}

interface Insight {
  index: number;
  message: {
    role: string;
    content: string;
    refusal: string | null;
    annotations: any[]; // You can replace `any` with a stricter type if you know the shape
  };
  logprobs: any | null; // Same here, refine if you know the structure
  finish_reason: string;
}
interface SanitizationResponse {
  analysed_data: AnalysedData[];
  anonymized_text: string;

}

export {
  type SanitizationResponse,
  type AnalysedData,
  type Insight,
  type Interpret
};