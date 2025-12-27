import { useEffect, useState } from "react";
import { getBench, getDemands } from "./api/api";

function App() {
  const [benchCount, setBenchCount] = useState("INIT");
  const [demandCount, setDemandCount] = useState("INIT");

  useEffect(() => {
    console.log("Dashboard useEffect started");
    console.log("Dashboard useEffect started");
    console.log("Dashboard useEffect started");

    const loadDashboard = async () => {
      console.log("Calling getBench()");
      const bench = await getBench();
      console.log("Bench response:", bench);

      console.log("Calling getDemands()");
      const demand = await getDemands();
      console.log("Demand response:", demand);

      setBenchCount(bench.length);
      setDemandCount(demand.length);
    };

    // 🔥 THIS WAS MISSING 🔥
    loadDashboard();

  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Dashboard</h2>

      <p>
        <strong>Total Bench:</strong> {benchCount}
      </p>

      <p>
        <strong>Active Demands:</strong> {demandCount}
      </p>
    </div>
  );
}

export default App;
