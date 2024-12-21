import os
import psutil
import pandas as pd
import streamlit as st
from lightweight_charts.widgets import StreamlitChart

def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_in_mb = process.memory_info().rss / (1024 * 1024)
    return memory_in_mb

chart = StreamlitChart(toolbox=True, height=150, width=150, inner_width=1, inner_height=1)
# data = pd.DataFrame({
#         'Date': pd.date_range(start='2024-01-01', periods=10000, freq='D'),
#         'Value': range(1, 10001)  
#     })
# chart.set(data)

if st.button("Rerun"):
    st.rerun()

if 'previous_ram' not in st.session_state:
    st.session_state.previous_ram = 0

ram = get_memory_usage()
ram_increase = ram - st.session_state.previous_ram

st.session_state.previous_ram = ram
st.write("Streamlit Cache and Memory Usage Demo")
st.write(f"Memory Usage: {ram:.2f} MB")
st.write(f"Memory Increase Since Last Run: {ram_increase:.2f} MB")
