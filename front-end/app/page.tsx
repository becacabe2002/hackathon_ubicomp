"use client";
import React, { useState, FormEvent } from "react";
import { SanitizationResponse, Insight, AnalysedData, Interpret } from "./interfaces";
import TableData from "./table";
import Footer from "./footer";
import Loading from "./loading";
import axios from "axios";

export default function CenteredInputPage() {
  const [textInputValue, setTextInputValue] = useState<string>("");
  const [displayQueryText, setDisplayText] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [insight, setInsight] = useState<Insight | null>(null);
  const [analyzed_data, setAnalyzedData] = useState<SanitizationResponse | null>(null);

  const [interpret, setInterpret] = useState<Interpret | null>(null);


  const fetchData = async (data: { text: string }) => {
    const response = await axios.post("http://localhost:5678/webhook-test/webhook", data);
    const array = response.data as any[];
    const interpret: Interpret = array[0]?.interpret
    const analysed_data: SanitizationResponse = array[1]
    let insight: Insight | undefined;
    console.log(interpret)
    console.log(analysed_data)
    console.log(insight)
    if (interpret?.decision !== "deny") {
      insight = array[2]
    }


    setInsight(insight ?? null);
    setAnalyzedData(analysed_data ?? null);
    setInterpret(interpret ?? null);
  };
  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    if (textInputValue.trim()) {
      e.preventDefault();
      setDisplayText(textInputValue);
      setInsight(null);
      setAnalyzedData(null);
      setInterpret(null);
      setLoading(true);
      await fetchData({ text: textInputValue });
      setLoading(false);
      setTextInputValue("");
    }
  }
  console.log(interpret)
  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-6">
      <section className="absolute top-6">
        <h1 className="text-3xl font-bold text-center">Piiden</h1>
      </section>
      <section className="w-full max-w-[1024px]">
        <div className="rounded-2xl bg-white shadow-md p-6">
          <p className="text-sm text-gray-500 text-center mt-1">
            Enter your prompt below and submit.
          </p>

          <form onSubmit={handleSubmit} className="mt-6 flex items-center gap-2">
            <label htmlFor="centered-input" className="sr-only">
              Your text
            </label>
            <input
              id="centered-input"
              type="text"
              value={textInputValue}
              onChange={(e) => setTextInputValue(e.target.value)}
              placeholder="Write here..."
              className="flex-1 rounded-xl border border-gray-300 px-4 py-2 outline-none focus:ring-2 focus:ring-black/10 focus:border-gray-400"
            />


            {loading ? <Loading /> : <button
              type="submit"
              className="rounded-xl px-4 py-2 bg-black text-white hover:bg-black/90 active:scale-[0.99] transition"

            >
              Submit
            </button>}
          </form>

          {analyzed_data && (
            <div className="mt-4 ">
              <h2 className="text-lg font-semibold text-center">User Query</h2>
              <div className="mt-1 text-lg font-medium break-words">{displayQueryText}</div>
              <h2 className="text-lg font-semibold text-center">Sanitized Query</h2>
              <div className="mt-1 text-lg font-medium break-words">{analyzed_data?.anonymized_text}</div>
              <h2 className="text-lg font-semibold text-center">Result</h2>
              <div className="mt-1 text-lg font-medium break-words">{interpret?.decision == "deny" ? interpret?.reason : insight?.message?.content!!}</div>
            </div>
          )}
        </div>
      </section>
      {analyzed_data && <TableData {...analyzed_data} />}
      <Footer />
    </main>
  );
}