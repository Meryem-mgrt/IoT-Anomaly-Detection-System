export default function AlertBox({ alerts }) {
  return (
    <div className="bg-red-50 p-4 rounded-xl shadow">
      <h2 className="text-red-600 font-bold">Alerts</h2>

      <div className="space-y-2 mt-2">
        {alerts.map((a, i) => (
          <div key={i} className="bg-red-100 p-2 rounded">
            ⚠️ Machine {a.machine_id} anomaly detected
          </div>
        ))}
      </div>
    </div>
  );
}


