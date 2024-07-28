import gradio as gr
from requests import get, post
from pathlib import Path
import json
api = "https://infer.acgnai.top"

def get_speaker_list():
    headers = {"content-type": "application/json"}
    content = {"type": "tts", "brand": "gpt-sovits", "name": "anime"}
    response = get(f"{api}/infer/spks", headers=headers,data=json.dumps(content))
    data = json.loads(response.text)
    return data["spklist"]

def refresh_spk_list():
    global spk_list
    spk_list = get_speaker_list()
    gr.Info("角色以及情感列表已刷新！")

spk_list = get_speaker_list()
speakers = list(spk_list.keys())
emotions = list(set([emotion for emotions in spk_list.values() for emotion in emotions]))

def update_emotions(speaker):
    return gr.update(choices=spk_list[speaker])

def infer(access_token, speaker, emotion, text, text_language, top_k, top_p, temperature, speed):
    headers = {"content-type": "application/json"}
    content = {
        "type": "tts",
        "brand": "gpt-sovits",
        "name": "anime",
        "method": "webui",
        "access_token": access_token,
        "prarm": {
            "speaker": speaker,
            "emotion": emotion,
            "text": text,
            "text_language": text_language,
            "top_k": top_k,
            "top_p": top_p,
            "temperature": temperature,
            "speed": speed
        }
    }
    response = post(f"{api}/infer/gen", headers=headers, data=json.dumps(content))
    res = json.loads(response.text)
    if res["audio"] is None:
        gr.Warning(res["message"])
        audio = None
    else:
        gr.Info(res["message"])
        audio = res["audio"]
    return audio

def read_markdown(file):
    content = Path(file).read_text(encoding="utf-8")
    return content
    
with gr.Blocks(title="原神、星穹铁道、鸣潮语音合成") as app:
    gr.Markdown("## <center>原神 & 星穹铁道 & 鸣潮 [GPT-Sovits](https://github.com/RVC-Boss/GPT-SoVITS) 在线语音合成</center>")
    with gr.Tabs(selected="接口调用"):
        with gr.TabItem("推理"):
            with gr.Row():
                with gr.Tab(label="访问令牌"):
                    gr.Markdown("**获取访问令牌：**[https://getkey.acgnai.top/](https://getkey.acgnai.top/)")
                    acccess_token = gr.Textbox(max_lines=1, label="访问令牌", placeholder="请输入你的访问令牌", show_label=False,type="password")
            with gr.Row():
                with gr.Column(scale=6):
                    with gr.Tab(label="要合成的文本"):
                        text = gr.TextArea(lines=19, label="要合成的文本", placeholder="请输入要合成的文本", show_label=False)
                with gr.Column(scale=2):
                    with gr.Tab(label="合成选项"):
                        with gr.Row():
                            with gr.Tab(label="角色与情感"):
                                with gr.Row():
                                    speaker = gr.Dropdown(label="角色",choices=speakers,interactive=True,value=speakers[0]),
                                    emotion = gr.Dropdown(label="情感",choices=emotions,interactive=True,value="中立")
                                    get_spk = gr.Button("刷新角色与情感列表", variant="primary")
                                    speaker[0].change(update_emotions, inputs=speaker[0], outputs=emotion)
                                    get_spk.click(refresh_spk_list)
                        with gr.Row():
                            with gr.Tab(label="语言设置"):
                                with gr.Row():
                                    language = gr.Dropdown(label="语言",choices=["中文","英语","日语","中英混合","日英混合","自动检测"],value="中文",interactive=True)
            audio = gr.Audio(label="合成结果", interactive=False)
            with gr.Row():
                        
                with gr.Column(scale=6):
                    with gr.Tab(label="合成参数"):
                        with gr.Row():
                            top_k = gr.Slider(label="前k个采样（Top-k）",minimum=1,maximum=100,step=1,value=10,interactive=True)
                            top_p = gr.Slider(label="累计概率采样 (Top-p)",minimum=0.01,maximum=1.0,step=0.01,value=1.0,interactive=True)
                        with gr.Row():
                            temperature = gr.Slider(label="温度系数 (Temperature)",minimum=0.01,maximum=1,step=0.01,value=1.0,interactive=True)
                            speed = gr.Slider(label="语速（0.5为半速，1.0为正常速度，1.5为1.5倍速，以此类推）",minimum=0.01,maximum=2.0,step=0.01,value=1.0,interactive=True)
            submit = gr.Button("一键合成！", variant="primary")
            submit.click(infer,inputs=[acccess_token,speaker[0],emotion,text,language,top_k,top_p,temperature,speed],outputs=audio)
                            
        with gr.TabItem("接口调用"):
            gr.Markdown(value=read_markdown("./docs/gpt-sovits.md"))

    
app.queue(default_concurrency_limit=1)
app.launch(show_api=False,server_port=12348)