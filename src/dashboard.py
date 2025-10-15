import streamlit as st
import pandas as pd
import time

FILE_PATH = "data/sensor_data.csv"

st.set_page_config(page_title="Industrial Monitoring Dashboard", layout="wide")

st.title("🏭 Industrial Data Monitoring Dashboard")
st.markdown("Real-time monitoring of simulated machine temperature and pressure.")

placeholder = st.empty()

while True:
    df = pd.read_csv(FILE_PATH)
    df = df.tail(50)  # show latest 50 readings

    temp_alerts = df[df["Temperature"] > 100]
    pressure_alerts = df[df["Pressure"] < 950]

    with placeholder.container():
        st.subheader("📊 Live Sensor Data")
        st.line_chart(df[["Temperature", "Pressure"]])

        st.subheader("🚨 Alerts")
        if not temp_alerts.empty or not pressure_alerts.empty:
            st.error("⚠️ Abnormal readings detected!")
            st.dataframe(pd.concat([temp_alerts, pressure_alerts]))
        else:
            st.success("✅ All systems normal.")

        st.caption(f"Last updated: {df['Timestamp'].iloc[-1]}")

    time.sleep(2);
