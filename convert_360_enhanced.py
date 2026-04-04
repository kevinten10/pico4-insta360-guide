import os
import subprocess
import glob
import argparse
import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple


class VRVideoConverter:
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or self._get_default_config()
        self._ensure_directories()

    @staticmethod
    def _get_default_config() -> Dict:
        return {
            "raw_dir": "./raw",
            "export_dir": "./exports",
            "ffmpeg_path": "ffmpeg",
            "video_codec": "libx265",
            "preset": "fast",
            "crf": 23,
            "audio_codec": "copy",
            "audio_bitrate": None,
            "camera_model": "X3",
            "ih_fov": 180,
            "iv_fov": 180,
            "pitch": 0,
            "yaw": 0,
            "roll": 0,
            "output_resolution": None
        }

    def _ensure_directories(self):
        os.makedirs(self.config["raw_dir"], exist_ok=True)
        os.makedirs(self.config["export_dir"], exist_ok=True)

    def check_ffmpeg(self) -> bool:
        try:
            result = subprocess.run(
                [self.config["ffmpeg_path"], "-version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def check_v360_filter(self) -> bool:
        try:
            result = subprocess.run(
                [self.config["ffmpeg_path"], "-filters"],
                capture_output=True,
                text=True
            )
            return "v360" in result.stdout
        except FileNotFoundError:
            return False

    def find_insv_pairs(self) -> Dict[str, List[str]]:
        raw_dir = self.config["raw_dir"]
        files = glob.glob(os.path.join(raw_dir, "*.insv"))
        pairs = {}

        for f in files:
            base = os.path.basename(f)
            base = base.replace("_00_", "_XX_").replace("_10_", "_XX_")
            if base not in pairs:
                pairs[base] = []
            pairs[base].append(f)

        return pairs

    def build_filter_complex(self, num_inputs: int) -> str:
        if num_inputs >= 2:
            filter_parts = [
                "[0:v][1:v]hstack",
                f"v360=input=dfisheye:output=equirect",
                f"ih_fov={self.config['ih_fov']}",
                f"iv_fov={self.config['iv_fov']}"
            ]

            if self.config["pitch"] != 0:
                filter_parts.append(f"pitch={self.config['pitch']}")
            if self.config["yaw"] != 0:
                filter_parts.append(f"yaw={self.config['yaw']}")
            if self.config["roll"] != 0:
                filter_parts.append(f"roll={self.config['roll']}")

            filter_str = ",".join(filter_parts[:1]) + "," + ":".join(filter_parts[1:])

            if self.config["output_resolution"]:
                w, h = self.config["output_resolution"]
                filter_str += f",scale={w}:{h}"

            return filter_str
        else:
            filter_str = (
                f"v360=input=fisheye:output=equirect:"
                f"ih_fov={self.config['ih_fov']}:iv_fov={self.config['iv_fov']}"
            )
            if self.config["output_resolution"]:
                w, h = self.config["output_resolution"]
                filter_str += f",scale={w}:{h}"
            return filter_str

    def convert_file(self, input_files: List[str], output_file: str) -> bool:
        print(f"\n🎬 开始转换: {os.path.basename(output_file)}")
        print(f"   输入文件: {[os.path.basename(f) for f in input_files]}")

        cmd = [
            self.config["ffmpeg_path"],
            "-y",
            "-hide_banner",
            "-loglevel", "info"
        ]

        for f in input_files:
            cmd.extend(["-i", f])

        cmd.extend([
            "-filter_complex", self.build_filter_complex(len(input_files)),
            "-c:v", self.config["video_codec"],
            "-preset", self.config["preset"],
            "-crf", str(self.config["crf"])
        ])

        if self.config["audio_codec"] == "copy":
            cmd.extend(["-c:a", "copy"])
        else:
            cmd.extend(["-c:a", self.config["audio_codec"]])
            if self.config["audio_bitrate"]:
                cmd.extend(["-b:a", self.config["audio_bitrate"]])

        cmd.append(output_file)

        try:
            print(f"   正在处理...")
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                file_size = os.path.getsize(output_file) / (1024 * 1024)
                print(f"✅ 转换成功! ({file_size:.2f} MB)")
                return True
            else:
                print(f"❌ 转换失败")
                print(f"   错误信息: {result.stderr[-500:]}")
                return False

        except Exception as e:
            print(f"❌ 转换出错: {str(e)}")
            return False

    def convert_all(self, overwrite: bool = False) -> Tuple[int, int]:
        pairs = self.find_insv_pairs()

        if not pairs:
            print("⚠️ 未找到待转换的 .insv 文件")
            return 0, 0

        success_count = 0
        skip_count = 0

        for base_name, files in sorted(pairs.items()):
            output_name = base_name.replace("_XX_", "_FULL_").replace(".insv", ".mp4")
            output_path = os.path.join(self.config["export_dir"], output_name)

            if os.path.exists(output_path) and not overwrite:
                print(f"⏩ 跳过已存在: {output_name}")
                skip_count += 1
                continue

            if self.convert_file(files, output_path):
                success_count += 1
            else:
                if os.path.exists(output_path):
                    os.remove(output_path)

        return success_count, skip_count

    def print_status(self):
        print("\n" + "=" * 60)
        print("📊 VR 视频转换器状态")
        print("=" * 60)
        print(f"FFmpeg 可用: {'✅' if self.check_ffmpeg() else '❌'}")
        print(f"v360 滤镜: {'✅' if self.check_v360_filter() else '❌'}")
        print(f"输入目录: {os.path.abspath(self.config['raw_dir'])}")
        print(f"输出目录: {os.path.abspath(self.config['export_dir'])}")

        pairs = self.find_insv_pairs()
        print(f"待转换文件对: {len(pairs)}")
        for base, files in pairs.items():
            print(f"  - {base}: {len(files)} 个文件")
        print("=" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(description="增强版 Insta360 到 PICO VR 视频转换器")
    parser.add_argument("--config", type=str, help="配置文件路径 (JSON)")
    parser.add_argument("--raw-dir", type=str, help="原始文件目录")
    parser.add_argument("--export-dir", type=str, help="输出目录")
    parser.add_argument("--preset", type=str, choices=["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"], help="编码预设")
    parser.add_argument("--crf", type=int, help="CRF 质量值 (0-51)")
    parser.add_argument("--camera", type=str, choices=["X3", "X4", "ONE_X2"], help="相机型号")
    parser.add_argument("--ih-fov", type=int, help="输入水平视场角")
    parser.add_argument("--iv-fov", type=int, help="输入垂直视场角")
    parser.add_argument("--resolution", type=str, help="输出分辨率 (例如: 5760:2880)")
    parser.add_argument("--overwrite", action="store_true", help="覆盖已存在的文件")
    parser.add_argument("--status", action="store_true", help="仅显示状态")
    parser.add_argument("--verbose", action="store_true", help="详细输出")

    args = parser.parse_args()

    config = VRVideoConverter._get_default_config()

    if args.config and os.path.exists(args.config):
        with open(args.config, 'r', encoding='utf-8') as f:
            config.update(json.load(f))

    if args.raw_dir:
        config["raw_dir"] = args.raw_dir
    if args.export_dir:
        config["export_dir"] = args.export_dir
    if args.preset:
        config["preset"] = args.preset
    if args.crf is not None:
        config["crf"] = args.crf
    if args.camera:
        config["camera_model"] = args.camera
        if args.camera == "X3":
            config["ih_fov"] = 180
            config["iv_fov"] = 180
        elif args.camera == "X4":
            config["ih_fov"] = 190
            config["iv_fov"] = 190
    if args.ih_fov:
        config["ih_fov"] = args.ih_fov
    if args.iv_fov:
        config["iv_fov"] = args.iv_fov
    if args.resolution:
        w, h = map(int, args.resolution.split(":"))
        config["output_resolution"] = (w, h)

    converter = VRVideoConverter(config)

    if args.status:
        converter.print_status()
        return

    converter.print_status()

    if not converter.check_ffmpeg():
        print("❌ 错误: 未找到 FFmpeg，请先安装 FFmpeg 并添加到系统 PATH")
        return

    if not converter.check_v360_filter():
        print("❌ 错误: FFmpeg 不支持 v360 滤镜，请使用较新版本的 FFmpeg")
        return

    success, skipped = converter.convert_all(overwrite=args.overwrite)

    print("\n" + "=" * 60)
    print(f"📈 转换完成: 成功 {success} 个, 跳过 {skipped} 个")
    print("=" * 60)


if __name__ == "__main__":
    main()
