import os
import json
from datetime import datetime
import random


class VRStoryGenerator:
    def __init__(self, output_dir="./ai_content/stories"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_vr_story(self, genre="adventure"):
        settings = {
            "adventure": {
                "setting": "神秘的古代遗迹",
                "goal": "寻找失落的宝藏",
                "obstacles": ["陷阱", "谜题", "守护者"],
                "tone": "惊险刺激"
            },
            "mystery": {
                "setting": "维多利亚时代的豪宅",
                "goal": "解开谋杀之谜",
                "obstacles": ["线索", "嫌疑人", "秘密房间"],
                "tone": "悬疑紧张"
            },
            "fantasy": {
                "setting": "魔法森林",
                "goal": "拯救被施咒的王国",
                "obstacles": ["恶龙", "黑魔法", "试炼"],
                "tone": "奇幻壮丽"
            },
            "sci-fi": {
                "setting": "未来太空站",
                "goal": "阻止外星入侵",
                "obstacles": ["机器人", "时间悖论", "太空"],
                "tone": "科幻未来"
            }
        }

        story_data = settings.get(genre, settings["adventure"])

        story = {
            "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "genre": genre,
            "title": f"{story_data['setting']}之旅",
            "setting": story_data["setting"],
            "goal": story_data["goal"],
            "tone": story_data["tone"],
            "characters": [
                {
                    "role": "主角",
                    "name": "探险家",
                    "description": "勇敢的冒险者"
                },
                {
                    "role": "向导",
                    "name": "神秘人",
                    "description": "提供线索的NPC"
                }
            ],
            "plot_points": [
                {
                    "act": 1,
                    "event": "到达目的地",
                    "location": story_data["setting"],
                    "interaction": "与向导对话"
                },
                {
                    "act": 2,
                    "event": "面对第一个挑战",
                    "obstacle": random.choice(story_data["obstacles"]),
                    "puzzle": "解开机关"
                },
                {
                    "act": 3,
                    "event": "最终决战",
                    "climax": "达成目标",
                    "reward": "宝藏/真相"
                }
            ],
            "vr_interactions": [
                "物品拾取",
                "谜题解密",
                "NPC对话",
                "环境探索",
                "传送移动"
            ]
        }
        return story

    def save_story(self, story, filename=None):
        if filename is None:
            filename = f"vr_story_{story['id']}.json"

        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(story, f, ensure_ascii=False, indent=2)

        print(f"✅ VR故事已保存: {filepath}")
        return filepath

    def generate_unity_story_script(self, story):
        script = f"""
using UnityEngine;

public class VRStoryController : MonoBehaviour
{{
    public string storyTitle = "{story['title']}";
    private int currentAct = 0;

    void Start()
    {{
        Debug.Log($"开始故事: {story['title']}");
        StartAct(0);
    }}

    void StartAct(int actIndex)
    {{
        currentAct = actIndex;
        Debug.Log($"第 {{actIndex + 1}} 幕: {story['plot_points'][actIndex]['event']}");
    }}

    public void CompleteCurrentAct()
    {{
        if (currentAct < {len(story['plot_points']) - 1})
        {{
            StartAct(currentAct + 1);
        }}
        else
        {{
            Debug.Log("故事完成！");
        }}
    }}
}}
"""
        return script

    def save_unity_script(self, story, filename=None):
        if filename is None:
            filename = f"VRStory_{story['id']}.cs"

        filepath = os.path.join(self.output_dir, filename)
        script_content = self.generate_unity_story_script(story)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(script_content)

        print(f"✅ Unity故事脚本已保存: {filepath}")
        return filepath


if __name__ == "__main__":
    generator = VRStoryGenerator()

    genres = ["adventure", "mystery", "fantasy", "sci-fi"]
    for genre in genres:
        print(f"\n📖 生成 {genre} 故事...")
        story = generator.generate_vr_story(genre)
        generator.save_story(story)
        generator.save_unity_script(story)
