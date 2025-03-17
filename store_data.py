from google.oauth2 import service_account
from googleapiclient.discovery import build

service = build("sheets", "v4", credentials=credentials)

SHEET_ID = "your_google_sheet_id"
RANGE_NAME = "Sheet1!A1:B1"

values = [["Timestamp", "Sensor Value"], ["2025-03-10 10:00:00", 23.5]]
body = {"values": values}

request = service.spreadsheets().values().update(
    spreadsheetId=SHEET_ID,
    range=RANGE_NAME,
    valueInputOption="RAW",
    body=body
)
response = request.execute()
print("Data stored in Google Sheets:", response)