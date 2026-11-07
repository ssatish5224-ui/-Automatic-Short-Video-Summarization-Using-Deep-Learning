import os
import tempfile
from pathlib import Path

import cv2
import numpy as np
import streamlit as st
from PIL import Image

from summarizer import summarize_video

st.set_page_config(page_title="AI Video Summarizer", page_icon="🎬", layout="wide")
st.title("🎬 Automatic Short-Video Summarization")
st.caption("Deep Learning-based key moment selection using MobileNetV2")

with st.sidebar:
    st.header("Summary settings")
    segment_seconds = st.slider("Segment length (seconds)", 2, 10, 5)
    summary_seconds = st.slider("Target summary duration (seconds)", 5, 60, 20)
    st.info("The model samples frames, extracts MobileNetV2 features, scores segments, and joins the best non-overlapping moments.")

uploaded = st.file_uploader("Upload a video", type=["mp4", "avi", "mov", "mkv"])

if uploaded:
    suffix = Path(uploaded.name).suffix or ".mp4"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded.getbuffer())
        input_path = tmp.name

    st.subheader("Input video")
    st.video(input_path)

    if st.button("Generate summary", type="primary"):
        with st.spinner("Analyzing video frames and selecting important moments..."):
            try:
                result = summarize_video(
                    input_path,
                    segment_seconds=segment_seconds,
                    target_seconds=summary_seconds,
                    output_dir="outputs",
                )
                st.success("Summary generated successfully!")
                st.subheader("Short summary video")
                st.video(result["summary_path"])

                left, right = st.columns(2)
                left.metric("Original duration", f'{result["original_duration"]:.1f} sec')
                right.metric("Summary duration", f'{result["summary_duration"]:.1f} sec')

                st.subheader("Selected timestamps")
                for item in result["segments"]:
                    st.write(
                        f'**{item["start"]:.1f}s – {item["end"]:.1f}s** '
                        f'(importance score: {item["score"]:.3f})'
                    )
                    if os.path.exists(item["thumbnail"]):
                        st.image(item["thumbnail"], width=320)

                with open(result["summary_path"], "rb") as f:
                    st.download_button(
                        "⬇️ Download summary video",
                        data=f,
                        file_name="video_summary.mp4",
                        mime="video/mp4",
                    )
            except Exception as exc:
                st.error(f"Could not summarize this video: {exc}")
                st.info("Try a short MP4 video with a standard video codec.")
    os.unlink(input_path)
else:
    st.info("Upload an MP4, AVI, MOV, or MKV video to begin.")
