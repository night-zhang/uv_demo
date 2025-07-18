from config import cfg
import os
import sys
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():
    env = os.environ.copy()
    env["DATABASE_URL"] = cfg.database_url

    if cfg.debug:
        print(f"env[DATABASE_URL] = {env['DATABASE_URL']}")

    # 执行 Prisma 命令（Python 版 Prisma）
    subprocess.run([
        "prisma", "db", "push"
    ], env=env)


if __name__ == "__main__":
    main()
