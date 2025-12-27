import { useEffect, useState } from "react";
import { getBench, deleteBench } from "../api/api";

export default function Bench() {
  const [bench, setBench] = useState([]);

  useEffect(() => {
    loadBench();
  }, []);

  const loadBench = async () => {
    const res = await getBench();
    setBench(res.data);
  };

  const remove = async (id) => {
    await deleteBench(id);
    loadBench();
  };

  return (
    <div>
      <h2>Bench</h2>

      <table border="1">
        <thead>
          <tr>
            <th>Name</th>
            <th>Skills</th>
            <th>Experience</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {bench.map((b) => (
            <tr key={b.id}>
              <td>{b.name}</td>
              <td>{b.primary_skills}</td>
              <td>{b.experience_years}</td>
              <td>
                <button onClick={() => remove(b.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
