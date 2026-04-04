import os
import yaml
from typing import Dict, Any


class ConfigLoader:
    def __init__(self, config_path: str = "./config/config.yaml"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"配置文件不存在: {self.config_path}")

        with open(self.config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        return config

    def get(self, key_path: str, default: Any = None) -> Any:
        keys = key_path.split('.')
        value = self.config

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default

        return value

    def get_paths(self) -> Dict[str, str]:
        return self.get('paths', {})

    def get_ffmpeg_config(self) -> Dict[str, Any]:
        return self.get('ffmpeg', {})

    def get_pico_config(self) -> Dict[str, Any]:
        return self.get('pico', {})

    def get_ai_content_config(self) -> Dict[str, Any]:
        return self.get('ai_content', {})
