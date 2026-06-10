# Django Employee CRUD Application with Fake Data Population

A robust, fully functional Employee Management System built using the Django framework. This application performs full CRUD (Create, Read, Update, Delete) operations and includes a custom population script using the `Faker` library to inject dummy records into the database instantly.

## ⚡ Features

- **Full CRUD Operations:** Seamlessly Create, Retrieve, Update, and Delete employee records.
- **Automated Data Seeding:** Includes a standalone database population script powered by `Faker` to seed the database with mass random employee records.
- **Django ORM:** Utilizes Django's powerful Object-Relational Mapper for safe and clean database queries.
- **Dynamic Routing:** URL routing configured with dynamic integer IDs for accurate update and delete actions.

---

## 🛠️ Project Architecture

The project consists of an application named `testapp` integrated into the main project `crudProject`.

- **Model:** `Employee` (Fields: ID, Employee Number, Name, Salary, City)
- **Views:** Handle standard HTTP requests, form validations, and redirects.
- **Population Script:** A utility script to seed fake employee profiles.

---

## 📦 Prerequisites & Installation

Follow these steps to get the development environment running locally:


## Install Dependencies
pip install django faker

## Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

## 🧪 Database Seeding (Populating Fake Data)
python populate.py

## 🏃 How to Run the Application
python manage.py runserver
