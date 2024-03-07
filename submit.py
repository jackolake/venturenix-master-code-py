from google.cloud import storage
import hashlib
import time
from pathlib import Path
import ntplib

BUCKET_NAME = "python-2024-submission"

# Check local files existence
required_files = [
    'private_key',
    'python-contest-submission.json',
    'module.py',
    'requirements.txt'
]

for f in required_files:
    if not Path(f).is_file():
        raise ModuleNotFoundError(f"{f} is not found")

# get private_key digest
with open('private_key', "rb") as f:
    userid = hashlib.sha1(f.read()).hexdigest()

# Check time diff with NTP
ntpc = ntplib.NTPClient()
timediff = ntpc.request('stdtime.gov.hk', version=3).delay
if abs(timediff) > 1:
    raise SystemError("System time is incorrect")

# Upload required files
upload_files = [
    'module.py',
    'requirements.txt'
]

prefix = str(userid) + "/" + str(time.time())+'_'

storage_client = storage.Client.from_service_account_json("python-contest-submission.json")
bucket = storage_client.bucket(BUCKET_NAME)
print(f"Uploading files at {time.ctime(time.time()+timediff)}")
try:
    for f in upload_files:
        blob = bucket.blob(prefix + f)
        blob.upload_from_filename(f)
except:
    print("Error uploading file, please ask for help")
storage_client.close()