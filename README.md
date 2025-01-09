# aether

![GitHub Release](https://img.shields.io/github/release/AirTouch666/aether)
![GitHub repo size](https://img.shields.io/github/repo-size/AirTouch666/aether)

English | [简体中文](./README-CN.md)

A command-line interface for interacting with various AI models.

## Installation

Install `aether` by using `pip`
```bash
pip install aether-cli
```


## Supported Models

### OpenAI
- GPT-4 Turbo (`gpt-4`)
- GPT-4 Mini (`gpt-4-mini`)
- GPT-3.5 Turbo (`gpt-3.5`)

### Google
- Gemini Pro (`gemini-pro`)
- Gemini Pro Vision (`gemini-pro-vision`)
- Gemini Ultra (`gemini-ultra`)
- Gemini 2.0 Flash (`gemini-2-flash`)

### Others
- Kimi (`kimi`)
- Qwen (`qwen`)
- Spark (`spark`)

## Usage

### Set API key for a model
```bash
ask set model-name your-api-key
```
For example,
```bash
ask set gpt-4 sk-xxxxxxxxx
```

### Switch to a model
```bash
ask use model-name
```
For example,
```bash
ask use gpt-4
```

### Proxy
#### View proxy status
```bash
ask proxy
```

#### Set proxy
```bash
ask proxy http://xxx.xx:xxxx
```
For example,
```bash
ask proxy http://127.0.0.1:7890
```

#### Disable proxy
```bash
ask proxy none
```

### Start chatting
```bash
ask
```
For example,
```bash
❱❱❱ ask
Chatting with kimi. Type '/bye' to quit.
>>> hi
Hi there! How can I assist you today? If you have any questions or need help with something, feel free to ask!
>>> /bye
```

## Features

- Multiple AI model support
- Easy model switching
- Proxy support
- Async chat interface
- Loading animation

## License
This project is licensed under the MIT License, see [LICENSE](./LICENSE)