import axios from "axios"

interface Param {
    token: string;
    speaker: string;
    text: string;
    sdp_ratio: number;
    noise: number;
    noisew: number;
    length: number;
}
export default async (param: Param) => {
    const { data } = await axios.post("https://tts.ai-lab.top", param)
    return data;
}