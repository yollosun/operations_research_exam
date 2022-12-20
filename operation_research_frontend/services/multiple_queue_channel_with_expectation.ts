import { api } from "./api";

export const solveMultiQueuingTheoryWithExpectation = async (requests_flow_rate, service_flow_rate, number_of_channels) =>
    await api.post(`queue/multi_channel_with_expectation?requests_flow_rate=${requests_flow_rate}&service_flow_rate=${service_flow_rate}&number_of_channels=${number_of_channels}`);