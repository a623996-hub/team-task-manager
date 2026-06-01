# Team Task Manager System

## Project Overview
The Team Task Manager System is a full-stack web application developed to manage projects and tasks between Admin and Users. The system provides role-based access control where Admin can create projects, assign tasks and manage users, while Users can view and update their assigned tasks.

This project demonstrates REST API development, database integration, CRUD operations, authentication and deployment.

---

## Technologies Used

### Backend
- FastAPI
- Python
- SQLAlchemy
- PostgreSQL

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Render (Backend)
- Netlify (Frontend)

---

## Features

### Admin Features
- Admin Login
- Create Projects
- Create Tasks
- Assign Tasks to Users
- View All Projects
- View All Tasks
- Delete Tasks

### User Features
- User Login
- View Assigned Tasks
- Update Task Status
- Mark Task as:
  - Pending
  - In Progress
  - Completed

---

## CRUD Operations
The project supports complete CRUD operations:

- Create Project
- Read/View Projects
- Create Tasks
- Update Task Status
- Delete Tasks

---

## REST APIs
The backend is developed using FastAPI and provides RESTful APIs for:

- Authentication
- Project Management
- Task Management
- User Management

Swagger API documentation is available using:

/docs

---

## Database
PostgreSQL database is used for storing:

- Users
- Projects
- Tasks

The database relationships and validations are implemented using SQLAlchemy ORM.

---

## Authentication & Authorization
The system uses role-based access control:

- Admin Role
- User Role

Only Admin can create projects and tasks.

---

## Deployment Links

### Backend
https://team-task-manager-y8ut.onrender.com

### Frontend
team-task-mangaer.netlify.app

---

## How to Run Locally

### Backend

1. Open terminal
2. Run:

```bash
uvicorn backend.main:app --reload
