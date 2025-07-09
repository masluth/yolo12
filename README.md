🧠 Apa Itu YOLOv12?
YOLOv12 (You Only Look Once version 12) adalah versi terbaru dari keluarga arsitektur real-time object detection yang sangat populer dan efisien. YOLO dirancang untuk mendeteksi objek dalam gambar atau video dengan kecepatan tinggi dan akurasi tinggi dalam sekali proses.

🚀 Fitur dan Keunggulan YOLOv12
YOLOv12 dikembangkan oleh tim Ultralytics dan melanjutkan peningkatan dari versi-versi sebelumnya seperti YOLOv5, v8, dsb.

🔧 1. Arsitektur Modular & Efisien
Menggunakan backbone dan head yang dioptimalkan.

Kombinasi teknologi CNN dan attention mechanism (opsional).

Ukuran model lebih ringan (misalnya yolo12n.pt untuk versi nano).

🧪 2. Kemampuan Deteksi Multi-Objek
Dapat mendeteksi banyak objek dalam satu frame sekaligus.

Cocok untuk aplikasi seperti CCTV, robotik, kendaraan otonom, dan AI camera.

⚙️ 3. Dukungan Format dan API Lengkap
Bisa digunakan di Python melalui ultralytics library.

Mendukung model .pt (PyTorch) dan ONNX untuk deployment di device edge (mobile, Jetson, dsb).

📦 4. Pretrained dan Custom Model
Tersedia versi pre-trained untuk dataset umum (seperti COCO).

Bisa dilatih ulang (fine-tune) untuk dataset spesifik kamu (misalnya deteksi helm, sampah, dll).

📈 Performa
Model	Ukuran	FPS (GPU)	Akurasi (mAP)
YOLOv12n	Sangat ringan	⚡ Cepat (>100 FPS)	Baik untuk real-time
YOLOv12m/l/x	Lebih besar	Lebih akurat	Cocok untuk proyek dengan fokus akurasi tinggi
