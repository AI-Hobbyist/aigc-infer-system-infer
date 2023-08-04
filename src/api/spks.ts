import axios from "./axios"

export default async () => {
    if(import.meta.env.DEV) return ["减佬","zzc","乱炖"]
    const { data } = await axios("/spks")
    return data;
}