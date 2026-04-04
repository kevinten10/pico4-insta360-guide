# PICO 4 VR 项目工具箱 👓

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Device: PICO 4](https://img.shields.io/badge/Device-PICO%204-blue.svg)](https://www.picoxr.com/)
[![Camera: Insta360](https://img.shields.io/badge/Camera-Insta360-red.svg)](https://www.insta360.com/)
[![AI-Powered](https://img.shields.io/badge/AI-Powered-green.svg)](https://github.com/kevinten-ai)

[中文](README.md) | [English](#english-version)

---

## ℹ️ 项目简介

这是一个全面的 **PICO 4 VR 开发和元宇宙探索工具箱**，包含：

- 🎬 **Insta360视频自动转换与同步** - 原始功能
- 📚 **元宇宙与VR开发学习资源** - 新增！
- 🤖 **AI驱动的VR内容生成** - 新增！
- 💻 **Unity开发示例代码** - 新增！

---

## 🚀 核心功能

### 1. 📂 视频转换与同步
- **自动转换**：将 Insta360 `.insv` 文件转换为全景 `.mp4`
- **自动同步**：通过 ADB 自动推送到 PICO 4
- **主入口**：`python main.py` 一站式操作

### 2. 📚 学习资源库
完整的学习路径，包含：
- `learning/01_metaverse_introduction.md` - 元宇宙入门
- `learning/02_vr_development_basics.md` - VR开发基础
- `learning/03_advanced_topics.md` - VR高级主题

### 3. 🤖 AI内容生成
- **VR场景生成**：森林、太空、海滩等主题
- **虚拟形象生成**：随机Avatar生成器
- **VR故事生成**：冒险、悬疑、奇幻、科幻剧本
- **Unity脚本自动生成**：快速启动项目

### 4. 💻 Unity示例代码
- `examples/unity/HelloPICO.cs` - 基础控制器交互
- `examples/unity/VRMovement.cs` - 移动与传送系统

### 5. ⚙️ 配置系统
- YAML配置文件支持
- 可自定义所有参数

---

## 🎯 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行主程序
```bash
python main.py
```
或使用命令行参数：
```bash
python main.py convert   # 转换视频
python main.py sync      # 同步到PICO
python main.py ai        # 生成AI内容
python main.py learn     # 查看学习资源
python main.py all       # 执行全部
```

### 3. 学习路径
1. 阅读 `tutorials/01_quick_start.md` 快速入门
2. 浏览 `learning/` 目录深入学习
3. 参考 `examples/unity/` 开始开发

---

## 📊 项目结构

```
vr/
├── main.py                    # 主入口程序
├── convert_360.py            # 视频转换脚本
├── sync_to_pico.py           # 设备同步脚本
├── requirements.txt           # Python依赖
├── config/                    # 配置目录
│   ├── config.yaml           # 主配置文件
│   └── config_loader.py      # 配置加载器
├── learning/                  # 学习资源
│   ├── 01_metaverse_introduction.md
│   ├── 02_vr_development_basics.md
│   └── 03_advanced_topics.md
├── ai_content/                # AI内容生成
│   ├── vr_scene_generator.py
│   ├── avatar_generator.py
│   ├── story_generator.py
│   ├── generated/            # 生成的场景
│   ├── avatars/              # 生成的Avatar
│   └── stories/              # 生成的故事
├── examples/                  # 示例代码
│   └── unity/
├── tutorials/                 # 教程
├── raw/                       # 原始视频输入
└── exports/                   # 转换后视频输出
```

---

## 🛠️ 技术栈

| 类别 | 技术 |
| :--- | :--- |
| **VR设备** | PICO 4 |
| **相机** | Insta360 X3/X4 |
| **开发引擎** | Unity 3D |
| **视频处理** | FFmpeg |
| **设备通信** | ADB |
| **编程语言** | Python 3.x, C# |
| **配置格式** | YAML |

---

<a name="english-version"></a>
## 🌐 English Version

### Comprehensive PICO 4 VR Toolkit
This project provides a complete toolkit for PICO 4 VR development, metaverse exploration, and AI-powered content creation.

### Key Features
1.  **Insta360 Video Pipeline**: Convert and sync videos automatically
2.  **Learning Resources**: Metaverse and VR development tutorials
3.  **AI Content Generation**: VR scenes, avatars, and story scripts
4.  **Unity Examples**: Ready-to-use VR code samples

### Quick Start
```bash
pip install -r requirements.txt
python main.py
```

### Prerequisites
- Python 3.x
- FFmpeg (for video stitching)
- ADB (for device sync)
- Unity 3D (for VR development)

---

## 🤝 贡献与支持

欢迎提交 Issue 或 Pull Request 来改进此项目！

- Maintainer: [kevinten-ai](https://github.com/kevinten-ai)

---

## 📝 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件
