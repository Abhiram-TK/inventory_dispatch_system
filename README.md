# Inventory Reservation System

## Project Overview

Transactional inventory reservation backend system built using:

- Python
- PostgreSQL
  -SQLAlchemy ORM

The system manages:

- products
- inventory batches
- inventory reservations
- dispacth tracking

Core focus:

- relational database design
- transactional consistency
- ORM relationships
- rollback safety
- inventory integrity

---

## Features

- Product management
- inventory batch tracking
- Reservation workflow
- Transaction-safe inventory deduction
- Rollback protection
- Database constraints
- Foreign key relationships

---

## Database Schema

### Product

Stores product details.

### InventoryBatch

Represnts inventory stock batches.

### Reservation

Tracks reserved inventory quantities.

### Dispatch

Tracks shipment/disptach records.

---

## Technologies Used

- Pytthon
- PostgreSQL
- SQLAlchemy
- psycopg2
- python-dotenv

---

## Setup Instruction

### Clone Repository

```bash
git clone <>
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environemnt Variables

Create '.env':

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/inventory_db
```

### Run Project

```bash
python -m app.main
```

---

## Current Project Status

ORM layer completed.

Implemented:

- ORM models
- relationships
- constraints
- CRUD operations
- transactional reservation workflow
- rollback verification

In future, will add:

- FASTAPI APIs
- Redis caching
- Celery workers
- Docker
- load testing
- deployment
