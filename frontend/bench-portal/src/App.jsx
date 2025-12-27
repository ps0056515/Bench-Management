import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Bench from "./pages/Bench";
import Demand from "./pages/Demand";
import Match from "./pages/Match";

function App() {
  return (
    <Router>
      <div>
        {/* SIMPLE NAV */}
        <nav style={{ marginBottom: "20px" }}>
          <Link to="/">Dashboard</Link> |{" "}
          <Link to="/bench">Bench</Link> |{" "}
          <Link to="/demand">Demand</Link> |{" "}
          <Link to="/match">Match</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/bench" element={<Bench />} />
          <Route path="/demand" element={<Demand />} />
          <Route path="/match" element={<Match />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
