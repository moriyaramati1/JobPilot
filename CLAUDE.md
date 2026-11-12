# JobPilot

Job-application tracker. api/ = FastAPI (Python 3.12), web/ = Next.js + TypeScript.

## Commands
- API: cd api && uvicorn app.main:app --reload
- Tests: cd api && pytest

## Rules
- Every new endpoint gets a pytest test.
- Never read or edit .env files.
- Small commits with conventional messages (feat:, fix:, chore:).