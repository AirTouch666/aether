# aether

![GitHub Release](https://img.shields.io/github/release/AirTouch666/aether)
![GitHub repo size](https://img.shields.io/github/repo-size/AirTouch666/aether)

[English](./README.md) | 简体中文

一个用于与各种 AI 模型交互的命令行工具。

## 安装

使用 `pip` 安装 `aether`：
```bash
pip install aether-cli
```


## 支持的模型

### OpenAI
- GPT-4 Turbo (`gpt-4`)
- GPT-4 Mini (`gpt-4-mini`)
- GPT-3.5 Turbo (`gpt-3.5`)

### Google
- Gemini Pro (`gemini-pro`)
- Gemini Pro Vision (`gemini-pro-vision`)
- Gemini Ultra (`gemini-ultra`)
- Gemini 2.0 Flash (`gemini-2-flash`)

### 其他
- Kimi (`kimi`)
- 通义千问 (`qwen`)
- 讯飞星火 (`spark`)

## 使用方法

### 设置模型的 API 密钥
```bash
ask set 模型名称 你的API密钥
```
例如：
```bash
ask set gpt-4 sk-xxxxxxxxx
```

### 切换模型
```bash
ask use 模型名称
```
例如：
```bash
ask use gpt-4
```

### 代理设置
#### 查看代理状态
```bash
ask proxy
```

#### 设置代理
```bash
ask proxy http://xxx.xx:xxxx
```
例如：
```bash
ask proxy http://127.0.0.1:7890
```

#### 关闭代理
```bash
ask proxy none
```

### 开始对话
```bash
ask
```
例如：
```bash
❱❱❱ ask
Chatting with kimi. Type '/bye' to quit.
>>> 你好
你好！有什么我可以帮你的吗？
>>> /bye
```

## 特性

- 支持多个 AI 模型
- 便捷的模型切换
- 代理支持
- 异步聊天界面
- 加载动画

## 许可证
本项目采用 MIT 许可证，查看 [LICENSE](./LICENSE) 了解更多信息。 