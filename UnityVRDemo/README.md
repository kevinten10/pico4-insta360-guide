# 🎮 PICO 4 VR Demo 项目

一个完整的Unity VR示例项目，可直接导入并在PICO 4上运行。

## 📋 项目包含

### 核心功能
- ✅ VR移动系统（摇杆移动 + 瞬移）
- ✅ 物体抓取交互
- ✅ 射线选择系统
- ✅ 控制器输入处理
- ✅ 完整的PICO SDK集成

### 脚本文件
| 脚本 | 功能 |
|------|------|
| `VRPlayerController.cs` | 玩家移动、旋转、传送 |
| `VRHandController.cs` | 手柄射线、抓取控制 |
| `VRInteractable.cs` | 可交互物体基类 |

## 🚀 快速开始

### 1. 导入项目
```
1. 打开 Unity Hub
2. 点击 "Open" → 选择 UnityVRDemo 文件夹
3. 等待项目加载完成
```

### 2. 安装PICO SDK
```
1. Window → Package Manager
2. 点击 "+" → Add package from disk
3. 选择 PICO Unity Integration SDK
4. 等待安装完成
```

### 3. 场景设置
```
1. 打开 Scenes/SampleScene
2. 在 Hierarchy 中创建空物体命名为 "Player"
3. 将 VRPlayerController.cs 拖到 Player 上
4. 创建两个 Cube 作为手柄，分别添加 VRHandController.cs
5. 设置 Layer 为 "Interactable" 用于可交互物体
```

### 4. 构建设置
```
File → Build Settings:
- Platform: Android
- Texture Compression: ASTC
- 点击 Switch Platform

Player Settings:
- Company Name: YourCompany
- Product Name: VRDemo
- Minimum API Level: Android 10.0 (API 29)
- Target API Level: Android 12.0 (API 31)

XR Settings:
- Virtual Reality Supported: ✓
- Add: PICO XR
```

### 5. 构建并运行
```
1. 连接 PICO 4（USB调试已开启）
2. File → Build And Run
3. 等待构建完成，自动安装到设备
```

## 🎮 操作说明

### 移动
| 操作 | 按键 | 说明 |
|------|------|------|
| 移动 | 左摇杆 | 前后左右移动 |
| 转向 | 右摇杆 | 快速45度转向 |
| 传送 | 右扳机键按住 | 瞄准地面，松开后传送 |

### 交互
| 操作 | 按键 | 说明 |
|------|------|------|
| 抓取 | 扳机键 | 抓取可交互物体 |
| 释放 | 松开扳机 | 释放物体 |
| A键 | 右手A | 按钮交互 |
| B键 | 右手B | 菜单/返回 |

## 📝 自定义扩展

### 添加新的可交互物体
```csharp
1. 创建 Cube 或其他3D物体
2. 添加 Collider 组件
3. 添加 Rigidbody 组件
4. 添加 VRInteractable.cs 脚本
5. 设置 Layer 为 "Interactable"
```

### 添加自定义交互
```csharp
// 继承 VRInteractable 类
public class CustomButton : VRInteractable
{
    public override void OnGrab(Transform controller)
    {
        base.OnGrab(controller);
        // 你的自定义逻辑
        Debug.Log("按钮被按下!");
    }
}
```

## 🔧 常见问题

### Q: 构建失败？
**A:** 
- 确保安装了 Android Build Support
- 检查 Minimum API Level >= 29
- 确认 PICO SDK 正确安装

### Q: 无法在PICO上运行？
**A:**
- 开启开发者模式（设置→关于→版本号点击7次）
- 开启USB调试（设置→开发者选项）
- 使用USB 3.0数据线连接

### Q: 控制器没反应？
**A:**
- 确保手柄已配对
- 检查 PICO SDK 是否正确初始化
- 查看控制台是否有错误信息

## 📚 学习资源

- [PICO开发者文档](https://developer.pico-interactive.com/)
- [Unity XR文档](https://docs.unity3d.com/Manual/XR.html)
- 项目中的 `learning/` 目录

## 🎯 下一步

1. 添加更多交互物体
2. 创建UI界面
3. 添加音效和特效
4. 实现多人联机
5. 发布到PICO商店

---

**祝你开发愉快! 🚀**
