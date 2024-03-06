# Venturenix Master Code 2024
## Python Edition

This repo contains the code for Venturenix Master Code 2024.

### Code execution
The following instructions is applcable to MacOS terminal, Windows WSL and Linux. For specfic IDE please proceed accordingly.

In order to compete without problem, please ensure:

1. Have a virtual environment setup for the competition
```bash
python3 -m venv ~$USER/venv/mastercode2024
source ~$USER/venv/mastercode2024/bin/activate
```
2. Clone the repo to your local computer
```bash
git clone git@github.com:hfvtx/venturenix-master-code-py.git
```

3. Environment is properly setup
```bash
cd venturenix-master-code-py
pip install -r requirements.txt
```
4. Try to run the code and see if it runs successfully
```bash
python3 main.py

Running answers...
Benchmarking...

Reference
---------
Memory usage: 2601.18125Mb
Average CPU: 0.45545
Benchmark CPU time: 2.911
Final Score (reference only): 416743.72804
```

### Code Submission
In order to submit your code, you need to download 2 files separately. __Please make sure to download both files into same folder containing the code. Do NOT rename the files.__
1. Personal private key

   Login to https://vtx-python-contest.softr.app/ by using the magic link sent to your personal e-mail box.  The filename should be `private_key`.
2. Service account json

   URL will be provided to the participants onsite.

Once both files are in place, you could submit your code with the following command.
```bash
python3 submit.py

Uploading files at Thu Mar  7 01:03:29 2024
```
If you install new libraries into the environment, please ensure to update `requirements.txt` before submission or the scoring process will fail.
```bash
pip freeze > requirements.txt
```
__When time is up, the service account will be disabled and submission will fail. Please make sure to submit before time__

### Score
Your official score is available at: https://vtx-python-contest.softr.app/leaderboard-list