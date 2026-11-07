# Automatic Short-Video Summarization Using Deep Learning

**Student:** DAYANANDA  
**Register No.:** 8080152

## Project description
This application creates a shorter video by identifying visually distinctive moments in a longer video. It uses a pretrained MobileNetV2 network to extract deep visual features from sampled frames. A documented scoring method combines visual feature novelty and frame-to-frame motion, then selects high-scoring non-overlapping time segments.

## Main workflow
Video upload → Frame sampling → MobileNetV2 feature extraction → Segment scoring → Non-overlapping selection → Summary MP4 + timestamps + thumbnails.

## Setup (Windows / VS Code)
1. Install Python 3.10–3.12.
2. Extract this ZIP.
3. Open the extracted folder in VS Code.
4. Open Terminal and run:

```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, run this once in the same terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

5. Open the local Streamlit address shown in the terminal (usually http://localhost:8501).
6. Upload a video and click **Generate summary**.

## Notes
- The first run may download MobileNetV2 ImageNet weights and may take some time.
- Use a video you own or have permission to process.
- The summary is an automatically selected visual highlight preview, not a guarantee that every narrative-important event is included.
- The output video is written to `outputs/video_summary.mp4`.
- This starter implementation analyzes visual frames. Audio features are optional and are not included.
- For best compatibility, use a standard MP4 (H.264) input.
