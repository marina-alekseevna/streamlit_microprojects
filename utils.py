import pandas as pd
import base64
# Source: https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def download_file(df, name):
    csv = df.to_csv(index=False)

    b64 = base64.b64encode(csv.encode()).decode()  
    href = f'<a href="data:file/csv;base64,{b64}" download="{name}.csv">Download CSV File</a>'
    return href