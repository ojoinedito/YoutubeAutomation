import os, requests

os.makedirs("videos", exist_ok=True)
headers = {"Authorization": os.getenv("PEXELS_API_KEY")}
params = {"query": "dark forest", "per_page": 3}
data = requests.get("https://api.pexels.com/v1/videos/search",
                    headers=headers, params=params).json()
for i, v in enumerate(data["videos"]):
    url = v["video_files"][0]["link"]
    resp = requests.get(url)
    with open(f"videos/clip{i+1}.mp4", "wb") as f:
        f.write(resp.content)
    print(f"videos/clip{i+1}.mp4 indirildi.")
