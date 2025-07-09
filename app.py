import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np
import threading
import queue
import time

# ==================== CONFIG & SETUP ====================
st.set_page_config(page_title="YOLO 12 Detection", layout="centered")
model = YOLO("yolo12n.pt")

st.title("🎯 Deteksi Objek dengan YOLO 12")

# ==================== MENU NAVIGASI ======================
mode = st.sidebar.radio("Pilih Mode Deteksi", ["📸 Webcam", "🖼️ Upload Foto"])

if mode == "📸 Webcam":
    st.subheader("🔴 Deteksi Objek via Webcam")

    col1, col2 = st.columns(2)
    start = col1.button("▶️ Mulai Deteksi")
    stop = col2.button("🛑 Stop Deteksi")

    FRAME_WINDOW = st.empty()
    status_box = st.empty()

    # Queue untuk komunikasi frame dari thread capture ke main thread
    frame_queue = queue.Queue()
    stop_event = threading.Event()

    def capture_and_detect(stop_event, q):
        cap = cv2.VideoCapture(0)
        while not stop_event.is_set():
            ret, frame = cap.read()
            if not ret:
                status_box.error("🚫 Gagal mengambil frame dari kamera.")
                break
            results = model(frame)[0]
            annotated = results.plot()
            q.put(annotated)
            time.sleep(0.03)  # untuk batasi fps sekitar 30

        cap.release()

    # Simpan thread di variabel global supaya tidak mati garbage collector
    if 'thread' not in st.session_state:
        st.session_state.thread = None

    if start and (st.session_state.thread is None or not st.session_state.thread.is_alive()):
        stop_event.clear()
        st.session_state.thread = threading.Thread(target=capture_and_detect, args=(stop_event, frame_queue), daemon=True)
        st.session_state.thread.start()
        status_box.success("✅ Deteksi dimulai... Klik Stop untuk berhenti.")

    if stop:
        stop_event.set()
        status_box.info("ℹ️ Deteksi dihentikan.")

    # Loop update UI di main thread
    while True:
        if not frame_queue.empty():
            frame = frame_queue.get()
            FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), caption="Live Camera Feed", use_column_width=True)
        time.sleep(0.01)
        # Perlu cara break loop kalau stop_event sudah set
        if stop_event.is_set():
            FRAME_WINDOW.empty()
            break

elif mode == "🖼️ Upload Foto":
    st.subheader("🟢 Deteksi Objek dari Gambar")

    uploaded_file = st.file_uploader("📤 Upload Gambar", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        results = model(img)[0]
        annotated_img = results.plot()

        st.image(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB),
                 caption="🖼️ Hasil Deteksi", use_column_width=True)
