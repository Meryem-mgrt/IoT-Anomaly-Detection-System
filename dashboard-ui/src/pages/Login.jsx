import { useState } from "react";
import { api } from "../api/http";

export default function Login() {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {

    try {

      const res = await api.post("/auth/login", {
        username,
        password,
      });

      localStorage.setItem("token", res.data.access_token);

      alert("Login success");

    } catch (err) {

      console.error(err);

      alert("Login failed");
    }
  };

  return (
    <div className="flex items-center justify-center h-screen">

      <div className="p-6 bg-white shadow rounded space-y-3">

        <input
          placeholder="username"
          className="border p-2 w-full"
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          placeholder="password"
          type="password"
          className="border p-2 w-full"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={login}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Login
        </button>

      </div>
    </div>
  );
}