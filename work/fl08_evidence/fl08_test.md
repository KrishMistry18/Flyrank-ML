# FL-08 Live Test Record

**Date/Time:** 2026-09-13
**URL Tested:** `https://portfolio-eta-pied-17.vercel.app/api/chat`
**Test Method:** Live POST request mimicking the frontend UI flow.

## The Test

**Question:**
`"What AI projects has Krish built?"`

**Actual Response Received:**
```json
{
  "reply": "Krish has built several projects incorporating AI and Machine Learning components:\n\n-   **ImpactGlobe**\n    -   **Description:** An offline-first incident reporting app with local AI inference.\n    -   **Problem:** Communities needed a reliable way to report incidents (accidents, hazards, garbage) even without internet access, while keeping sensitive photos off cloud servers.\n    -   **AI Components:** On-device inference using `MobileNetV3` CNN (Transfer Learning) to classify incidents. It also includes heuristic regression for real-time CO2 emissions tracking.\n    -   **Technologies:** `Flutter`, `TensorFlow`, `MobileNetV3`, `Firebase`, `Python`.\n    -   **Key Decision:** Choosing on-device inference (`MobileNetV3`) over a cloud API to eliminate latency, enable offline functionality, and ensure sensitive incident photos remain off external servers.\n\n-   **CrowdPulse**\n    -   **Description:** A real-time Crowd Analysis Dashboard.\n    -   **Problem:** Proactively identifying crowd anomalies requires high-accuracy tracking and low latency.\n    -   **AI Components:** Real-time object detection and density mapping pipelines using `YOLOv8` tracking algorithms, deployed on Hugging Face Spaces.\n    -   **Technologies:** `Python`, `Flask`, `YOLOv8`, `PyTorch`, `CUDA`, `Hugging Face Spaces`.\n    -   **Key Decision:** Optimized `YOLOv8` algorithms and moved AI inference to an NVIDIA GPU (`CUDA 12.1`) to achieve real-time processing speeds without sacrificing precision.\n\n-   **AyurWell**\n    -   **Description:** An AI-generated diet plans & dosha assessment application.\n    -   **Problem:** Safely generating highly personalized Ayurvedic diet plans based on user surveys.\n    -   **AI Components:** Integrated `LLMs` with strict prompt chaining and validation layers to generate personalized, season-aware dietary plans. It also uses a scoring algorithm to map user survey inputs to Ayurvedic Dosha profiles.\n    -   **Technologies:** `Vite`, `React`, `Django REST`, `Tailwind`, `LLMs`.\n    -   **Key Decision:** Implemented a strict prompt chaining pipeline with validation layers to ensure the AI generated safe health advice."
}
```

## Result Summary
- **Did the full flow work?** Yes. The request hit the live Vercel endpoint, the backend correctly injected the portfolio knowledge, communicated with the Gemini API using the secure server-side key, and returned a rich, accurate response based strictly on my verified projects.
- **Failures/Fallbacks Observed:** None on this query. The Gemini API responded perfectly.
