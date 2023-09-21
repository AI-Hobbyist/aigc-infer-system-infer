import axios from "./axios"

export default async () => {
    const { data } = await axios.get("https://tts.ai-lab.top/list")
    return data;
}