import { useEffect, useState } from "react";
import { getBench, getDemands } from "../api/api";

const Dashboard = () => {
  const [benchCount, setBenchCount] = useState(0);
  const [demandCount, setDemandCount] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    console.log("Dashboard useEffect started");

    Promise.all([getBench(), getDemands()])
      .then(([benchRes, demandRes]) => {
        setBenchCount(benchRes.data.length);
        setDemandCount(demandRes.data.length);
      })
      .catch((err) => {
        console.error("DASHBOARD ERROR", err);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading Dashboard...</p>;

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
};

export default Dashboard;
