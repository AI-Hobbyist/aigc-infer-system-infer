# 注意事项

1. 请先获取访问令牌，再进行合成。可前往 https://getkey.acgnai.top/ 获取
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
        "brand": "gpt-sovits",
        "name": "anime"
}
```

### **返回说明**

**message**：返回信息

**spklist**：角色列表

### **返回示例**

```javascript
{
        "message": "说话人列表获取成功！",
        "spklist": {
		"温迪": [
			"生气",
			"吃惊",
			"难过",
			"中立",
			"厌恶",
			"开心",
			"恐惧"
		],
		"..."
	}
}
```

# 提交推理

### **推理**

**请求地址**：`https://infer.acgnai.top/infer/gen`

**请求方式**：`POST`

**请求头**：`content-type: application/json`

**请求示例**：

```javascript
{
        "access_token": "你的访问令牌",
        "type": "tts",
        "brand": "gpt-sovits",
        "name": "anime",
        "method": "api",
        "prarm": {
            "speaker": "芙宁娜",
            "emotion": "中立",
            "text": "测试语音合成。",
            "text_language":"中文",
            "text_split_method": "按标点符号切",
            "fragment_interval": 0.3,
            "batch_size": 1,
            "batch_threshold": 0.75,
            "parallel_infer": true,
            "split_bucket": true,
            "top_k": 10,
            "top_p": 1.0,
            "temperature": 1.0,
            "speed_factor": 1.0
    }
}
```

### **参数说明**
#### 基本参数

**access_token**：访问令牌

**speaker**：角色

**emotion**：情感（可从角色列表获取）

**text**：要合成的文本

**text_language**：语言（可选：中文、英语、日语、中英混合、日英混合、自动检测）

#### 切分方式

**text_split_method**：切分方式（可选：不切、凑四句一切、凑50字一切、按中文句号。切、按英文句号.切、按标点符号切）

**fragment_interval**：分段间隔（秒，范围：0.01 ~ 1.0）

#### 并行推理

**batch_size**：批量大小（范围：1 ~ 200）

**batch_threshold**：批处理阈值（范围：0.0 ~ 1.0）

**parallel_infer**：启用并行推理（True、False）

**split_bucket**：数据分桶（True、False）

#### 合成参数

**top_k**：前k个采样（范围：1 ~ 100）

**top_p**：累计概率采样（范围：0.01 ~ 1.0）

**temperature**：温度系数（范围：0.01 ~ 1.0）

**repetition_penalty**：重复惩罚（范围：0.0 ~ 2.0）

**speed_factor**：语速（范围：0.01 ~ 2.0）

### **返回说明**

**audio**：音频url，若合成失败则返回 None

**message**：返回信息

### **返回示例**

```javascript
{
        "message": "合成成功!",
        "audio": "https://gsv.ai-lab.top/3d185846f2290c73dd427d3a65cda40c.wav"
}
```