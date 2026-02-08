# QA signup automation script of this website https://authorized-partner.vercel.app/






## Environment / Setup

### Language
- Python 3.12+

### Framework
- Playwright (Python)

### Browser Driver
- Playwright Chromium browser (auto-managed by Playwright)

### Operating System
- Tested on Windows 10/11

---

## Prerequisites

Make sure the following are installed:

### 1. Install Python
Download from:
https://www.python.org/downloads/

Verify installation:

```bash
python --version

#Install Playwright
pip install playwright


#Install browser dependencies
python -m playwright install

#install chromium for playwright
python -m playwright install chromium



#Run the automation script
to run go to powershell or terminal
go to folder where the script is written
cd documents

then run python signup_automation_script1.py


for testing automatically chrome browser open 

for test data dummy values

| Field      | Value                                         |
| ---------- | --------------------------------------------- |
| First Name | Diwas                                         |
| Last Name  | Kushwaha                                      |
| Email      | [diwas@example.com](mailto:diwas@example.com) |
| Phone      | 982964746                                     |
| Password   | TestPassword123                               |
