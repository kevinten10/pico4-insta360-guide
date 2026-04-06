# 📦 Unity VR项目打包并部署到PICO 4 完整指南

## 目录
1. [环境准备](#环境准备)
2. [Unity构建设置](#unity构建设置)
3. [打包APK](#打包apk)
4. [部署到PICO](#部署到pico)
5. [发布到PICO商店](#发布到pico商店)
6. [常见问题](#常见问题)

---

## 环境准备

### 1. 确认开发环境

| 组件 | 版本要求 | 检查方法 |
|------|---------|---------|
| Unity | 2021.3 LTS+ | Help → About Unity |
| Android Build Support | 已安装 | Build Settings → Android |
| PICO SDK | 最新版 | Package Manager |
| JDK | 11+ | Edit → Preferences → External Tools |
| Android SDK | API 29+ | 同上 |

### 2. PICO设备准备

#### 开启开发者模式
```
1. 打开PICO 4设置
2. 进入 "关于本机"
3. 连续点击 "版本号" 7次
4. 返回设置，进入 "开发者选项"
5. 开启 "USB调试"
```

#### 连接电脑
```
1. 使用USB-C数据线连接PICO到电脑
2. PICO弹出"允许USB调试"，勾选"始终允许"
3. 点击"确定"
4. 电脑端确认连接成功
```

#### 验证连接
```bash
# 打开命令行，输入
adb devices

# 应该显示：
List of devices attached
XXXXXXXX    device
```

---

## Unity构建设置

### 1. 切换平台

```
File → Build Settings (Ctrl+Shift+B)
├─ Platform: Android
├─ Texture Compression: ASTC
└─ 点击 [Switch Platform]
```

### 2. Player设置

```
Edit → Project Settings → Player
```

#### Resolution and Presentation
```
✓ Run in background
✓ Render outside safe area
Orientation: Landscape Left
```

#### Other Settings
```
Identification:
  - Package Name: com.yourcompany.yourapp
  - Version: 1.0.0
  - Bundle Version Code: 1
  - Minimum API Level: Android 10.0 (API 29)
  - Target API Level: Android 12.0 (API 31)

Configuration:
  - Scripting Backend: IL2CPP
  - API Compatibility Level: .NET Standard 2.1
  - Target Architectures: ARM64 ✓
```

#### XR Plug-in Management
```
Edit → Project Settings → XR Plug-in Management
├─ Android标签
├─ ✓ PICO XR
└─ 点击 [Install XR Plug-in Management] 如未安装
```

#### PICO XR设置
```
Edit → Project Settings → PICO XR
├─ Target Devices: PICO 4, PICO Neo3
├─ Stereo Rendering Mode: Multi Pass
└─ 其他保持默认
```

### 3. 场景设置

```
File → Build Settings → Scenes In Build
├─ 点击 [Add Open Scenes]
├─ 确保场景已勾选
└─ 调整场景顺序（如有多个）
```

### 4. 质量设置

```
Edit → Project Settings → Quality
├─ 选择 "Very Low" 或 "Low"
├─ 确保选中Android平台图标
└─ 关闭不必要的特效以保证90FPS
```

---

## 打包APK

### 方法一：Unity直接构建（推荐开发测试）

#### 步骤1：连接设备
```
1. PICO通过USB连接电脑
2. 确认adb devices显示设备
```

#### 步骤2：构建并运行
```
File → Build And Run (Ctrl+B)
├─ 选择保存位置（如 Builds/VRDemo.apk）
├─ 等待构建完成（首次较慢，约5-10分钟）
└─ 自动安装并启动应用
```

#### 构建输出
```
构建成功后会显示：
✓ Build completed successfully
✓ APK大小: XX MB
✓ 已安装到设备
```

### 方法二：仅构建APK（用于分发）

```
File → Build Settings
├─ 点击 [Build]
├─ 选择保存路径
└─ 生成APK文件
```

### 方法三：命令行构建（CI/CD使用）

```bash
# Windows PowerShell
& "C:\Program Files\Unity\Hub\Editor\2021.3.x\Editor\Unity.exe" `
  -quit `
  -batchmode `
  -projectPath "D:\YourProject" `
  -executeMethod BuildScript.BuildAndroid `
  -logFile "build.log"
```

#### 构建脚本 (BuildScript.cs)
```csharp
using UnityEditor;
using UnityEngine;

public class BuildScript
{
    [MenuItem("Build/Build Android")]
    public static void BuildAndroid()
    {
        string[] scenes = { "Assets/Scenes/SampleScene.unity" };
        string outputPath = "Builds/VRDemo.apk";
        
        BuildPipeline.BuildPlayer(
            scenes,
            outputPath,
            BuildTarget.Android,
            BuildOptions.None
        );
        
        Debug.Log($"✅ 构建完成: {outputPath}");
    }
}
```

---

## 部署到PICO

### 方法一：Unity直接部署（已在上文介绍）

### 方法二：ADB命令行部署

#### 安装APK
```bash
# 安装应用到PICO
adb install -r Builds/VRDemo.apk

# -r 表示覆盖安装（如果已存在）
# 成功显示：Success
```

#### 启动应用
```bash
# 启动应用
adb shell am start -n com.yourcompany.yourapp/com.unity3d.player.UnityPlayerActivity

# 查看日志
adb logcat -s Unity:D
```

#### 卸载应用
```bash
adb uninstall com.yourcompany.yourapp
```

### 方法三：使用本项目的同步脚本

```bash
# 在项目根目录运行
python sync_to_pico.py

# 或将APK放入 exports/ 目录
# 自动同步到PICO
```

### 方法四：PICO开发者平台上传

#### 1. 注册开发者账号
```
1. 访问 https://developer.pico-interactive.com/
2. 注册/登录账号
3. 完成开发者认证
```

#### 2. 创建应用
```
1. 进入开发者控制台
2. 点击 "创建应用"
3. 填写应用信息：
   - 应用名称
   - 包名 (com.yourcompany.yourapp)
   - 应用类型
   - 应用描述
```

#### 3. 上传APK
```
1. 选择应用 → 版本管理
2. 点击 "上传新版本"
3. 上传APK文件
4. 填写版本信息
5. 上传截图和图标
6. 提交审核
```

---

## 发布到PICO商店

### 准备材料

| 材料 | 要求 | 说明 |
|------|------|------|
| APK文件 | 已签名 | Release模式构建 |
| 应用图标 | 512x512 PNG | 应用商店显示 |
| 封面图 | 1920x1080 | 商店详情页 |
| 截图 | 5-10张 | 应用内画面 |
| 应用描述 | 中文+英文 | 功能介绍 |
| 隐私政策 | 网页链接 | 用户数据说明 |

### 构建Release版本

#### 1. 创建密钥库
```
Edit → Project Settings → Player → Publishing Settings
├─ Keystore: Create New
├─ 填写信息：
│   - Keystore password
│   - Key alias
│   - Key password
└─ 保存.keystore文件
```

#### 2. 构建Release APK
```
File → Build Settings
├─ 确保是Release模式
├─ 点击 [Build]
└─ 生成签名APK
```

### 提交审核

```
1. 登录PICO开发者平台
2. 选择应用 → 提交审核
3. 填写审核信息：
   - 应用分类
   - 适用年龄
   - 内容分级
   - 测试账号（如需要）
4. 提交等待审核（通常3-7个工作日）
```

---

## 常见问题

### Q1: 构建失败，显示"Gradle build failed"

**解决方案：**
```
1. 检查网络连接（需要下载Gradle）
2. 更新Gradle版本：
   Edit → Preferences → External Tools → Android → Gradle
3. 清除缓存：
   File → Invalidate Caches / Restart
4. 检查Android SDK路径是否正确
```

### Q2: 安装到PICO后闪退

**解决方案：**
```
1. 检查Minimum API Level是否<=PICO系统版本
2. 查看logcat日志定位错误：
   adb logcat -s Unity:D AndroidRuntime:E
3. 确保PICO SDK正确初始化
4. 检查是否有缺失的场景或资源
```

### Q3: 控制器没有响应

**解决方案：**
```
1. 确认PICO SDK已正确导入
2. 检查XR Plug-in Management中PICO XR已启用
3. 确保使用了正确的命名空间：
   using Unity.XR.PXR;
4. 检查手柄是否已配对
```

### Q4: 画面卡顿，帧率低

**解决方案：**
```
1. 降低Quality设置到Low
2. 减少场景中的多边形数量
3. 使用遮挡剔除（Occlusion Culling）
4. 降低渲染分辨率：
   XRSettings.eyeTextureResolutionScale = 0.8f;
5. 使用单通道渲染（Single Pass）
```

### Q5: ADB无法识别设备

**解决方案：**
```
1. 检查USB线是否为数据线（非仅充电）
2. 更换USB端口（推荐USB 3.0）
3. 重新安装ADB驱动
4. PICO端重新授权USB调试
5. 重启PICO设备和电脑
```

### Q6: 应用商店审核被拒

**常见原因：**
```
1. 应用崩溃或无法启动
2. 缺少必要的权限说明
3. 内容不符合平台规范
4. 截图与实际内容不符
5. 缺少隐私政策

**解决方法：**
- 仔细查看审核反馈邮件
- 修复问题后重新提交
- 必要时联系PICO开发者支持
```

---

## 性能优化建议

### 构建前检查清单

- [ ] Quality设置已调整为Low/Very Low
- [ ] 移除了不必要的插件和资源
- [ ] 启用了IL2CPP脚本后端
- [ ] 仅选择ARM64架构
- [ ] 压缩了纹理（ASTC格式）
- [ ] 测试了90FPS帧率
- [ ] 检查了内存使用（<2GB）

### 推荐的构建设置

```
Scripting Backend: IL2CPP
C++ Compiler Configuration: Release
Target Architectures: ARM64
Strip Engine Code: ✓
```

---

## 相关链接

- [PICO开发者平台](https://developer.pico-interactive.com/)
- [PICO SDK文档](https://developer.pico-interactive.com/document/unity)
- [Unity Android构建文档](https://docs.unity3d.com/Manual/android-BuildProcess.html)
- [Android开发者指南](https://developer.android.com/studio/publish)

---

**祝你发布成功！🚀**

*最后更新: 2026年4月6日*
