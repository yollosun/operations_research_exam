import { api } from "./api";

export const solveMultiQueuingTheoryWithRejection = async (average_time, intensity, number_of_channels) =>
    await api.post(`queue/multi_channel_with_rejection?average_time=${average_time}&intensity=${intensity}&number_of_channels=${number_of_channels}`);
