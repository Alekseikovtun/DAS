# Installation Guide
1. Clone a repository using the <**git clone https://github.com/Alekseikovtun/DAS.git -b stage**> command
2. Create a virtual environment
3. Use the <**pip install -r .\requirements.txt**> command
4. Create a <**.env**> file in the root of the project
5. Write it to a file .env data, as in the <**env_template**> file
- In DB_OUT_PORT  write the port that Docker will accept (example: 5001)
- In DB_USER write the name of the user who is the administrator (example: postgres)
- In DB_PASSWORD write the password with which the administrator will connect to the database (example: postgres)
- In DB_DATA write <**./artifacts/db**>
- In DB_NAME write the DB name
6. Install **Docker Desktop**
7. Run the command <**docker compose -f (the path to the file docker-compose.yml) up**>
