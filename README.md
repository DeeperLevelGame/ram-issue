# RAM Usage Issue Demo

This repository demonstrates a memory (RAM) usage issue when using Streamlit, with repeated reruns causing significant memory increase. 

## Steps to Reproduce the Issue

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/ram-issue.git
   cd ram-issue
2. ```
   pip install -r requirements.txt
3. ```
   streamlit run .\ram_issue_demo.py
4. Click the Rerun button repeatedly to see the RAM usage increase. Aditionally, uncomment line 13-17 to see the increase of RAM usage by data being set in the chart.
