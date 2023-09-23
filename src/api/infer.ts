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
    document.title = "[正在合成] 原神/星穹铁道语音合成 - AI-Hobbyist"
    const { data } = await axios.post("https://tts.ai-lab.top", param)
    document.title = "[合成完毕!] 原神/星穹铁道语音合成 - AI-Hobbyist"
    let tmp_handler: any;
    window.addEventListener("blur", tmp_handler = () => {
        document.title = "原神/星穹铁道语音合成 - AI-Hobbyist"
        window.removeEventListener("blur", tmp_handler)
    })
    return data;
}