import { nlp_api } from "./api";

export const paraphraseInRussian = async (data: Array<string>) =>
    await nlp_api.post(`paraphrase_ru`, data = data);

export const paraphraseInEnglish = async (data: Array<string>) =>
    await nlp_api.post(`paraphrase`, data = data);