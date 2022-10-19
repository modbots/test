# (c) @modbots

# Don't Forget That I Made This!
# So Give Credits!
import os
class Config(object):
	BOT_TOKEN = "1952639092:AAHZ6p4FlhaIDO3E55eKKumu2twBMf3NvtE"
	API_ID = 7810305
	API_HASH = "2f25ab3cb4ea9708817581fbde570821"
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = -1001243842447
	UPDATES_CHANNEL = -1001450359206
	DOWN_PATH = "./downloads"
	PRESET = "ultrafast"
	OWNER_ID = 1247136776
	DEF_WATER_MARK_FILE = "https://www.freepnglogos.com/uploads/instagram-logo-png-transparent-0.png"
	CAPTION = "By @AHToolsBot"
	BOT_USERNAME = "VideoWatermark_Bot"
	DATABASE_URL = "mongodb+srv://minnhtetkyaw:thinnmyatoo@cluster0.j5g9f.mongodb.net/Cluster0?retryWrites=true&w=majority"
	BROADCAST_AS_COPY = True
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
	
Hi, I am Channel Bot!
You are not support to be Here...
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""