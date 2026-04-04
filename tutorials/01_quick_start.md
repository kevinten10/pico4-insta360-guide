# 快速入门指南

## 环境准备

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 安装必要工具
- **FFmpeg**: 用于视频转换
  - Windows: 下载并添加到PATH
  - Mac: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg`

- **ADB**: 用于与PICO设备通信
  - 下载 Android Platform Tools
  - 添加到系统PATH

## 基本使用

### 方法1: 使用主菜单
```bash
python main.py
```

### 方法2: 命令行参数
```bash
# 转换视频
python main.py convert

# 同步到PICO
python main.py sync

# 生成AI内容
python main.py ai

# 查看学习资源
python main.py learn

# 执行全部
python main.py all
```

## 工作流程

### 转换Insta360视频
1. 将 `.insv` 文件放入 `raw/` 目录
2. 运行 `python convert_360.py`
3. 转换后的视频保存在 `exports/` 目录

### 同步到PICO
1. 用USB连接PICO 4
2. 确保开启USB调试
3. 运行 `python sync_to_pico.py`
4. 文件会自动推送到PICO

### 生成AI内容
```bash
python main.py ai
```

这将生成：
- VR场景模板（森林、太空、海滩）
- 虚拟形象（Avatar）
- VR故事剧本（冒险、悬疑、奇幻、科幻）

## 下一步

- 阅读 `learning/` 目录下的学习资料
- 查看 `examples/` 目录下的示例代码
- 开始你的第一个VR项目！
