# 简介
学习uv管理项目


# 提前安装好uv相关组件
```shell
# 下载pipx，最好把uv用pipx安装到项目外的目录
python3 -m pip install --user pipx
# 安装uv，可能后续需要设置环境变量
pipx install uv
uv -V
```

# 同步虚拟环境
```shell
uv sync
```


# 数据库迁移
```shell
# Linux下激活虚拟环境
source .venv/bin/activate
# windows下激活虚拟环境
.venv\Scripts\activate
# prisma db push的命令默认只会去.env中获取数据库的配置，改为去basesting里获取
python -m scripts.prisma_push
```



# 运行
## uv运行
```shell
uv run uvicorn main:app --reload --port=8080
```



## pycharm设置运行
- 编辑运行配置
- 添加fastapi配置
- 选中main.py
- 额外参数填：`--reload --port=8080`

## vscode设置运行
- 创建.vscode/launch.json（没有则手动创建）
- 内容如下
```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI: Uvicorn",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",  // <-- 使用模块启动
      "args": [
        "main:app",          // "模块名:FastAPI实例名"
        "--reload",           // 开发模式自动重载
        "--port=8080"
      ],
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}

```


## 手动激活虚拟环境运行（不推荐）

```shell
# Linux下激活虚拟环境
source .venv/bin/activate
# windows下激活虚拟环境
.venv\Scripts\activate
uvicorn main:app --reload --port=8080
```


# 其它
生成秘钥
```shell
python -c "import secrets; print(secrets.token_urlsafe(32))"

# 或者
openssl rand -hex 32
```