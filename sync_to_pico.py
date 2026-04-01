import os
import time
import shutil
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- 配置区 (Configuration) ---
SOURCE_DIR = "./exports"       # 监控 Insta360 Studio 的导出目录
PICO_DEST_DIR = "/sdcard/Movies/" # PICO 4 目标目录
EXTENSIONS = {".mp4", ".m4v"}    # 关注的文件后缀

class SyncHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and os.path.splitext(event.src_path)[1].lower() in EXTENSIONS:
            self.sync_file(event.src_path)

    def sync_file(self, file_path):
        file_name = os.path.basename(file_path)
        print(f"馃敶 检测到新视频: {file_name}")
        
        # 尝试通过 ADB 传输 (Android Debug Bridge)
        print(f"鈺 正在尝试通过 ADB 传输到 PICO 4...")
        try:
            # 检查 ADB 设备
            result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
            if "device" in result.stdout.split('\n')[1]:
                cmd = ["adb", "push", file_path, PICO_DEST_DIR]
                subprocess.run(cmd, check=True)
                print(f"鉁 同步成功: {file_name}")
            else:
                print("鈿 未检测到 PICO 4 设备。请检查 USB 连接并开启 USB 调试。")
                print(f"馃搳 请手动拷贝至: {PICO_DEST_DIR}")
        except FileNotFoundError:
            print("鈿 未安装 ADB 环境。建议安装 Android Platform Tools 以实现自动同步。")
            print(f"馃搳 请手动拷贝至: {PICO_DEST_DIR}")
        except Exception as e:
            print(f"鉁 传输失败: {e}")

if __name__ == "__main__":
    if not os.path.exists(SOURCE_DIR):
        os.makedirs(SOURCE_DIR)
        print(f"馃摕 已创建监控目录: {SOURCE_DIR}")

    event_handler = SyncHandler()
    observer = Observer()
    observer.schedule(event_handler, SOURCE_DIR, recursive=False)
    
    print(f"馃殗 自动化同步服务已启动...")
    print(f"馃搳 监控目录: {os.path.abspath(SOURCE_DIR)}")
    print(f"馃搳 目标设备: PICO 4 ({PICO_DEST_DIR})")
    print("鎸 Ctrl+C 停止服务")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
