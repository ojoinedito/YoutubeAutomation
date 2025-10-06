import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
creds = flow.run_console()
yt = build("youtube", "v3", credentials=creds)

body = {
    "snippet": {
        "title": "Horror Short",
        "description": "AI ile üretilen korku kısa filmi",
        "tags": ["horror", "shorts", "español"],
        "categoryId": "27"
    },
    "status": {"privacyStatus": "public"}
}
yt.videos().insert(part="snippet,status",
                   body=body,
                   media_body="output.mp4").execute()
print("YouTube’a yüklendi.")
