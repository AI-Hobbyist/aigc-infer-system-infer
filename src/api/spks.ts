import axios from "./axios"

export default async () => {
    if(import.meta.env.DEV) return ["纳西妲"]
    const { data } = await axios("/spks")
    return data;
}