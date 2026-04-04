# GEMINI.md - PICO 4 & Insta360 Full-Auto Pipeline

## Project Overview
This project provides a full-auto pipeline for converting and syncing Insta360 VR content to PICO 4 headsets.

## Automation Pipeline
1.  **Ingestion**: User places `.insv` files into the `raw/` directory.
2.  **Conversion (`convert_360.py`)**:
    *   Uses FFmpeg with the `v360` filter for stitching.
    *   Template configured for Insta360 X3/X4 dual-fisheye files.
    *   Outputs H.265 MP4 into the `exports/` directory.
3.  **Synchronization (`sync_to_pico.py`)**:
    *   Monitors `exports/` for new MP4 files.
    *   Pushes files to PICO 4 via `adb push`.

## Key Files
- `convert_360.py`: The core stitching script (Requires FFmpeg).
- `sync_to_pico.py`: The ADB-based transfer tool.
- `README.md`: End-user documentation (Bilingual).
- `raw/` & `exports/`: Ingestion and processing directories.

## Development & Environment
- **Prerequisites**: FFmpeg, Python 3, ADB (Android Platform Tools).
- **Deployment**: `https://github.com/kevinten-ai/pico4-insta360-guide`.
