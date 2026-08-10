# 🚀 Clash Verge Rev 完全配置与使用教程 (含免费节点订阅)

本指南针对 Windows / macOS / Linux 平台下最流行的代理客户端 **Clash Verge Rev** 提供从零开始的配置与故障排查说明。

> 🔗 ** NeuralNode 官方开放订阅**：返回 [README 主页](https://github.com/NeuralNode-Dev/NeuralNode-Dev) 获取每日自动测速的免费 Clash 订阅。  
> ⭐ **优质高速专线推荐**：如需稳定解锁 4K 影音与 AIGC 工具，推荐使用经过认证的 [云猫网络 (Cloud Yuncat)](https://cloud.yuncat.top)，注册免费领 3 天试用。

---

## 🛠️ 一、Clash Verge Rev 客户端安装与中文设置

1. **客户端下载**：从官方发布页下载对应的系统安装包（Windows 推荐 `.msi` 或 `.exe` 安装版，macOS 下载 `.dmg`）。
2. **切换中文界面**：
   - 打开 Clash Verge Rev。
   - 点击左侧菜单栏 **「Settings」 (设置)**。
   - 在 **「Language」** 选项中切换为 **「简体中文」**。

---

## 🔗 二、订阅链接导入与节点选择

1. 复制你的 Clash 订阅链接（YAML 格式）：
   - 官方试用订阅：`https://cloud.yuncat.top`
   - 公益聚合订阅：`https://raw.githubusercontent.com/NeuralNode-Dev/NeuralNode-Dev/main/links/clash.yaml`

2. 打开 Clash Verge Rev，点击左侧菜单 **「订阅」 (Profiles)**。
3. 在顶部输入框粘贴订阅 URL，点击 **「导入」 (Import)**。
4. 导入成功后，鼠标**右键点击订阅卡片**，选择 **「启用」 (Use)**。
5. 点击左侧菜单 **「代理」 (Proxies)**，选择 **「Rule (规则模式)」** 并选择最快节点。
6. 点击左侧菜单 **「设置」 (Settings)**，开启 **「系统代理」 (System Proxy)**。

---

## ❓ 三、常见报错与故障排查

### 1. 导入订阅报错 `Download Failed` 或 `Invalid Config`
- 检查网络连通性，或尝试开启 GitHub 文件加速。
- 确认复制的 URL 是否包含非法空格或换行。

### 2. 启用代理后无法网页打开但 Telegram 正常
- 确认是否开启了「系统代理」。
- 右键 Clash Verge 选单，尝试开启 **「TUN 模式」**（需管理员权限）。

### 3. OpenAI / ChatGPT 访问提示 `Access Denied` 或 `IP Blocked`
- 公益公共节点 IP 易受限制，建议开启 **[云猫网络](https://cloud.yuncat.top)** 的 AIGC 专线节点进行访问。
