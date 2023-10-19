import axios from "./axios"

export default async () => {
    const { data } = await axios.get("https://tirs.ai-lab.top/spklist/spks.json")
    return data;
}