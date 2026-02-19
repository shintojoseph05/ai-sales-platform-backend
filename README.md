# AI Sales Platform Backend

Backend service for my AI Sales Automation SaaS.

## Tech Stack

- Python 3.10+
- FastAPI (for API)
- pytest (for tests)
- Virtualenv for isolation

## Setup

```bash
# Clone repository
git clone https://github.com/<your-username>/ai-sales-platform-backend.git
cd ai-sales-platform-backend

# Create & activate virtual env (Windows)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create env file
copy .env.example .env
# then edit .env with your real API keys
