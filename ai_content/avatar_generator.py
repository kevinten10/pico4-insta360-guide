import os
import json
from datetime import datetime
import random


class AvatarGenerator:
    def __init__(self, output_dir="./ai_content/avatars"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_avatar(self, style="realistic", gender=None):
        if gender is None:
            gender = random.choice(["male", "female", "neutral"])

        hair_colors = ["black", "brown", "blonde", "red", "blue", "pink"]
        eye_colors = ["brown", "blue", "green", "hazel", "gray"]
        skin_tones = ["pale", "fair", "medium", "olive", "brown", "dark"]

        avatar = {
            "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "style": style,
            "gender": gender,
            "appearance": {
                "hair": {
                    "color": random.choice(hair_colors),
                    "style": random.choice(["short", "long", "curly", "ponytail", "spiky", "bald"])
                },
                "eyes": {
                    "color": random.choice(eye_colors)
                },
                "skin": {
                    "tone": random.choice(skin_tones)
                },
                "facial_features": {
                    "glasses": random.choice([True, False]),
                    "beard": gender in ["male", "neutral"] and random.choice([True, False, False]),
                    "makeup": gender in ["female", "neutral"] and random.choice([True, False])
                }
            },
            "clothing": {
                "top": random.choice(["t-shirt", "shirt", "hoodie", "sweater", "jacket"]),
                "bottom": random.choice(["jeans", "shorts", "skirt", "trousers"]),
                "shoes": random.choice(["sneakers", "boots", "sandals", "formal"])
            },
            "accessories": [
                item for item in [
                    "watch", "bracelet", "necklace", "hat", "backpack"
                ] if random.random() > 0.6
            ],
            "personality_traits": random.sample([
                "friendly", "adventurous", "creative", "serious",
                "playful", "intellectual", "athletic", "artistic"
            ], 3)
        }
        return avatar

    def save_avatar(self, avatar, filename=None):
        if filename is None:
            filename = f"avatar_{avatar['id']}.json"

        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(avatar, f, ensure_ascii=False, indent=2)

        print(f"✅ 虚拟形象已保存: {filepath}")
        return filepath

    def generate_vrchat_description(self, avatar):
        description = f"""
# VRChat 虚拟形象描述

## 基本信息
- 风格: {avatar['style']}
- 性别: {avatar['gender']}

## 外观
- 头发: {avatar['appearance']['hair']['color']} - {avatar['appearance']['hair']['style']}
- 眼睛: {avatar['appearance']['eyes']['color']}
- 肤色: {avatar['appearance']['skin']['tone']}

## 服装
- 上衣: {avatar['clothing']['top']}
- 下装: {avatar['clothing']['bottom']}
- 鞋子: {avatar['clothing']['shoes']}

## 配饰
{', '.join(avatar['accessories']) if avatar['accessories'] else '无'}

## 性格特质
{', '.join(avatar['personality_traits'])}
"""
        return description

    def batch_generate(self, count=5):
        avatars = []
        for i in range(count):
            print(f"🎭 生成虚拟形象 {i+1}/{count}...")
            avatar = self.generate_avatar()
            self.save_avatar(avatar)
            avatars.append(avatar)
        return avatars


if __name__ == "__main__":
    generator = AvatarGenerator()
    generator.batch_generate(3)
