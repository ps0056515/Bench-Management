import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav>
      <Link to="/">Dashboard</Link> |{" "}
      <Link to="/bench">Bench</Link> |{" "}
      <Link to="/demand">Demand</Link> |{" "}
      <Link to="/match">Match</Link>
    </nav>
  );
}
