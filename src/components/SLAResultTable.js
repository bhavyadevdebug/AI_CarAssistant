export default function SLAResultTable() {
  // For now, static demo data
  const data = {
    documentType: "CAR LEASE AGREEMENT",
    documentDate: "2025-03-05",
    contractNumber: "CLA-2025-55921",
  };

  return (
    <div className="border p-4 rounded">
      <h2 className="text-xl font-bold mb-4">Extracted SLA Data</h2>
      <table className="table-auto w-full">
        <tbody>
          <tr>
            <td className="font-semibold">Document Type</td>
            <td>{data.documentType}</td>
          </tr>
          <tr>
            <td className="font-semibold">Document Date</td>
            <td>{data.documentDate}</td>
          </tr>
          <tr>
            <td className="font-semibold">Contract Number</td>
            <td>{data.contractNumber}</td>
          </tr>
        </tbody>
      </table>
      <button className="mt-4 bg-gray-700 text-white px-4 py-2 rounded">
        Export JSON
      </button>
    </div>
  );
}