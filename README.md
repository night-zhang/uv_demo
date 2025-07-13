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
- 进行项目，执行
```shell
uv venv
```


# 运行
## uv运行
uv run uvicorn main:app --reload


## pycharm设置运行
- 编辑运行配置
- 添加fastapi配置
- 选中main.py

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
        "--reload"           // 开发模式自动重载
      ],
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}

```


## 手动激活虚拟环境运行（不推荐）
- source .venv/bin/activate
- uvicorn main:app --reload

