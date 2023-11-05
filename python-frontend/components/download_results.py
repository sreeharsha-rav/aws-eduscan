import pandas as pd
import base64

# Function to create link to download the results in csv format
def download_csv(data):
    df = pd.DataFrame(data)
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="results.csv">Download CSV</a>'
    return href
