# 1. 安装依赖

```bash
# 仅第一次使用
uv init --python 3.12

# 激活虚拟环境
uv add -r requirements.txt
```

# 2. 聊天

## 2.1 启动

- 无会话

```bash
uv run oncebot.py
```

![](https://raw.githubusercontent.com/nnsay/gist/main/img20231228184143.png)

- 有会话

```bash
uv run chatbot.py
```

![](https://raw.githubusercontent.com/nnsay/gist/main/img20231228183910.png)

## 2.2 退出

退出快捷键: Ctl + C

## 2.3 安装全局命令

克隆 repo 到本地, 进入 repo 执行下面的脚本

```bash
export GOOGLE_API_KEY=xxxx

pip install -r requirements.txt

mkdir -p $HOME/.local/bin
export PATH="$HOME/.local/bin:$PATH"

make install
```

![](https://raw.githubusercontent.com/nnsay/gist/main/img20231228190718.png)

## 2.4 调试

如果想要查看 langchain 的一些输出, 可以增加 DEBUG 环境变量, 例如:

```bash
DEBUG=1 python chatbot.py
```

# 3. 其他

- 生成 requirements

  ```bash
  pipreqs . --force --ignore .bot
  ```
