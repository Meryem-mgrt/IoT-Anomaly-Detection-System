import { useState } from "react";
import { api } from "../api/http";

export default function Register() {

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const register = async () => {

    try {

      await api.post("/auth/register", {
        username,
        email,
        password
      });

      alert("User created");

    } catch (err) {

      console.error(err);

      alert("Register failed");
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
          placeholder="email"
          className="border p-2 w-full"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          placeholder="password"
          type="password"
          className="border p-2 w-full"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={register}
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          Register
        </button>

      </div>
    </div>
  );
}