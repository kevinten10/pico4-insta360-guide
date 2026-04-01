# PICO 4 & Insta360 VR Workflow 馃

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Device: PICO 4](https://img.shields.io/badge/Device-PICO%204-blue.svg)](https://www.picoxr.com/)
[![Camera: Insta360](https://img.shields.io/badge/Camera-Insta360-red.svg)](https://www.insta360.com/)

[中文](README.md) | [English](#english-version)

---

## 馃倴 项目简介
本项目致力于为 **Insta360** 用户提供在 **PICO 4 VR 眼镜**上观看 360°/180° 全景视频的最佳实践流程。包含全套导出参数、传输方案以及一个自动化的同步脚本。

---

## 馃殗 标准工作流 (Standard Workflow)

### 1. 录制 (Capture)
*   **设备建议**：Insta360 X3/X4, RS, EVO。
*   **设置**：使用 5.7K/30fps 或 8K/30fps (X4) 获得最佳沉浸感。

### 2. 导出 (Export)
*   **工具**：Insta360 Studio (PC)。
*   **编码**：**H.265 (HEVC)** —— 相比 H.264，在相同体积下提供更高画质。
*   **分辨率**：务必选 5.7K 或更高。
*   **视野**：选择 **Equirectangular (等距柱状投影)**。
*   **码率**：建议 100Mbps。

### 3. 自动同步 (Automated Sync) - **NEW!**
我们提供了一个 Python 监控脚本，可以将导出的 MP4 自动推送到连接的 PICO 4。
*   **安装依赖**：`pip install -r requirements.txt`
*   **运行脚本**：`python sync_to_pico.py`
*   **原理**：脚本监控 `exports/` 目录，通过 ADB 将新文件推送到 PICO 4 的 `Movies/` 文件夹。

### 4. 观看 (Play)
*   打开 PICO 4 “文件管理器”。
*   在播放设置中手动选择：**360°** / **2D** 或 **3D (上下/左右)**。

---

## 馃搳 参数矩阵 (Parameter Matrix)

| 视频类型 | 导出设置 | 播放器模式 | 推荐感官 |
| :--- | :--- | :--- | :--- |
| **360 全景** | 5.7K/H.265 | 360° / 2D | 馃専 极佳 |
| **180 3D** | 5.7K/H.265 | 180° / 3D (左右) | 馃 沉浸感强 |
| **常规视频** | 4K/H.264 | 2D / 巨幕模式 | 馃摴 电影感 |

---

<a name="english-version"></a>
## 馃倳 English Version

### Project Overview
A complete workflow and toolset for Insta360 content on PICO 4 VR.

### Key Features
- **Auto-Sync Script**: Uses Python and ADB to sync exports directly to your headset.
- **Optimization Guide**: Best export settings for H.265 5.7K+ playback.
- **Multi-method Transfer**: USB, Samba, and Automation.

### Quick Start
1. Connect PICO 4 with USB Debugging enabled.
2. Put your exported MP4 into the `exports/` folder.
3. Run `python sync_to_pico.py` for auto-transfer.

---

## 馃摓 贡献与支持
欢迎提交 Issue 或 Pull Request 来改进此指南！
- Maintainer: [kevinten-ai](https://github.com/kevinten-ai)
