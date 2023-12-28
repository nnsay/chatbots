# 安装依赖

```bash
# 仅第一次使用
python -m venv .bot

# 激活虚拟环境
source .bot/bin/activate

# 安装依赖
pip install -r requirements.txt
```

# 启动聊天

- 无会话

```bash
python oncebot.py
```

- 有会话

```bash
python chatbot.py
```

# 其他

- 生成 requirements

  ```bash
  pipreqs . --force --ignore .bot
  ```
