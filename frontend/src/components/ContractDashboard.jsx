import React, { useState } from "react";
import { createContract, attachSLA, fetchSLA } from "../api/contracts";

function ContractDashboard() {
  const [sla, setSla] = useState([]);

  async function handleFlow() {
    const contractId = await createContract();
    await attachSLA(contractId);
    const slaRecords = await fetchSLA(contractId);
    setSla(slaRecords);
  }

  return (
    <div className="p-6">
      <button
        onClick={handleFlow}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Run Contract Flow
      </button>

      <h2 className="mt-6 text-xl font-bold">SLA Records</h2>

      {sla.length > 0 ? (
        <table className="mt-4 w-full border-collapse border border-gray-300">
          <thead>
            <tr className="bg-gray-100">
              <th className="border border-gray-300 px-4 py-2">APR %</th>
              <th className="border border-gray-300 px-4 py-2">Term (months)</th>
              <th className="border border-gray-300 px-4 py-2">Monthly Payment</th>
              <th className="border border-gray-300 px-4 py-2">Down Payment</th>
              <th className="border border-gray-300 px-4 py-2">Mileage Allowance</th>
              <th className="border border-gray-300 px-4 py-2">Red Flags</th>
            </tr>
          </thead>
          <tbody>
            {sla.map((record) => (
              <tr key={record.id}>
                <td className="border border-gray-300 px-4 py-2">{record.apr_percent}</td>
                <td className="border border-gray-300 px-4 py-2">{record.term_months}</td>
                <td className="border border-gray-300 px-4 py-2">{record.monthly_payment}</td>
                <td className="border border-gray-300 px-4 py-2">{record.down_payment}</td>
                <td className="border border-gray-300 px-4 py-2">{record.mileage_allowance_yr}</td>
                <td className="border border-gray-300 px-4 py-2 text-red-600">{record.red_flags}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="mt-4 text-gray-600">No SLA records yet.</p>
      )}
    </div>
  );
}

export default ContractDashboard;