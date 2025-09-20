import React from "react";
import { SanitizationResponse } from "./interfaces";

const TableData = (result: SanitizationResponse) => (
    <section className="w-full max-w-[1024px] mt-10  justify-center pb-16">
        <div className="rounded-2xl bg-white shadow-md p-2 overflow-x-auto">
            <h2 className="text-xl font-semibold text-center mb-4">Findings with decision factors
            </h2>
            <div className="w-full overflow-x-auto flex justify-center">
                <table className="max-w-[1024px] border border-gray-300 text-sm">
                    <thead className="bg-gray-100">
                        <tr>
                            <th className="border px-3 py-2">Entity_type</th>
                            <th className="border px-3 py-2">Entity_value</th>
                            <th className="border px-3 py-2 w-[20px]">Score</th>
                            <th className="border px-3 py-2">Pattern_name</th>
                            <th className="border px-3 py-2">Recognizer</th>
                            <th className="border px-3 py-2">Explanation</th>
                            <th className="border px-3 py-2">Context word</th>
                        </tr>
                    </thead>
                    <tbody>
                        {result.analysed_data.map((data, index) => (
                            <tr key={index} className="hover:bg-gray-50">
                                <td className="border px-3 py-2">{data.entity_type}</td>
                                <td className="border px-3 py-2">{data.entity_value}</td>
                                <td className="border px-3 py-2 w-[20px]">{data.score.toFixed(4)}</td>
                                <td className="border px-3 py-2">{data.analysis_explanation?.pattern_name ?? ''}</td>
                                <td className="border px-3 py-2">{data.analysis_explanation?.recognizer ?? ''}</td>
                                <td className="border px-3 py-2">{data.analysis_explanation?.textual_explanation ?? ''}</td>
                                <td className="border px-3 py-2">{data.analysis_explanation?.supportive_context_word ?? ''}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    </section>
);

export default TableData;