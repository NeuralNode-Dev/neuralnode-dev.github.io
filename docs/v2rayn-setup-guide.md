# 💻 v2rayN 客户端配置与使用教程 (含订阅导入)

本教程适用于 Windows 操作系统下的经典代理工具 **v2rayN**，指导如何导入订阅、更新 Core 及排查常见错误。

> 🔗 ** NeuralNode 官方开放订阅**：返回 [README 主页](https://github.com/NeuralNode-Dev/NeuralNode-Dev) 获取每日自动测速的免费订阅。  
> ⭐ **优质高速专线推荐**：如需稳定解锁 4K 影音与 AIGC 工具，推荐使用经过认证的 [云猫网络 (Cloud Yuncat)](https://cloud.yuncat.top)，注册免费领 3 天试用。

---

## 🛠️ 一、v2rayN 下载与环境准备

1. **下载客户端**：在 GitHub release 下载包含内核的 `v2rayN-With-Core.zip` 解压包。
2. **解压运行**：解压至无中文路径的文件夹中，双击运行 `v2rayN.exe`。
3. **环境要求**：如提示缺少运行环境，需安装微软 `.NET Desktop Runtime`。

---

## 🔗 二、导入节点与订阅

1. 打开 v2rayN 主界面。
2. 点击顶部菜单栏 **「订阅分组」 -> 「订阅分组设置」**。
3. 点击左下角 **「添加」**：
   - 别名：`NeuralNode`
   - 可选地址 (URL)：粘贴订阅链接（如 `https://cloud.yuncat.top` 或 `https://raw.githubusercontent.com/NeuralNode-Dev/NeuralNode-Dev/main/links/v2.txt`）

4. 点击 **「保存」**。
5. 点击顶部菜单 **「订阅分组」 -> 「更新订阅」**，稍等片刻即可加载出完整节点列表。

---

## ⚡ 三、开启代理与测试

1. 选中要使用的节点，按键盘 `Enter` 回车键设为活动节点。
2. 在电脑右下角任务栏中，**右键图标**：
   - **清除系统代理 / 自动配置系统代理**：切换为 **「自动配置系统代理」** (图标变为红色)。
   - **路由**：选择 **「绕过大陆(IP) / GeoIP CN」**。

---

## ❓ 四、常见问题

- **报错 `系统代理开启失败`**：退出杀毒软件（如 360），重新以管理员身份运行 `v2rayN.exe`。
- **解锁 AI 与流媒体**：建议使用支持原生 IP 欺骗与分流的 [云猫网络 (Cloud Yuncat)](https://cloud.yuncat.top)。
