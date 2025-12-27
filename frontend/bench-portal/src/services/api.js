import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";
export const getBench = () => axios.get(`${API_BASE}/bench`);
export const getDemands = () => axios.get(`${API_BASE}/demand`);


