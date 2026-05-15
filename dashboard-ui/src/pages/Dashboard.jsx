import { useEffect, useState } from "react";

import { connectWebSocket } from "../sockets/ws";

import TemperatureChart from "../charts/TemperatureChart";
import VibrationChart from "../charts/VibrationChart";

import AlertBox from "../components/AlertBox";

export default function Dashboard() {

  const [data, setData] = useState([]);

  const [alerts, setAlerts] = useState([]);

  useEffect(() => {

    const ws = connectWebSocket((msg) => {

      const sensor = msg.sensor;

      const prediction = msg.prediction;

      const formatted = {
        ...sensor,
        anomaly: prediction.anomaly,
        timestamp: new Date().toLocaleTimeString()
      };

      setData((prev) => [...prev.slice(-20), formatted]);

      if (prediction.anomaly === 1) {

        setAlerts((prev) => [...prev, formatted]);
      }
    });

    return () => ws.close();

  }, []);

  return (
    <div className="p-6 grid grid-cols-3 gap-4">

      <div className="col-span-2 space-y-4">

        <TemperatureChart data={data} />

        <VibrationChart data={data} />

      </div>

      <div>

        <AlertBox alerts={alerts} />

      </div>

    </div>
  );
}