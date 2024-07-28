import gradio as gr
from requests import get, post
from pathlib import Path
import json
api = "https://infer.acgnai.top"

def get_speaker_list():
    headers = {"content-type": "application/json"}
    content = {"type": "tts", "brand": "bert-vits2", "name": "sr"}
    response = get(f"{api}/infer/spks", headers=headers,data=json.dumps(content))
    data = json.loads(response.text)
    return data["spklist"]

def infer(access_token, text, speaker, language, style_text, style_weight, cut_by_sent, interval_between_sent, interval_between_para, sdp_ratio, noise_scale, noise_scale_w, length_scale):
    lang = ["ZH","JP","EN","mix","auto"][["中文","日语","英语","多语种混合","自动检测语言"].index(language)]
    speed = (100 - length_scale) / 100
    headers = {"content-type": "application/json"}
    content = {
        "type": "tts",
        "brand": "bert-vits2",
        "name": "sr",
        "method": "webui",
        "access_token": access_token,
        "prarm": {
            "text": text,
            "speaker": speaker,
            "language": lang,
            "style_text": style_text,
            "style_weight": style_weight,
            "cut_by_sent": cut_by_sent,
            "interval_between_sent": interval_between_sent,
            "interval_between_para": interval_between_para,
            "sdp_ratio": sdp_ratio,
            "noise_scale": noise_scale,
            "noise_scale_w": noise_scale_w,
            "length_scale": speed
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
    
with gr.Blocks(title="星穹铁道语音合成") as app:
    speakers = get_speaker_list()
    gr.Markdown("## <center>星穹铁道 [Bert-VITS2多国语言版](https://github.com/fishaudio/Bert-VITS2/releases/tag/v2.3) 在线语音合成</center>")
    with gr.Tabs(selected="接口调用"):
        with gr.TabItem("推理"):
            with gr.Row():
                with gr.Tab(label="访问令牌"):
                    gr.Markdown("**获取访问令牌：**[https://getkey.acgnai.top/](https://getkey.acgnai.top/)")
                    acccess_token = gr.Textbox(max_lines=1, label="访问令牌", placeholder="请输入你的访问令牌", show_label=False,type="password")
            with gr.Row():
                with gr.Column(scale=6):
                    with gr.Tab(label="要合成的文本"):
                        text = gr.TextArea(lines=15, label="要合成的文本", placeholder="请输入要合成的文本", show_label=False)
                        audio = gr.Audio(label="合成结果", interactive=False)
                with gr.Column(scale=2):
                    with gr.Tab(label="其它参数"):
                        with gr.Row():
                            with gr.Tab(label="风格参数"):
                                with gr.Row():
                                    style_text = gr.Textbox(max_lines=1, label="风格文本", placeholder="例如：我好开心！")
                                with gr.Row():
                                    style_weight = gr.Slider(label="风格权重",minimum=0,maximum=1,step=0.1,value=0.7,interactive=True)
                        with gr.Row():
                            with gr.Tab(label="切分参数"):
                                with gr.Row():
                                    cut_by_sent = gr.Checkbox(label="是否按句切分",value=False,interactive=True)
                                with gr.Row():
                                    interval_between_sent = gr.Slider(label="每句间隔(s)",minimum=0.1,maximum=2,step=0.1,value=0.2,interactive=True)
                                    interval_between_para = gr.Slider(label="每段间隔(s)",minimum=0.1,maximum=2,step=0.1,value=1.0,interactive=True)
            with gr.Row():
                with gr.Column(scale=1):
                    with gr.Tab(label="角色列表"):
                        speaker = gr.Dropdown(label="角色",show_label=False,choices=speakers,value=speakers[198],interactive=True),
                        language = gr.Dropdown(label="语言",choices=["中文","日语","英语","多语种混合","自动检测语言"],value="中文",interactive=True)
                with gr.Column(scale=6):
                    with gr.Tab(label="合成参数"):
                        with gr.Row():
                            sdp_ratio = gr.Slider(label="SDP/DP 混合比",minimum=0,maximum=1,step=0.1,value=0.5,interactive=True)
                            noise_scale = gr.Slider(label="感情",minimum=0.1,maximum=2,step=0.1,value=0.6,interactive=True)
                        with gr.Row():
                            noise_scale_w = gr.Slider(label="音素长度",minimum=0.1,maximum=2,step=0.1,value=0.8,interactive=True)
                            length_scale = gr.Slider(label="语速(%)",minimum=-99,maximum=99,step=0.1,value=0,interactive=True)
            submit = gr.Button("一键合成！", variant="primary")
            submit.click(infer,inputs=[acccess_token,text,speaker[0],language,style_text,style_weight,cut_by_sent,interval_between_sent,interval_between_para,sdp_ratio,noise_scale,noise_scale_w,length_scale],outputs=audio)
                            
        with gr.TabItem("接口调用"):
            gr.Markdown(value=read_markdown("./docs/bert-vits2.md"))

    
app.queue(default_concurrency_limit=1)
app.launch(show_api=False,server_port=12346)