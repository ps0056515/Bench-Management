import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

/* =======================
   BENCH APIs
======================= */

export const getBench = () => {
  return API.get("/bench");
};

export const createBench = (data) => {
  return API.post("/bench", data);
};

export const updateBench = (id, data) => {
  return API.put(`/bench/${id}`, data);
};

export const deleteBench = (id) => {
  return API.delete(`/bench/${id}`);
};

/* =======================
   DEMAND APIs
======================= */

export const getDemands = () => {
  return API.get("/demand");
};

export const createDemand = (data) => {
  return API.post("/demand", data);
};

export const updateDemand = (id, data) => {
  return API.put(`/demand/${id}`, data);
};

export const deleteDemand = (id) => {
  return API.delete(`/demand/${id}`);
};

/* =======================
   MATCH API
======================= */

export const matchBenchToDemand = (demandId) => {
  return API.get(`/match/${demandId}`);

};
