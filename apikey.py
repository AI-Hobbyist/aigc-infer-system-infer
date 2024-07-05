import gradio as gr
import json, urllib
from webbrowser import open
from requests import post, get
api = "https://infer.acgnai.top"

def login_func(account,password):
    headers = {'Content-Type': 'application/json'}
    login = {"account": account, "password": password}
    resp = post(url=f"{api}/user/login",headers=headers,data=json.dumps(login))
    res = json.loads(resp.text)
    if res['user_token'] == 0:
        gr.Warning(res['message'])
    else:
        gr.Info(res['message'])
        gr.Info("现在可以到 获取访问令牌 那里获取自己的访问令牌了！")
        return res['user_token']
    
def get_user_info(user_token):
    if user_token is not None:
        headers = {'Content-Type': 'application/json'}
        user = {"user_token": user_token}
        resp = get(url=f"{api}/user",headers=headers,data=json.dumps(user))
        res = json.loads(resp.text)
        if res['uid'] is not None:
            if res['isadmin'] == 1:
                group = "管理员"
            else:
                group = "用户"
            urllib.request.urlretrieve(res['avatar'], f"./avatar/{res['uid']}.png")
            avatar = f"./avatar/{res['uid']}.png"
            return res['username'],res['email'],group,res['ip'],res['reg_time'],res['last_login'],avatar
    
def get_access_token(user_token):
    headers = {'Content-Type': 'application/json'}
    login = {"user_token": user_token}
    resp = post(url=f"{api}/user/token/access",headers=headers,data=json.dumps(login))
    res = json.loads(resp.text)
    if res['access_token'] == 0:
        gr.Warning(res['message'])
    else:
        gr.Info(res['message'])
        return res['access_token']

def open_website(link):
    open(str(link))
    
with gr.Blocks() as app:
    u_token = gr.State(0)
    with gr.Tabs():
        with gr.TabItem("登录"):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("")
                with gr.Column(scale=3):
                    with gr.Column(variant="panel"):
                        gr.Markdown("## <center>账号登录</center>")
                        gr.Markdown("<font size=3>[**注册账号**](https://reg.ai-hobbyist.com/)</font>")
                        acccount = gr.Textbox(label="账号",placeholder="请输入你的账号，邮箱和密码均可",max_lines=1)
                        password = gr.Textbox(label="密码",placeholder="请输入你的密码",max_lines=1,type="password")
                        login = gr.Button("登录")
                with gr.Column(scale=1):
                    gr.Markdown("")
        with gr.TabItem("获取访问令牌"):
                with gr.Row():
                    with gr.Tab("注意事项"):       
                        gr.Markdown("# <center>免责声明</center>")
                        gr.Markdown("<font size=4>合成内容如果出现了【任何 **版权** 或 **法律** 或 **其它相关** 的问题】，请使用者自行解决相关问题。与【项目开发者】、【模型训练者】、【数据集提供者】、【AI Hobbyist 组织】、【米哈游】无关！</font>")   
                        gr.Markdown("# <center>注意事项</center>")
                        gr.Markdown("<font size=4>1. 本模型所用头像，形象，语音等等的所有权均归米哈游所有。只可用于二次创作/配音。不得创作任何违反法律法规的内容，不得用于任何商业用途，不得二次配布；<br>2. 发视频请注明 **模型训练者** 、**整合包作者**（如果用到了整合包）、**在线推理链接**（如果用到了在线推理）；<br>3. 后续会添加更多的API支持；<br>4. 访问令牌仅显示一次，刷新后需要重新获取，所以生成后一定要保存到安全的位置</font>") 
                        gr.Markdown("# <center>相关信息</center>") 
                        gr.Markdown("<font size=4>**AI Hobbyist Github：**[https://github.com/AI-Hobbyist](https://github.com/AI-Hobbyist)<br>**AI Hobbyist 主页：**[https://www.ai-hobbyist.com](https://www.ai-hobbyist.com)<br>**模型训练：**[红血球AE3803](https://space.bilibili.com/6589795)<br>**后端开发：**[红血球AE3803](https://space.bilibili.com/6589795)<br>**所用数据集：**[原神 & 星穹铁道AI素材合集](https://www.bilibili.com/read/cv35926092)<br>**交流群：**[点击链接加入群聊【AI Hobbyist 交流群】](hhttps://qm.qq.com/q/Wk8BEF5ROC)</font>")               
                with gr.Row():
                    with gr.Tab("访问令牌"):
                        with gr.Row():
                            with gr.Column(scale=5):
                                access_token = gr.Textbox(label="访问令牌",interactive=False, max_lines=1)
                                update_token = gr.Button("刷新令牌",variant="primary")
                with gr.Row():
                    with gr.Tab("在线推理链接集合(点击访问)"):
                        with gr.Row():
                            url1 = gr.Button("星穹铁道Bert-Vits2多国语言版在线推理")
                            url2 = gr.Button("二游Bert-Vits2中文特化版在线推理")
                            url3 = gr.Button("待更新")
                            url4 = gr.Button("待更新")
                        with gr.Row():
                            url5 = gr.Button("待更新")
                            url6 = gr.Button("待更新")
                            url7 = gr.Button("待更新")
                            url8 = gr.Button("待更新")
    link1 = gr.State("https://bv2sr.acgnai.top")
    link2 = gr.State("https://bv-cn.acgnai.top")
    login.click(login_func,inputs=[acccount,password],outputs=[u_token])
    update_token.click(get_access_token,inputs=[u_token],outputs=[access_token])
    url1.click(open_website,inputs=[link1])
    url2.click(open_website,inputs=[link2])

app.queue(default_concurrency_limit=1)
app.launch(show_api=False,server_port=12345)