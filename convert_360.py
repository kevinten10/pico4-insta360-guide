import os
import subprocess
import glob

# --- 配置 (Configuration) ---
RAW_DIR = "./raw"
EXPORT_DIR = "./exports"
FFMPEG_PATH = "ffmpeg"  # 确保 ffmpeg 已安装在系统路径中

def convert_to_360_equirectangular(input_files, output_file):
    """
    使用 ffmpeg v360 滤镜将双鱼眼拼接为等距柱状投影 (Equirectangular)
    针对 Insta360 X3/X4 的基本拼接模版
    """
    print(f"🚀 正在启动自动化转换: {output_file}")
    
    # 获取两个镜头的输入文件
    # Insta360 通常将 00 和 10 作为左右镜头的标识
    if len(input_files) < 2:
        print("⚠️ 警告: 未找到成对的镜头文件，尝试单文件转换...")
        inputs = f"-i {input_files[0]}"
    else:
        inputs = f"-i {input_files[0]} -i {input_files[1]}"

    # 核心拼接滤镜 (基本的双鱼眼横向拼接并映射为全景)
    # 这里的参数需要根据特定相机型号的 FOV (Field of View) 进行微调
    filter_complex = (
        "[0:v][1:v]hstack,v360=input=dfisheye:output=equirect:ih_fov=180:iv_fov=180"
    )

    cmd = [
        FFMPEG_PATH,
        "-y",
        *input_files_args(input_files),
        "-filter_complex", filter_complex,
        "-c:v", "libx265",  # 使用 H.265 编码以节省空间并保持画质
        "-preset", "fast",
        "-crf", "23",
        "-c:a", "copy",     # 保留原始音频
        output_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ 转换成功: {output_file}")
    except Exception as e:
        print(f"❌ 转换过程中出错: {e}")

def input_files_args(input_files):
    args = []
    for f in input_files:
        args.extend(["-i", f])
    return args

def find_insv_pairs():
    """ 寻找成对的 .insv 文件 """
    files = glob.glob(os.path.join(RAW_DIR, "*.insv"))
    pairs = {}
    for f in files:
        # 获取文件名核心部分，忽略 _00_ 和 _10_ 的区别
        base = os.path.basename(f).replace("_00_", "_XX_").replace("_10_", "_XX_")
        if base not in pairs:
            pairs[base] = []
        pairs[base].append(f)
    return pairs

if __name__ == "__main__":
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)

    insv_pairs = find_insv_pairs()
    for base_name, files in insv_pairs.items():
        output_name = base_name.replace("_XX_", "_FULL_").replace(".insv", ".mp4")
        output_path = os.path.join(EXPORT_DIR, output_name)
        
        if not os.path.exists(output_path):
            convert_to_360_equirectangular(files, output_path)
        else:
            print(f"⏩ 跳过已存在文件: {output_name}")
