# 1. 安装依赖

```bash
# 仅第一次使用
python -m venv .bot

# 激活虚拟环境
source .bot/bin/activate

# 安装依赖
pip install -r requirements.txt
```

# 2. 聊天

## 启动

- 无会话

```bash
python oncebot.py
```

![](https://raw.githubusercontent.com/nnsay/gist/main/img20231228184143.png)

- 有会话

```bash
python chatbot.py
```

![](https://raw.githubusercontent.com/nnsay/gist/main/img20231228183910.png)

## 退出

退出快捷键: Ctl + C

## 调试

如果想要查看 langchain 的一些输出, 可以增加 DEBUG 环境变量, 例如:

```bash
DEBUG=1 python chatbot.py
```

# 3. 其他

- 生成 requirements

  ```bash
  pipreqs . --force --ignore .bot
  ```
