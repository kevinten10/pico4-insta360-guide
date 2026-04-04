#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def print_banner():
    banner = r"""
╔══════════════════════════════════════════════════════════╗
║                PICO 4 VR 项目工具箱                        ║
║            VR Development & Metaverse Toolkit             ║
╚══════════════════════════════════════════════════════════╝
    """
    print(banner)


def convert_videos():
    print("\n🎬 启动视频转换...")
    from convert_360 import main as convert_main
    convert_main()


def sync_to_pico():
    print("\n📡 启动PICO同步服务...")
    from sync_to_pico import main as sync_main
    sync_main()


def generate_ai_content():
    print("\n🤖 生成AI内容...")
    from ai_content.vr_scene_generator import VRSceneGenerator
    from ai_content.avatar_generator import AvatarGenerator
    from ai_content.story_generator import VRStoryGenerator

    scene_gen = VRSceneGenerator()
    avatar_gen = AvatarGenerator()
    story_gen = VRStoryGenerator()

    themes = ["forest", "space", "beach"]
    for theme in themes:
        scene = scene_gen.generate_scene_description(theme)
        scene_gen.save_scene(scene)
        scene_gen.save_unity_script(scene)

    avatar_gen.batch_generate(3)

    genres = ["adventure", "mystery", "fantasy", "sci-fi"]
    for genre in genres:
        story = story_gen.generate_vr_story(genre)
        story_gen.save_story(story)
        story_gen.save_unity_script(story)


def show_learning_menu():
    print("\n📚 学习资源:")
    print("  1. 元宇宙入门 (learning/01_metaverse_introduction.md)")
    print("  2. VR开发基础 (learning/02_vr_development_basics.md)")
    print("  3. VR高级主题 (learning/03_advanced_topics.md)")


def main():
    print_banner()

    parser = argparse.ArgumentParser(description='PICO 4 VR 项目工具箱')
    parser.add_argument('command', nargs='?', choices=['convert', 'sync', 'ai', 'learn', 'all'],
                        help='执行命令: convert(转换), sync(同步), ai(AI内容), learn(学习), all(全部)')

    args = parser.parse_args()

    if args.command is None:
        print("\n请选择一个操作:")
        print("  1. 转换Insta360视频")
        print("  2. 同步到PICO设备")
        print("  3. 生成AI内容")
        print("  4. 查看学习资源")
        print("  5. 执行全部")

        choice = input("\n请输入选项 (1-5): ").strip()

        if choice == "1":
            convert_videos()
        elif choice == "2":
            sync_to_pico()
        elif choice == "3":
            generate_ai_content()
        elif choice == "4":
            show_learning_menu()
        elif choice == "5":
            convert_videos()
            generate_ai_content()
            sync_to_pico()
        else:
            print("❌ 无效选项")
    else:
        if args.command == "convert":
            convert_videos()
        elif args.command == "sync":
            sync_to_pico()
        elif args.command == "ai":
            generate_ai_content()
        elif args.command == "learn":
            show_learning_menu()
        elif args.command == "all":
            convert_videos()
            generate_ai_content()
            sync_to_pico()


if __name__ == "__main__":
    main()
