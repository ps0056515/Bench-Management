import { useState } from "react";
import { matchBenchToDemand } from "../api/api";

export default function Match() {
  const [demandId, setDemandId] = useState("");
  const [result, setResult] = useState(null);

  const match = async () => {
    const res = await matchBenchToDemand(demandId);
    setResult(res.data);
  };

  return (
    <div>
      <h2>Match</h2>

      <input
        type="number"
        placeholder="Demand ID"
        value={demandId}
        onChange={(e) => setDemandId(e.target.value)}
      />

      <button onClick={match}>Match</button>

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}
