 🏭 Industrial Data Monitoring Dashboard

**Developer:** Bashiq Ali    

---
📖 Overview
This project simulates an industrial sensor monitoring system that tracks machine temperature and pressure in real time.  
It visualizes live data with Streamlit and automatically generates alerts when readings exceed safe thresholds.

It demonstrates:
- Technical troubleshooting  
- Data visualization and alerting  
- Understanding of industrial monitoring (similar to AVEVA PI System)

---

⚙️ Features
- Real-time data simulation  
- Live dashboard with graphs  
- Automatic anomaly detection (Temperature > 100 °C, Pressure < 950 hPa)  
- Continuous data logging  
- Troubleshooting log

---

🛠️ Tech Stack
Python 3 | Streamlit | Pandas | NumPy | Matplotlib

---

🚀 How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/bashiqali111/industrial-data-monitoring-dashboard.git
   cd industrial-data-monitoring-dashboard

2. Clone or Download the Project

If you have Git installed:

git clone https://github.com/bashiqali111/industrial-data-monitoring-dashboard.git
cd industrial-data-monitoring-dashboard


Or, download the ZIP file manually from GitHub → “Code” → “Download ZIP”
Then extract it and open the folder in VS Code.

3.Install Dependencies

Run this inside your project folder:

pip install -r requirements.txt


This installs:
streamlit
pandas
numpy
matplotlib

4. Start the Data Generator

Run the script that simulates temperature and pressure readings:

python src/data_generator.py


✅ This will create a file data/sensor_data.csv and continuously add new readings every second.
Keep this terminal open and running.

5. Launch the Dashboard

Open a new terminal tab (or window) and run:

python -m streamlit run src/dashboard.py


After a few seconds, your default web browser will open automatically at:

http://localhost:8501


You’ll see:

📊 Real-time updating line graphs

✅ “All systems normal” when values are safe

⚠️ “Abnormal readings detected!” when Temperature > 100°C or Pressure < 950 hPa

6. Stop the Program

To stop:

In each terminal window, press Ctrl + C

You’ll see: Dashboard stopped manually.
That’s completely normal.
