import gradio as gr
from requests import get, post
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
    
with gr.Blocks() as app:
    speakers = get_speaker_list()
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
            gr.Markdown("# <center>接口调用</center>")
            gr.Markdown("## 注意事项")
            gr.Markdown("<font size=3>1. 请先获取访问令牌，再进行合成。可前往 [https://getkey.acgnai.top/](https://getkey.acgnai.top/) 获取<br>2. 提交内容均为 json 格式，别搞错了！</font>")
            gr.Markdown("## 获取角色列表")
            gr.Markdown("<font size=3>**请求地址**：`https://infer.acgnai.top/infer/spks`<br>**请求方式**：`GET`<br>**请求头**：`content-type: application/json`<br>**请求示例**：</font>")
            gr.Markdown("```javascript\n{\n\t\"type\": \"tts\",\n\t\"brand\": \"bert-vits2\",\n\t\"name\": \"sr\"\n}\n```")
            gr.Markdown("**<font size=3>返回说明</font>**")
            gr.Markdown("<font size=3>**message**：返回信息<br>**spklist**：角色列表</font>")
            gr.Markdown("**<font size=3>返回示例</font>**")
            gr.Markdown("```javascript\n{\n\t\"message\": \"说话人列表获取成功！\",\n\t\"spklist\": [\n\t\t\"「信使」【中】\",\n\t\t\"「信使」【日】\",\n\t\t\"「信使」【英】\",\n\t\t\"三月七【中】\",\n\t\t\"三月七【日】\",\n\t\t\"三月七【英】\",\n\t\t\"...\",\n\t\t\"黑天鹅【英】\"\n\t]\n}\n```")
            gr.Markdown("## 推理")
            gr.Markdown("<font size=3>**请求地址**：`https://infer.acgnai.top/infer/gen`<br>**请求方式**：`POST`<br>**请求头**：`content-type: application/json`<br>**请求示例**：</font>")
            gr.Markdown("```javascript\n{\n\t\"access_token\": \"你的访问令牌\",\n\t\"type\": \"tts\",\n\t\"brand\": \"bert-vits2\",\n\t\"name\": \"sr\",\n\t\"prarm\": {\n\t\t\"speaker\": \"三月七【中】\",\n\t\t\"text\": \"测试语音合成。\",\n\t\t\"sdp_ratio\": 0.2,\n\t\t\"noise_scale\": 0.6,\n\t\t\"noise_scale_w\": 0.9,\n\t\t\"length_scale\": 1.0,\n\t\t\"language\": \"ZH\",\n\t\t\"cut_by_sent\": true,\n\t\t\"interval_between_sent\": 0.2,\n\t\t\"interval_between_para\": 1.0,\n\t\t\"style_text\": \"我很开心！！！\",\n\t\t\"style_weight\": 0.7\n\t}\n}\n```")
            gr.Markdown("## 参数说明")
            gr.Markdown("<font size=3>**access_token**：访问令牌<br>**speaker**：角色<br>**text**：要合成的文本<br>**language**：语言（可选：ZH、JP、EN、mix、auto）<br>**style_text**：风格文本<br>**style_weight**：风格权重（范围：0.0 ~ 1.0）<br>**cut_by_sent**：是否按句切分（可选：true、false）<br>**interval_between_sent**：每句间隔（范围：0.1 ~ 2.0，单位：秒）<br>**interval_between_para**：每段间隔（范围：0.1 ~ 2.0，单位：秒）<br>**sdp_ratio**：SDP/DP 混合比（范围：0.0 ~ 2.0）<br>**noise_scale**：感情（范围：0.1 ~ 2.0）<br>**noise_scale_w**：音素长度（范围：0.1 ~ 2.0）<br>**length_scale**：语速（范围：0.1 ~ 2.0）</font>")
            gr.Markdown("## 返回说明")
            gr.Markdown("<font size=3>**audio**：音频url，若合成失败则返回 None<br>**message**：返回信息</font>")
            gr.Markdown("## 返回示例")
            gr.Markdown("```javascript\n{\n\t\"message\": \"合成成功!\",\n\t\"audio\": \"https://sr21-bv-infer.ai-lab.top/3d185846f2290c73dd427d3a65cda40c.wav\"\n}\n```")

    
app.queue(default_concurrency_limit=1)
app.launch(show_api=False,server_port=12346)