🌟 Visual Novelty Detector
AI system that detects unseen objects, unusual events, and anomalies in CCTV footage

The Visual Novelty Detector is an AI-powered security system that identifies new, unusual, or suspicious visual events in real-time.
Instead of detecting known objects (cars, people, etc.), it detects novel events such as:

A new person entering the scene

A new vehicle that wasn’t observed before

Abnormal motion patterns

Moved or removed objects

Unusual activity in restricted zones

This project is ideal for:
✔ CCTV analytics
✔ Smart surveillance
✔ Security automation
✔ Research in anomaly/novelty detection

🚀 Features

🔍 1. Novel Object Detection

Automatically identifies new visual elements that were not previously in the frame.

🧠 2. Novelty Score Engine

Each frame is assigned a novelty score using deep-learning embeddings.

🗂 3. Local Novelty Database

Stores all novelty logs (embeddings + timestamps) in a lightweight DB.

🎯 4. Motion & Event Tracking

Tracks objects across frames to check if they reappear or behave abnormally.

🎥 5. Real-Time Processing

Processes video streams frame-by-frame with optimized inference.

📂 Project Structure

<img width="756" height="388" alt="image" src="https://github.com/user-attachments/assets/43bf2c8d-9235-4f3d-9540-a566728c9490" />

🛠 Tech Stack

Python 3.8+

OpenCV

Scikit-Learn

Ultralytics YOLO (optional)

NumPy

SQLite (for novelty DB)

Faiss / Cosine similarity for embeddings (if enabled)

⚙️ Installation

1. Clone the repository
   
   <img width="810" height="160" alt="image" src="https://github.com/user-attachments/assets/de586e6c-8fe9-4469-90ae-f696c2977c18" />

3. Create virtual environment (recommended)
   
   <img width="720" height="126" alt="image" src="https://github.com/user-attachments/assets/1f016057-01f3-40df-8934-c5256d5e8c44" />

   Activate:

      Windows:
   
   <img width="689" height="126" alt="image" src="https://github.com/user-attachments/assets/b0dc44bc-5c47-43f9-a222-9745047d585a" />


   Linux/Mac:
   
   <img width="696" height="125" alt="image" src="https://github.com/user-attachments/assets/15e30a54-1a76-42ae-930d-83f3194c9348" />

5. Install dependencies
   
   <img width="731" height="123" alt="image" src="https://github.com/user-attachments/assets/5a13c59c-84a2-48db-a846-067fae76492a" />

▶️ How to Run

Simply run:

   <img width="704" height="127" alt="image" src="https://github.com/user-attachments/assets/9f37128b-4a3c-4be9-94d9-84ef129e0a35" />
   
The detector will:
✔ Load the camera/video
✔ Analyze the stream
✔ Highlight unusual objects
✔ Store novelty events in the DB
✔ Display them in real-time

📊 How Novelty Score Works

Each frame → converted into an embedding → compared vs previous embeddings.

If distance > threshold, it’s classified as novel.

Example algorithm:

Embedding model → vector of 512 dimensions

Compute cosine similarity

Lower similarity = higher novelty

Novelty score formula:

<img width="846" height="122" alt="image" src="https://github.com/user-attachments/assets/fc1efc30-f7b4-4224-8631-bf9dcfe4e17b" />

📁 Outputs

All novel events are saved in:

<img width="755" height="229" alt="image" src="https://github.com/user-attachments/assets/c1e2dcf7-a0d6-431e-817e-9a4bd7df0757" />

Each log contains:

<img width="768" height="295" alt="image" src="https://github.com/user-attachments/assets/e6bdf48d-d8ec-4fcf-9c9f-2a39063eb2a9" />

📌 Use Cases

🔐 Security Surveillance

Detect new people entering restricted areas.

🚗 Parking & Vehicle Monitoring

Detect unknown vehicles.

🏭 Industrial Safety

Detect unusual behavior or anomalies in factories.

🧠 Research in Anomaly Detection

Provides a simple architecture for academic work.

📸 Screenshots (Optional)

Add your sample output images here:

<img width="570" height="157" alt="image" src="https://github.com/user-attachments/assets/bf003bf0-43f1-4e28-aa5e-e7cdd429c0cf" />

👨‍💻 Author

Amrit Kumar Das (AK)

⭐ Show Some Love

If you like this project, give it a ⭐ on GitHub!

