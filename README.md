# Installation Guide
1. Clone a repository using the <**git clone https://github.com/Alekseikovtun.git**> command
2. Create a virtual environment
3. Use the <**pip install -r .\requirements.txt**> command
4. Create a <**.env**> file in the root of the project
5. Write it to a file .env data, as in the <**env_template**> file
- In DB_DATA write <**./artifacts/db**>
6. Install **Docker Desktop**
7. Run the command <**docker compose -f (the path to the file docker-compose.yml) up**>
8. Run the command <**uvicorn entry:app --reload --port 8080**>
