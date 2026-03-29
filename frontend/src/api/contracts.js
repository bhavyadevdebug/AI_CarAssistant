import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

// Create a contract
export async function createContract() {
  const response = await axios.post(`${BASE_URL}/contracts/`, {
    dealer_offer_name: "Dealer A",
    vin: "1234567890",
    terms: "Lease terms here",
  });
  return response.data.contract_id;
}

// Attach SLA
export async function attachSLA(contractId) {
  const response = await axios.post(`${BASE_URL}/contracts/${contractId}/sla`, {
    apr_percent: 5.5,
    term_months: 36,
    monthly_payment: 299.99,
    down_payment: 2000,
    early_termination_fee: 500,
    mileage_allowance_yr: 12000,
    red_flags: "High APR",
  });
  return response.data.sla_id;
}

// Fetch SLA
export async function fetchSLA(contractId) {
  const response = await axios.get(`${BASE_URL}/contracts/${contractId}/sla`);
  return response.data;
}