#🪨📄✂️ **Rock Paper Scissor Detection App**

A simple and interactive web application built with Streamlit that uses YOLOv8 to detect hand gestures — Rock, Paper, or Scissors — in uploaded images.

#**📸 Features**
Upload an image containing hand gestures.

Detects whether the gesture is Rock, Paper, or Scissor using a trained YOLOv8 model.

Beautiful, responsive UI with gesture examples.

Fast and accurate predictions.

#🛠️ **Tech Stack**
Python 🐍

Streamlit 📈

YOLOv8 (via Ultralytics) 🎯

PIL & OpenCV for image processing

#🔧 **Setup Instructions**
Clone the repository:

```#bash
git clone https://github.com/suveshak/Rock_Paper_Scissor.git
cd Rock_Paper_Scissor
```
```#bash
Install dependencies:
pip install streamlit pillow opencv-python ultralytics
```
**Add the YOLO model:
**
Place your last.pt file in the root directory or appropriate path as referenced in the code.

**Run the app:**

```#bash
streamlit run app.py
```
#📁 **Project Structure**
```#bash
Rock_Paper_Scissor/
│
├── app.py              # Main Streamlit app
├── last.pt             # Trained YOLOv8 model (not included in repo)
└── README.md           # Project documentation
```

**The simplest option is to deploy on Streamlit Community Cloud:**

Push your code (with last.pt) to GitHub.

Go to streamlit.io/cloud and connect your GitHub.

Choose the repository and select app.py as the entry point.

Done! 🎉

If you're still set on using Vercel, it requires a workaround using Docker. Let me know and I can help you containerize it.

#✨ **Credits**
Ultralytics YOLOv8

Streamlit

World RPS Society for sample images

#📜 **License**
This project is licensed under the MIT License.

