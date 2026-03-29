import { useState } from "react";
import { getVinReport } from "../api/vin";

export default function VINReport() {
  const [vin, setVin] = useState("");
  const [report, setReport] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await getVinReport(vin);
      setReport(data);
    } catch {
      alert("VIN lookup failed");
    }
  };

  return (
    <div className="border p-4 rounded">
      <h2 className="text-xl font-bold mb-4">VIN Report</h2>
      <form onSubmit={handleSubmit} className="mb-4">
        <input
          type="text"
          placeholder="Enter VIN"
          className="border p-2 mr-2 rounded"
          value={vin}
          onChange={(e) => setVin(e.target.value)}
        />
        <button className="bg-orange-500 text-white px-4 py-2 rounded">
          Lookup
        </button>
      </form>

      {report && (
        <table className="table-auto w-full">
          <tbody>
            <tr><td className="font-semibold">Brand</td><td>{report.brand}</td></tr>
            <tr><td className="font-semibold">Model</td><td>{report.model}</td></tr>
            <tr><td className="font-semibold">Fuel Type</td><td>{report.fuelType}</td></tr>
          </tbody>
        </table>
      )}
    </div>
  );
}