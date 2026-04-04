# PICO 4 & Insta360 VR Workflow 👓

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Device: PICO 4](https://img.shields.io/badge/Device-PICO%204-blue.svg)](https://www.picoxr.com/)
[![Camera: Insta360](https://img.shields.io/badge/Camera-Insta360-red.svg)](https://www.insta360.com/)

[中文](README.md) | [English](#english-version)

---

## ℹ️ 项目简介
本项目致力于为 **Insta360** 用户提供在 **PICO 4 VR 眼镜**上观看全景视频的**全自动流水线**。

---

## 🚀 核心功能与自动化 (Features & Automation)

### 1. 📂 自动转换 (Auto-Convert) - **NEW!**
我们新增了基于 FFmpeg 的自动化转换脚本，可将原始 `.insv` 文件直接转换为全景 `.mp4`。
*   **脚本**：`python convert_360.py`
*   **输入**：将原始文件放入 `raw/` 文件夹。
*   **输出**：自动生成拼接好的全景视频至 `exports/`。

### 2. ⚡ 自动同步 (Auto-Sync)
监控 `exports/` 目录，一旦转换完成，立即通过 ADB 将视频推送到 PICO 4。
*   **脚本**：`python sync_to_pico.py`

### 3. 🛠️ 标准工作流 (The Pipeline)
1.  **录制**：使用 Insta360 拍摄。
2.  **拷贝**：将文件放入项目 `raw/` 目录。
3.  **运行**：`python convert_360.py && python sync_to_pico.py`
4.  **观看**：戴上 PICO 4 直接观看。

---

## 📊 参数矩阵与配置 (Tech Specs)

| 环节 | 推荐配置 |
| :--- | :--- |
| **分辨率** | 5.7K (X3) / 8K (X4) |
| **编码** | **H.265 (HEVC)** |
| **脚本依赖** | `ffmpeg` (需安装在系统路径) |

---

<a name="english-version"></a>
## 🌐 English Version

### Full-Auto Pipeline
1.  **Raw Input**: Put `.insv` files in `raw/`.
2.  **Process**: Run `convert_360.py` for stitching (FFmpeg v360).
3.  **Sync**: Run `sync_to_pico.py` for ADB transfer to PICO 4.

### Prerequisites
- Python 3.x
- FFmpeg (for stitching)
- ADB (for device sync)

---

## 🤝 贡献与支持
欢迎提交 Issue 或 Pull Request 来改进此指南！
- Maintainer: [kevinten-ai](https://github.com/kevinten-ai)
