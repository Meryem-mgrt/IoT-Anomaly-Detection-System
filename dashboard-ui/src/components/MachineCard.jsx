export default function MachineCard({ data }) {
  return (
    <div className="p-4 bg-white shadow rounded">
      <h3>Machine: {data.machine_id}</h3>

      <p>Temperature: {data.temperature}</p>

      <p>Vibration: {data.vibration}</p>
    </div>
  );
}