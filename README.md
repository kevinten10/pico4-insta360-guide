# PICO 4 & Insta360 360° 视频观看指南 (Workflow Guide)

本项目旨在整理并自动化从 **Insta360 拍摄** 到 **PICO 4 VR 眼镜观看** 的完整工作流。

## 馃殗 工作流概览 (Standard Workflow)

1.  **录制 (Capture)**：使用 Insta360 (X3/X4/RS 等) 录制 5.7K 或更高分辨率的全景视频。
2.  **导出 (Export)**：使用 Insta360 Studio 将 `.insv` 转换为全景 `MP4`。
3.  **传输 (Transfer)**：通过 USB、Samba (飞屏) 或 NAS 将视频传输至 PICO 4。
4.  **观看 (Play)**：使用 PICO 内置播放器或 Skybox VR 进行 360°/180° 渲染播放。

---

## 馃搳 关键技术细节 (Technical Specs)

| 环节 | 推荐配置 / 设置 |
| :--- | :--- |
| **分辨率** | 推荐 5.7K (X3) 或 8K (X4) |
| **编码格式** | H.265 (HEVC) - PICO 4 硬件解码支持最佳 |
| **导出模式** | **Equirectangular (等距柱状投影)** |
| **码率** | 60Mbps - 100Mbps (保证 VR 沉浸感) |

---

## 馃搮 传输方案 (Connection Methods)

### A. 有线传输 (USB-C)
*   将 PICO 4 连接至 PC。
*   将文件放入 `Internal Shared Storage/Movies/` 目录。

### B. 无线飞屏 (Samba/DLNA)
*   PC 端开启“媒体流”或共享文件夹。
*   PICO 4 文件管理器 -> 网络 -> 添加设备。

### C. 自动化脚本 (WIP)
*   [ ] 计划开发 Python 脚本，自动监控导出文件夹并同步至 PICO 4。

---

## 馃敆 常见问题排查 (Troubleshooting)

*   **画面变扁平了？**
    *   在播放器设置中手动选择 `360°` 模式。
*   **画面太糊？**
    *   检查导出时是否选择了“平面”而非“全景”。
    *   VR 观看对分辨率要求极高，请务必导出 5.7K 及以上。

---

## 馃摓 项目维护
由 [kevinten-ai](https://github.com/kevinten-ai) 维护。
