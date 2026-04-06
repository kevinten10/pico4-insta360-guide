# 🤖 持续研究系统使用指南

## 系统概述

本项目配备了自动化持续研究系统，能够：
- 🔬 自动分析README内容
- ✅ 验证技术规格准确性
- 🎨 生成可视化图表
- 🔄 持续优化和更新文档
- 📤 自动提交到GitHub

---

## 📁 研究系统文件

| 文件 | 说明 |
|------|------|
| `continuous_research.py` | 主研究系统（推荐） |
| `research_bot.py` | 基础研究机器人 |
| `start_continuous_research.bat` | Windows批处理启动脚本 |
| `.research_state.json` | 研究状态保存 |
| `research.log` | 研究日志 |
| `assets/diagrams/` | 生成的图表目录 |

---

## 🚀 使用方法

### 方法1: 单次运行（推荐初次使用）

```bash
python continuous_research.py
# 选择选项 1: 单次运行研究
```

### 方法2: 持续运行模式

```bash
python continuous_research.py
# 选择选项 2: 持续运行模式
# 设置研究间隔（默认3600秒=1小时）
```

### 方法3: Windows批处理（后台持续运行）

```bash
start_continuous_research.bat
```

双击运行，窗口将保持打开并每小时执行一次研究。

### 方法4: 仅生成图表

```bash
python continuous_research.py
# 选择选项 3: 仅生成可视化图表
```

---

## 📊 生成的可视化图表

系统会自动生成以下Mermaid图表：

### 1. 工作流程图 (workflow.mmd)
展示从Insta360拍摄到PICO观看的完整流程

### 2. 学习路径图 (learning_path.mmd)
展示从入门到专家的5阶段学习路线

### 3. AI生态系统图 (ai_ecosystem.mmd)
展示PICO AI应用的层次结构

### 4. 技术栈架构图 (tech_stack.mmd)
展示项目的完整技术栈

---

## ⚙️ 系统配置

在 `continuous_research.py` 中可以修改配置：

```python
self.config = {
    'research_interval': 3600,  # 研究间隔（秒）
    'auto_commit': True,         # 是否自动提交到GitHub
    'generate_diagrams': True,   # 是否生成图表
    'verify_facts': True         # 是否验证技术事实
}
```

---

## 🔍 研究内容

系统会自动研究和验证：

### 技术规格验证
- ✅ PICO 4 硬件参数
- ✅ Insta360 X3/X4 规格
- ✅ FFmpeg v360 滤镜支持
- ✅ Unity XR 开发要求

### README分析
- 📏 文档长度和结构
- 📊 表格和代码块统计
- 🔗 链接和图片数量
- ⚠️ 需要更新的内容

### 改进建议生成
- 💡 缺失的章节建议
- 🎨 可视化改进
- 📚 内容补充建议

---

## 📈 研究日志

所有研究活动都会记录在 `research.log` 中：

```
[2026-04-06 09:13:38] [INFO] 🔬 开始第 1 轮研究...
[2026-04-06 09:13:38] [INFO] 📊 README分析: 415 行, 8635 字符
[2026-04-06 09:13:38] [INFO] ✅ 已验证 3 项技术规格
[2026-04-06 09:13:38] [INFO] 🎨 已生成并添加架构图
```

---

## 🔄 自动提交

当 `auto_commit` 为 `True` 时：
1. 系统完成研究后自动检查更改
2. 如有更改，自动提交到GitHub
3. 提交信息包含研究周期编号

---

## 🛑 停止系统

- **单次运行**: 自动完成后退出
- **持续运行**: 按 `Ctrl+C` 停止
- **批处理窗口**: 关闭窗口或按 `Ctrl+C`

---

## 💡 使用建议

1. **初次使用**: 先运行单次模式，检查效果
2. **日常使用**: 使用批处理脚本后台运行
3. **重要更新前**: 暂停自动提交，手动审核
4. **定期检查**: 查看 `research.log` 了解研究进展

---

## 🔮 未来扩展

计划添加的功能：
- [ ] 网络搜索验证最新信息
- [ ] AI驱动的内容生成
- [ ] 多语言自动翻译
- [ ] 性能基准测试
- [ ] 用户反馈集成

---

*最后更新: 2026年4月6日*
