# 注意事项

1. 请先获取访问令牌，再进行合成，可前往 https://getkey.acgnai.top/ 获取
2. 提交内容均为 json 格式，别搞错了！

# 请求角色列表

### 角色列表

**请求地址**：`https://infer.acgnai.top/infer/spks`

**请求方式**：`GET`

**请求头**：`content-type: application/json`

**请求示例**：

```javascript
{
        "type": "tts",
        "brand": "bert-vits2-cn",
        "name": "anime"
}
```

### **返回说明**

**message**：返回信息

**spklist**：角色列表

**返回示例**

```javascript
{
	"message": "说话人列表获取成功！",
	"spklist": [
		"「信使」【星穹铁道】",
		"「博士」【原神】",
		"「大肉丸」【原神】",
		"「女士」【原神】",
		"「梦主」【星穹铁道】",
		"「白老先生」【原神】",
		"「花角玉将」【原神】",
		"「角」【鸣潮】",
        	"更多说话人...",
		"龙二【原神】"
     ]
}
```

# 请求推理

### 推理

**请求地址**：`https://infer.acgnai.top/infer/gen`

**请求方式**：`POST`

**请求头**：`content-type: application/json`

**请求示例**：

```javascript
{
    "access_token": "你的访问令牌",
    "type": "tts",
    "brand": "bert-vits2-cn",
    "name": "anime",
    "prarm": {
        "speaker": "纳西妲【原神】",
        "text": "测试语音合成。",
        "sdp_ratio": 0.5,
        "noise_scale": 0.6,
        "noise_scale_w": 0.9,
        "length_scale": 1.1,
        "cut_by_sent": true,
        "interval_between_sent": 0.2,
        "interval_between_para": 1.0,
        "text_prompt": "Normal"
    }
}
```

### 参数说明

**access_token**：访问令牌

**speaker**：角色

**text**：要合成的文本

**cut_by_sent**：是否按句切分（可选：true、false）

**interval_between_sent**：每句间隔（范围：0.1 ~ 2.0，单位：秒）

**interval_between_para**：每段间隔（范围：0.1 ~ 2.0，单位：秒）

**sdp_ratio**：SDP/DP 混合比（范围：0.0 ~ 2.0）

**noise_scale**：感情（范围：0.1 ~ 2.0）

**noise_scale_w**：音素长度（范围：0.1 ~ 2.0）

**length_scale**：语速（范围：0.1 ~ 2.0）

**text_prompt**：生成风格，如：Normal

### 返回说明

**audio**：音频url，若合成失败则返回 None

**message**：返回信息

### 返回示例

```javascript
{
        "message": "合成成功!",
        "audio": "https://sr21-bv-infer.ai-lab.top/3d185846f2290c73dd427d3a65cda40c.wav"
}
```