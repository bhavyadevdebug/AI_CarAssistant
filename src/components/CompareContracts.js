export default function CompareContracts() {
  // Demo data for now
  const contracts = [
    { brand: "BMW", mileage: "10,000 km/year", penalty: "₹5/km" },
    { brand: "Audi", mileage: "12,000 km/year", penalty: "₹4/km" },
  ];

  return (
    <div className="border p-4 rounded">
      <h2 className="text-xl font-bold mb-4">Compare Contracts</h2>
      <table className="table-auto w-full border">
        <thead>
          <tr>
            <th className="border px-4 py-2">Brand</th>
            <th className="border px-4 py-2">Mileage Limit</th>
            <th className="border px-4 py-2">Penalty</th>
          </tr>
        </thead>
        <tbody>
          {contracts.map((c, i) => (
            <tr key={i}>
              <td className="border px-4 py-2">{c.brand}</td>
              <td className="border px-4 py-2">{c.mileage}</td>
              <td className="border px-4 py-2">{c.penalty}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}