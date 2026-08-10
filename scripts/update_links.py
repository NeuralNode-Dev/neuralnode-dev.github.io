import os
import re
import random
import datetime
import requests
from typing import List, Tuple

# --------------------------------------------------------------------------------
# NeuralNode-Dev 自动化节点池检测与分发引擎
# --------------------------------------------------------------------------------

# 官方与公共优选节点池
SOURCES: List[Tuple[str, str, str]] = [
    # (源名称, 订阅链接, 协议类型)
    ("NeuralNode Official Clash", "https://raw.githubusercontent.com/NeuralNode-Dev/NeuralNode-Dev/main/links/clash.yaml", "clash"),
    ("NeuralNode Official V2Ray", "https://raw.githubusercontent.com/NeuralNode-Dev/NeuralNode-Dev/main/links/v2.txt", "v2rayn"),

    ("Public FreeFQ Node Pool", "https://raw.githubusercontent.com/freefq/free/master/v2", "v2rayn")
]

# 请求伪装标头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 NeuralNode/2.0"
}

def check_link_availability(url: str) -> bool:
    """
    轻量级网络连通性校验 (支持 HEAD 请求与 GET Stream Fallback)
    """
    try:
        res = requests.head(url, headers=HEADERS, timeout=8, allow_redirects=True)
        if res.status_code == 200:
            return True
        res_get = requests.get(url, headers=HEADERS, timeout=8, stream=True)
        return res_get.status_code == 200
    except Exception as err:
        print(f"⚠️ [节点池访问异常] {url}: {err}")
        return False

def build_node_pool_markdown() -> str:
    """生成全新的节点池 Markdown 模块"""
    valid_clash: List[str] = []
    valid_v2ray: List[str] = []

    print("⚡ [NeuralNode Engine] 开始巡检节点池状态...")
    for name, url, type_ in SOURCES:
        if check_link_availability(url):
            print(f"  [OK] 有效源: {name}")
            if type_ == "clash":
                valid_clash.append(url)
            else:
                valid_v2ray.append(url)
        else:
            print(f"  [FAIL] 连通测试未通过: {name}")

    if valid_clash:
        random.shuffle(valid_clash)
    if valid_v2ray:
        random.shuffle(valid_v2ray)

    official_clash = "https://raw.githubusercontent.com/NeuralNode-Dev/NeuralNode-Dev/main/links/clash.yaml"
    official_v2ray = "https://raw.githubusercontent.com/NeuralNode-Dev/NeuralNode-Dev/main/links/v2.txt"


    # 构建全新的节点展示模块
    md = ""
    
    # 智能优选主推荐
    md += "#### 🚀 1. NeuralNode 智能优选主订阅 (Clash / Meta / Verge)\n"
    md += "每日自动检测连通性并随机优选路由，适合作为客户端主订阅使用：\n"
    md += "```yaml\n"
    md += f"{official_clash}\n"
    md += "```\n\n"

    # Clash 订阅集合
    md += "#### ⚡ 2. Clash 配置文件订阅库 (.yaml)\n"
    md += "支持 Clash Verge Rev, Clash for Windows, ClashX Meta, Shadowrocket, Stash：\n"
    md += "```yaml\n"
    md += f"{official_clash}\n"
    for link in valid_clash:
        if link != official_clash:
            md += f"{link}\n"
    md += "```\n\n"

    # Universal / Base64 订阅集合
    md += "#### 🌐 3. 通用协议Base64 订阅库 (v2rayN / Sing-box / 小火箭)\n"
    md += "支持 v2rayN, Shadowrocket, v2rayNG, Quantumult X, Sing-box：\n"
    md += "```text\n"
    md += f"{official_v2ray}\n"
    for link in valid_v2ray:
        if link != official_v2ray:
            md += f"{link}\n"
    md += "```\n"

    return md

def update_readme() -> None:
    """更新 README.md 的日期与节点池模块"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))
    readme_path = os.path.join(repo_root, "README.md")


    if not os.path.exists(readme_path):
        print(f"❌ 找不到 README.md: {readme_path}")
        return

    # UTC+8 时间
    tz_beijing = datetime.timezone(datetime.timedelta(hours=8))
    today_str = datetime.datetime.now(tz_beijing).strftime('%Y.%m.%d')

    node_pool_md = build_node_pool_markdown()

    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 替换更新日期
        content = re.sub(
            r'<!-- DATE_START -->.*?<!-- DATE_END -->',
            f'<!-- DATE_START -->{today_str}<!-- DATE_END -->',
            content
        )

        # 替换节点池模块
        content = re.sub(
            r'<!-- LINK_POOL_START -->[\s\S]*?<!-- LINK_POOL_END -->',
            f'<!-- LINK_POOL_START -->\n{node_pool_md}\n<!-- LINK_POOL_END -->',
            content
        )

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✨ [NeuralNode Engine] README.md 自动化更新完成 ({today_str})")

    except Exception as e:
        print(f"❌ 更新 README.md 过程出错: {e}")

if __name__ == "__main__":
    update_readme()
