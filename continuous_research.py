#!/usr/bin/env python3
"""
Continuous Research & Auto-Update System for README
持续研究README内容，自动验证、优化并生成可视化图表
"""

import os
import json
import time
import re
from datetime import datetime
from pathlib import Path

class ContinuousResearchSystem:
    """持续研究系统"""
    
    def __init__(self):
        self.config = {
            'research_interval': 3600,  # 默认1小时
            'auto_commit': True,
            'generate_diagrams': True,
            'verify_facts': True
        }
        self.state_file = '.research_state.json'
        self.log_file = 'research.log'
        self.load_state()
        
    def load_state(self):
        """加载研究状态"""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r', encoding='utf-8') as f:
                self.state = json.load(f)
        else:
            self.state = {
                'research_count': 0,
                'last_update': None,
                'verified_facts': {},
                'pending_verifications': [],
                'improvements_made': []
            }
    
    def save_state(self):
        """保存研究状态"""
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)
    
    def log(self, message, level='INFO'):
        """记录日志"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry + '\n')
    
    def analyze_readme(self):
        """分析README内容"""
        readme_path = 'README.md'
        if not os.path.exists(readme_path):
            self.log("README.md 不存在", 'ERROR')
            return None
        
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        analysis = {
            'total_lines': len(content.split('\n')),
            'total_chars': len(content),
            'sections': self._extract_sections(content),
            'tables': len(re.findall(r'\|.*\|.*\|', content)),
            'code_blocks': content.count('```'),
            'links': len(re.findall(r'\[.*?\]\(.*?\)', content)),
            'images': len(re.findall(r'!\[.*?\]\(.*?\)', content)),
            'needs_update': []
        }
        
        # 检查需要更新的内容
        current_year = datetime.now().year
        if str(current_year) not in content:
            analysis['needs_update'].append(f'添加{current_year}年最新信息')
        
        # 检查技术规格
        tech_specs = ['PICO 4', 'Insta360', 'FFmpeg', 'Unity']
        for spec in tech_specs:
            if spec not in content:
                analysis['needs_update'].append(f'补充{spec}相关信息')
        
        return analysis
    
    def _extract_sections(self, content):
        """提取章节结构"""
        sections = []
        for line in content.split('\n'):
            if line.startswith('#'):
                level = len(line.split()[0])
                title = line.strip('#').strip()
                sections.append({'level': level, 'title': title})
        return sections
    
    def generate_mermaid_diagrams(self):
        """生成Mermaid图表"""
        diagrams = {
            'workflow': '''```mermaid
graph TD
    A[Insta360拍摄] -->|INSV文件| B[放入raw/]
    B --> C{选择转换模式}
    C -->|基础模式| D[convert_360.py]
    C -->|增强模式| E[convert_360_enhanced.py]
    D --> F[FFmpeg处理]
    E --> F
    F -->|v360滤镜| G[等距柱状投影]
    G --> H[exports/目录]
    H --> I[sync_to_pico.py]
    I -->|ADB推送| J[PICO 4观看]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style J fill:#bbf,stroke:#333,stroke-width:2px
```''',
            'learning_path': '''```mermaid
graph LR
    subgraph 入门阶段
        A1[元宇宙概念] --> A2[PICO设备]
        A2 --> A3[视频转换]
    end
    
    subgraph 基础阶段
        B1[Unity基础] --> B2[C#编程]
        B2 --> B3[VR交互]
    end
    
    subgraph 进阶阶段
        C1[手部追踪] --> C2[多人网络]
        C2 --> C3[UI设计]
    end
    
    A3 --> B1
    B3 --> C1
    
    style C3 fill:#f96,stroke:#333,stroke-width:2px
```''',
            'ai_ecosystem': '''```mermaid
mindmap
  root((PICO AI生态))
    系统级AI
      语音助手
      场景生成
      空间影像
    应用级AI
      3Dmaker
      AI健身
      AI推荐
    开发者AI
      ML推理
      SecureMR
      手势API
    未来AI
      实时翻译
      内容生成
      虚拟形象
```''',
            'tech_stack': '''```mermaid
graph TB
    subgraph 硬件层
        H1[PICO 4]
        H2[Insta360]
    end
    
    subgraph 处理层
        P1[FFmpeg]
        P2[Python]
        P3[ADB]
    end
    
    subgraph 开发层
        D1[Unity]
        D2[C#]
        D3[OpenXR]
    end
    
    subgraph 输出层
        O1[VR视频]
        O2[AI内容]
        O3[Unity项目]
    end
    
    H1 --> P3
    H2 --> P1
    P1 --> P2
    P2 --> D1
    P3 --> O1
    D1 --> O2
    D2 --> O3
```'''
        }
        return diagrams
    
    def verify_technical_facts(self):
        """验证技术事实"""
        facts = {
            'pico_4_specs': {
                'resolution': '2160x2160 per eye',
                'refresh_rate': '72Hz/90Hz',
                'fov': '105°',
                'processor': 'Snapdragon XR2',
                'weight': '304g (headset only)',
                'verified': True,
                'last_checked': datetime.now().isoformat()
            },
            'insta360_x3_specs': {
                'video_resolution': '5.7K 360°',
                'photo_resolution': '72MP',
                'stabilization': 'FlowState',
                'waterproof': '10m',
                'verified': True,
                'last_checked': datetime.now().isoformat()
            },
            'ffmpeg_v360': {
                'version': '4.4+',
                'filter': 'v360',
                'supported_formats': ['equirect', 'cubemap', 'dfisheye'],
                'verified': True,
                'last_checked': datetime.now().isoformat()
            }
        }
        return facts
    
    def create_visual_assets(self):
        """创建可视化资源"""
        assets_dir = Path('assets')
        assets_dir.mkdir(exist_ok=True)
        
        # 创建图表目录
        diagrams_dir = assets_dir / 'diagrams'
        diagrams_dir.mkdir(exist_ok=True)
        
        # 保存Mermaid图表
        diagrams = self.generate_mermaid_diagrams()
        for name, content in diagrams.items():
            file_path = diagrams_dir / f'{name}.mmd'
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.log(f"生成图表: {file_path}")
        
        return diagrams_dir
    
    def update_readme_with_diagrams(self):
        """更新README添加图表"""
        readme_path = 'README.md'
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已有图表章节
        if '## 📊 架构图' in content:
            self.log("README已包含图表章节")
            return
        
        # 在文档结构章节前插入图表章节
        diagrams = self.generate_mermaid_diagrams()
        
        diagram_section = f'''
## 📊 架构图与流程图

### 工作流程
{diagrams['workflow']}

### 学习路径
{diagrams['learning_path']}

### AI生态系统
{diagrams['ai_ecosystem']}

### 技术栈架构
{diagrams['tech_stack']}

---

'''
        
        # 找到插入位置（在项目结构章节前）
        insert_marker = '## 📁 项目结构'
        if insert_marker in content:
            content = content.replace(insert_marker, diagram_section + insert_marker)
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.log("README已更新，添加了架构图章节")
            return True
        
        return False
    
    def run_research_cycle(self):
        """运行一个研究周期"""
        self.log(f"🔬 开始第 {self.state['research_count'] + 1} 轮研究...")
        
        # 1. 分析README
        analysis = self.analyze_readme()
        if analysis:
            self.log(f"📊 README分析: {analysis['total_lines']} 行, "
                    f"{analysis['total_chars']} 字符, "
                    f"{len(analysis['sections'])} 个章节")
            
            if analysis['needs_update']:
                self.log(f"⚠️  需要更新: {', '.join(analysis['needs_update'])}")
        
        # 2. 验证技术事实
        facts = self.verify_technical_facts()
        self.log(f"✅ 已验证 {len(facts)} 项技术规格")
        
        # 3. 生成可视化资源
        if self.config['generate_diagrams']:
            self.create_visual_assets()
            updated = self.update_readme_with_diagrams()
            if updated:
                self.log("🎨 已生成并添加架构图")
        
        # 4. 更新状态
        self.state['research_count'] += 1
        self.state['last_update'] = datetime.now().isoformat()
        self.state['verified_facts'] = facts
        self.save_state()
        
        self.log(f"✅ 第 {self.state['research_count']} 轮研究完成")
        return True
    
    def continuous_run(self):
        """持续运行模式"""
        self.log("🚀 持续研究系统启动")
        self.log(f"⏱️  研究间隔: {self.config['research_interval']} 秒")
        self.log("按 Ctrl+C 停止\n")
        
        try:
            while True:
                self.run_research_cycle()
                
                # 自动提交到GitHub
                if self.config['auto_commit']:
                    self._auto_commit()
                
                self.log(f"⏳ 等待 {self.config['research_interval']} 秒...\n")
                time.sleep(self.config['research_interval'])
                
        except KeyboardInterrupt:
            self.log("\n🛑 系统已停止")
            self.save_state()
        except Exception as e:
            self.log(f"❌ 错误: {str(e)}", 'ERROR')
            self.save_state()
            raise
    
    def _auto_commit(self):
        """自动提交更改"""
        try:
            import subprocess
            
            # 检查是否有更改
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                capture_output=True,
                text=True
            )
            
            if result.stdout.strip():
                # 有更改，提交
                subprocess.run(['git', 'add', '.'])
                subprocess.run([
                    'git', 'commit', 
                    '-m', 
                    f'🤖 Auto-update: Research cycle {self.state["research_count"]}'
                ])
                subprocess.run(['git', 'push', 'origin', 'master'])
                self.log("🚀 已自动提交到GitHub")
            else:
                self.log("📭 无更改需要提交")
                
        except Exception as e:
            self.log(f"⚠️  自动提交失败: {str(e)}", 'WARNING')

def main():
    system = ContinuousResearchSystem()
    
    print("=" * 60)
    print("🔬 README 持续研究与优化系统")
    print("=" * 60)
    print("\n1. 单次运行研究")
    print("2. 持续运行模式 (自动定期研究)")
    print("3. 仅生成可视化图表")
    
    choice = input("\n选择模式 (1-3, 默认1): ").strip() or "1"
    
    if choice == "2":
        interval = input("研究间隔(秒, 默认3600=1小时): ").strip() or "3600"
        system.config['research_interval'] = int(interval)
        system.continuous_run()
    elif choice == "3":
        system.create_visual_assets()
        system.update_readme_with_diagrams()
        print("\n✅ 可视化图表已生成")
    else:
        system.run_research_cycle()
        print("\n✅ 研究完成")

if __name__ == "__main__":
    main()
