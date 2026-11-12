# JobPilot BE

Job-application tracker. api/ = FastAPI (Python 3.12)


## Rules
- Every new endpoint gets a pytest test.
- Never read or edit .env files.
- Small commits with conventional messages (feat:, fix:, chore:).
- the app client module in a separate file for tests and also for app.
- each api endpoint should be declared on different file under api folder.
- the return types should be a formed with returned type model - use pydantic for that and name it with meaning.
- returned types should be in a separate file under types folder.
- status code should be used from http package and not as hard coded.
-  save the tested route as variable and not hurd coded and declare them in separate file