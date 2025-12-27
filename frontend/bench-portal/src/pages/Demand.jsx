import { useEffect, useState } from "react";
import { getDemands, deleteDemand } from "../api/api";

export default function Demand() {
  const [demands, setDemands] = useState([]);

  useEffect(() => {
    loadDemands();
  }, []);

  const loadDemands = async () => {
    const res = await getDemands();
    setDemands(res.data);
  };

  const remove = async (id) => {
    await deleteDemand(id);
    loadDemands();
  };

  return (
    <div>
      <h2>Demands</h2>

      <table border="1">
        <thead>
          <tr>
            <th>Project</th>
            <th>Skills</th>
            <th>Experience</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {demands.map((d) => (
            <tr key={d.id}>
              <td>{d.project_name}</td>
              <td>{d.required_skills}</td>
              <td>{d.min_experience}</td>
              <td>
                <button onClick={() => remove(d.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
