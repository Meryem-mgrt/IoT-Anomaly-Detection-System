import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function TemperatureChart({ data }) {
  return (
    <div className="bg-white p-4 rounded-xl shadow">
      <h2>Temperature Live</h2>

      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="temperature" stroke="#ff4d4d" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}