import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function VibrationChart({ data }) {
  return (
    <div className="bg-white p-4 rounded-xl shadow">
      <h2>Vibration Live</h2>

      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="vibration" stroke="#3366ff" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}