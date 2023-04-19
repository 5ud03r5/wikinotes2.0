<div align="center"><img src="https://user-images.githubusercontent.com/94323029/232141915-ce6074f8-3257-46e1-94fd-273b60657154.png"/></div>

<div align="center">
  <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/>
  <img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" /></div>
  
# Description
WikiNotes2.0 will be an improved version of my previous unfinished WikiNotes project.
It aims to be a platform to allow engineers share knowledge in terms of articles and notes. It also allows for easy article/note search with easy markdown syntax based creation. 

## Installation

WikiNotes tool requires you to have docker installed on your workstation/server. First clone git repository, then run following command from root project directory:

    docker compose up 

It will run docker containers (backend, frontend and postgres db)

If you dont want to use it as a docker, but instead use your own postgresql database, you can clone repository and modify line 9 in backend/db/database.py with your postgresql settings

