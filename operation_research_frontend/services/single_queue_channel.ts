import { api } from "./api";

export const solveSingleQueuingTheory = async (average_time, intensity) =>
    await api.post(`queue/single_channel?average_time=${average_time}&intensity=${intensity}`);
