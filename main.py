from datetime import date  # Core python module
import pandas as pd  # pip install pandas
from send_emails import send_email  # Local python module
import gspread

# Public GoogleSheets URL

SHEET_ID = "1EwwY-zWdRTpHzjIpGrdqdfF-DPx9vppkzej7v0la3fc"
SHEET_NAME = "Tasks"
URL = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(SHEET_ID, SHEET_NAME)
df = pd.read_csv(URL)


def load_df(URL):
    parse_data = ["Start date", "Due on"]
    df = pd.read_csv(URL, parse_dates=parse_data)
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["Due on"].date()):
            send_email(
            subject="[CSP Bi-Weekly Accomplishments]",
            receiver_email=["sambamjalloh@gmail.com"],
        )
        email_counter += 1
    
    return f"Total Emails Sent: {email_counter}"

df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)
