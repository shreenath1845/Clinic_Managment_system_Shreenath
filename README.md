# Clinic Management System

## Overview
The Clinic Management System is a web-based application built to simplify and digitize the operations of a clinic. It supports two primary users: **Receptionist** and **Doctor**. The system facilitates tasks like patient token management, prescription handling, and billing, while maintaining a complete patient history.

## Features

- **Receptionist Dashboard**
  - Login authentication
  - Generate and assign tokens to patients
  - Add patient details
  - View billing history
  - View doctor feedback

- **Doctor Dashboard**
  - Login authentication
  - View patient queue
  - Add prescriptions
  - View patient history

- **Patient Management**
  - Token generation for new patients
  - Personal data storage (name, age, gender, contact)
  - Prescription and visit history tracking

- **Billing**
  - Bill generation based on doctor’s input and receptionist's entries

- **Security**
  - User authentication for both roles
  - Access control based on role

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Django (Python)
- **Database:** MySQL, Sqlite3
- **Tools:** Atom, GitHub

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/clinic-management-system.git
   cd clinic-management-system
 done by @ Shreenath Naik A

## Deployment Strategy – Local Setup

 git clone https://github.com/your-username/clinic-management-system.git
 cd clinic-management-system
 python -m venv venv
 source venv/bin/activate       # Linux/Mac
 venv\Scripts\activate          # Windows
 pip install -r requirements.txt
 Create a new database (e.g., clinic_db)
 Add the database name, user, and password to settings.py:
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser
 python manage.py runserver
