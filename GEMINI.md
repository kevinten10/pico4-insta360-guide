# GEMINI.md - PICO 4 & Insta360 Guide Project

## Project Overview
This project provides a comprehensive workflow and automation tools for viewing Insta360 VR content on PICO 4 headsets.

## Key Components
- `sync_to_pico.py`: A Python automation script that monitors the `exports/` directory and syncs MP4 files to the connected PICO 4 device via ADB.
- `README.md`: Bilingual documentation (CN/EN) detailing the best export settings (H.265, 5.7K) and playback modes.
- `requirements.txt`: Python dependencies (e.g., `watchdog`).
- `LICENSE`: MIT License.

## Development & Usage
1.  **Environment Setup**: Ensure `adb` (Android Debug Bridge) is installed in the system PATH.
2.  **Script Execution**: Run `python sync_to_pico.py` to start the file monitor.
3.  **Deployment**: All updates should be pushed to `https://github.com/kevinten-ai/pico4-insta360-guide`.

## Future Roadmap
- [ ] Add support for wireless transfer via AirScreen/Skybox protocol.
- [ ] Implement a GUI for the synchronization script.
- [ ] Create a "best settings" export preset for Insta360 Studio.
