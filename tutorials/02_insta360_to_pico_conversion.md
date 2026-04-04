# Insta360视频到PICO VR视频转换完全指南

## 目录
1. [原理概述](#原理概述)
2. [前置准备](#前置准备)
3. [Insta360文件格式说明](#insta360文件格式说明)
4. [FFmpeg v360滤镜详解](#ffmpeg-v360滤镜详解)
5. [转换脚本使用](#转换脚本使用)
6. [高级配置](#高级配置)
7. [常见问题](#常见问题)

---

## 原理概述

### Insta360 相机工作原理
Insta360相机使用**双鱼眼镜头**（Dual Fisheye）同时捕捉两个180°视角的画面：
- 前置镜头（文件后缀通常为 `_00_`）
- 后置镜头（文件后缀通常为 `_10_`）

### 转换流程
```
Insta360 .insv 文件 (双鱼眼)
    ↓
[文件配对] 找到同一时刻的前后镜头文件
    ↓
[拼接] 使用 FFmpeg v360 滤镜拼接
    ↓
[投影] 转换为等距柱状投影 (Equirectangular)
    ↓
[编码] 使用 H.265 编码压缩
    ↓
PICO 可播放的 .mp4 文件
```

### PICO 4 视频要求
| 参数 | 推荐值 | 说明 |
|------|--------|------|
| 格式 | MP4 | 容器格式 |
| 视频编码 | H.264 / H.265 (HEVC) | H.265 更省空间 |
| 分辨率 | 4K-8K | 取决于源文件 |
| 帧率 | 30/60 fps | 与源文件保持一致 |
| 投影格式 | 等距柱状 (Equirectangular) | 360° 标准格式 |
| 音频 | AAC / MP3 | 立体声即可 |

---

## 前置准备

### 1. 安装 FFmpeg

#### Windows
1. 访问 [FFmpeg官网](https://ffmpeg.org/download.html)
2. 下载 Windows 编译版本（推荐 gyan.dev 或 BtbN）
3. 解压到 `C:\ffmpeg`
4. 添加到系统 PATH：
   - 右键"此电脑" → 属性 → 高级系统设置 → 环境变量
   - 在"系统变量"中找到 `Path`，点击编辑
   - 新建 → 添加 `C:\ffmpeg\bin`
5. 验证安装：
   ```powershell
   ffmpeg -version
   ```

#### Mac
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

### 2. 验证 FFmpeg v360 滤镜
```bash
ffmpeg -filters | grep v360
```
应该看到 `v360` 滤镜信息。

---

## Insta360文件格式说明

### 文件命名规则
Insta360 通常生成成对的文件：
```
VID_20240404_120000_00_001.insv  (前置镜头)
VID_20240404_120000_10_001.insv  (后置镜头)
```

关键标识符：
- `_00_` = 前置镜头
- `_10_` = 后置镜头

### .insv 文件本质
.insv 实际上是特殊的 MP4 容器，包含：
- 双鱼眼视频流
- 陀螺仪元数据（用于后期防抖）
- 音频流
- 相机配置信息

---

## FFmpeg v360滤镜详解

### 滤镜语法
```
v360=input=格式:output=格式:参数1=值:参数2=值
```

### 输入格式 (input)
| 值 | 说明 |
|----|------|
| `dfisheye` | 双鱼眼（Insta360常用） |
| `fisheye` | 单鱼眼 |
| `equirect` | 等距柱状 |
| `cubemap` | 立方体贴图 |

### 输出格式 (output)
| 值 | 说明 |
|----|------|
| `equirect` | 等距柱状（VR标准） |
| `cubemap` | 立方体贴图 |
| `flat` | 平面 |

### 常用参数

#### FOV 参数
- `ih_fov`：输入水平视场角（Input Horizontal FOV）
- `iv_fov`：输入垂直视场角（Input Vertical FOV）
- `h_fov`：输出水平视场角
- `v_fov`：输出垂直视场角

#### 鱼眼参数
- `pitch`：俯仰角调整
- `yaw`：偏航角调整
- `roll`：翻滚角调整

#### 双鱼眼特定参数
- `d_fov`：双鱼眼总视场角
- `in_forder`：输入顺序（前/后）
- `in_pad`：输入填充

### Insta360 推荐配置

#### X3 配置
```bash
v360=input=dfisheye:output=equirect:ih_fov=180:iv_fov=180:pitch=0:yaw=0:roll=0
```

#### X4 配置
```bash
v360=input=dfisheye:output=equirect:ih_fov=190:iv_fov=190
```

---

## 转换脚本使用

### 方法1：使用主程序（推荐）
```bash
python main.py
```
选择选项 1 进行转换。

### 方法2：直接运行转换脚本
```bash
python convert_360.py
```

### 方法3：命令行参数
```bash
# 转换并同步
python main.py all
```

### 工作流程
1. 将 `.insv` 文件放入 `raw/` 目录
2. 运行转换脚本
3. 转换后的文件在 `exports/` 目录
4.（可选）运行同步脚本推送到PICO

---

## 高级配置

### 自定义 FFmpeg 参数

编辑 `config/config.yaml`：
```yaml
ffmpeg:
  path: "ffmpeg"
  video_codec: "libx265"
  preset: "slow"       # 可选: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
  crf: 22              # 质量: 0-51, 越小越好
  audio_codec: "aac"
  audio_bitrate: "192k"
```

### CRF 值参考
| CRF | 质量 | 文件大小 |
|-----|------|----------|
| 18 | 近乎无损 | 很大 |
| 23 | 默认 | 中等 |
| 28 | 可接受 | 较小 |

### 预设 (Preset) 参考
| Preset | 速度 | 压缩率 |
|--------|------|--------|
| ultrafast | 最快 | 最差 |
| fast | 快 | 一般 |
| medium | 中 | 好 |
| slow | 慢 | 很好 |

### 完整的 FFmpeg 命令示例

#### 基础转换
```bash
ffmpeg -i input_00.insv -i input_10.insv \
  -filter_complex "[0:v][1:v]hstack,v360=input=dfisheye:output=equirect:ih_fov=180:iv_fov=180" \
  -c:v libx265 -crf 23 -preset fast \
  -c:a copy output.mp4
```

#### 带音频重新编码
```bash
ffmpeg -i input_00.insv -i input_10.insv \
  -filter_complex "[0:v][1:v]hstack,v360=input=dfisheye:output=equirect" \
  -c:v libx265 -crf 22 -preset medium \
  -c:a aac -b:a 192k output.mp4
```

#### 指定分辨率
```bash
ffmpeg -i input_00.insv -i input_10.insv \
  -filter_complex "[0:v][1:v]hstack,v360=input=dfisheye:output=equirect,scale=5760:2880" \
  -c:v libx265 -crf 23 output.mp4
```

---

## 常见问题

### Q1: 转换后的视频有拼接缝？
**A**: 调整 v360 参数的 FOV 值：
```bash
# 尝试微调 FOV
v360=input=dfisheye:output=equirect:ih_fov=175:iv_fov=175
```

### Q2: 视频上下颠倒？
**A**: 添加旋转参数：
```bash
# 旋转 180 度
v360=...:pitch=180
```

### Q3: 转换速度太慢？
**A**: 
- 使用更快的 preset: `-preset ultrafast`
- 降低分辨率
- 使用 GPU 加速（如果支持）

### Q4: PICO 无法播放？
**A**: 检查：
1. 确认是等距柱状投影
2. 视频编码是 H.264/H.265
3. 容器格式是 MP4
4. 尝试降低码率

### Q5: 只有单文件怎么办？
**A**: 脚本会自动处理单文件，但效果可能不如双鱼眼拼接。

---

## 使用 Insta360 Studio (备选方案)

如果 FFmpeg 效果不理想，可以使用官方软件：

1. 下载 [Insta360 Studio](https://www.insta360.com/download/studio)
2. 导入 .insv 文件
3. 调整拼接参数
4. 导出为 Equirectangular MP4
5. 使用本项目的同步脚本推送到 PICO

---

## 下一步

- 阅读 [快速入门](01_quick_start.md)
- 查看 [VR开发基础](../learning/02_vr_development_basics.md)
- 尝试生成AI内容：`python main.py ai`
