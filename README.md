# Inventory Reservation & Dispatch System

## Overview

Inventory Reservation & Dispatch System is a FastAPI-based backend microservice responsible for managing products, inventory batches, inventory reservations, and dispatch operations.

The service integrates with the Authentication Service for JWT authentication and permission-based authorization, and with the Sales Transaction Service through event-driven inventory reservation.

The project demonstrates backend service development using FastAPI, PostgreSQL, SQLAlchemy, Celery, Redis, and REST APIs.

---

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Celery
- Redis
- JWT Authentication
- Permission-Based Authorization (RBAC)
- Swagger UI
- Faker

---

## System Architecture

```text
                    Authentication Service
                            │
                     JWT Authentication
                            │
                            ▼
        Inventory Reservation & Dispatch System
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
          ▼                                   ▼
   Product & Inventory APIs         Reservation Event Handler
          │                                   │
          ▼                                   ▼
     PostgreSQL Database          Celery Background Tasks
```

---

## Reservation Workflow

```text
TRANSACTION_CREATED Event
            │
            ▼
Validate Event Payload
            │
            ▼
Find FIFO Inventory Batch
            │
            ▼
Reserve Inventory
            │
            ▼
Create Reservation
            │
            ▼
Store Transaction Mapping
            │
            ▼
Return Reservation Status
```

---

## Dispatch Workflow

```text
Reserved Inventory
        │
        ▼
Dispatch Request
        │
        ▼
Validate Reservation
        │
        ▼
Create Dispatch
        │
        ▼
Mark Reservation Complete
```

---

## Features

### Product Management

- Create products
- View products
- Product catalog API

### Inventory Management

- Create inventory batches
- View inventory
- FIFO inventory selection
- Inventory validation

### Reservation Management

- Manual reservation
- Event-driven reservation
- Reservation lookup by transaction ID
- Reservation expiration
- Duplicate event protection

### Dispatch Management

- Dispatch reserved inventory
- Dispatch tracking

### Security

- JWT Authentication
- Permission-based Authorization
- Protected endpoints

### Background Processing

- Celery worker
- Celery Beat
- Automatic reservation expiration

### Integration

- Sales Transaction Service integration
- Event-driven reservation processing

### Documentation

- Interactive Swagger UI

---

## Project Structure

```text
inventory_dispatch_system/

├── app
│   ├── api
│   │   ├── dispatch_routes.py
│   │   ├── event_routes.py
│   │   ├── inventory_routes.py
│   │   ├── product_routes.py
│   │   └── reservation_routes.py
│   │
│   ├── core
│   │   ├── config.py
│   │   └── logger.py
│   │
│   ├── database
│   │   ├── connection.py
│   │   ├── create_tables.py
│   │   └── seed_data.py
│   │
│   ├── events
│   │   ├── __init__.py
│   │   └── reservation_event_handler.py
│   │
│   ├── middleware
│   │   └── auth_middleware.py
│   │
│   ├── models
│   │   ├── __init__.py
│   │   ├── dispatch.py
│   │   ├── inventory_batch.py
│   │   ├── processed_transaction.py
│   │   ├── product.py
│   │   └── reservation.py
│   │
│   ├── operations
│   │   └── inventory_ops.py
│   │
│   ├── schemas
│   │   ├── dispatch_schema.py
│   │   ├── event_schema.py
│   │   ├── inventory_schema.py
│   │   ├── product_schema.py
│   │   └── reservation_schema.py
│   │
│   ├── services
│   │   ├── jwt_service.py
│   │   ├── permission_checker.py
│   │   └── rbac_service.py
│   │
│   ├── workers
│   │   ├── __init__.py
│   │   ├── celery_app.py
│   │   └── reservation_tasks.py
│   │
│   └── main.py
│
├── tests
│   ├── relationship_validation.py
│   ├── rollback_validation.py
│   ├── schema_validation.py
│   └── simulate_transaction_event.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## API Endpoints

### System

| Method | Endpoint | Description          |
| ------ | -------- | -------------------- |
| GET    | /health  | Service health check |

### Products

| Method | Endpoint  | Description    |
| ------ | --------- | -------------- |
| POST   | /products | Create product |
| GET    | /products | View products  |

### Inventory

| Method | Endpoint   | Description            |
| ------ | ---------- | ---------------------- |
| POST   | /inventory | Create inventory batch |
| GET    | /inventory | View inventory batches |

### Reservations

| Method | Endpoint                                   | Description        |
| ------ | ------------------------------------------ | ------------------ |
| POST   | /reservations                              | Create reservation |
| GET    | /reservations                              | View reservations  |
| GET    | /reservations/transaction/{transaction_id} | Reservation lookup |

### Dispatch

| Method | Endpoint  | Description        |
| ------ | --------- | ------------------ |
| POST   | /dispatch | Dispatch inventory |
| GET    | /dispatch | View dispatches    |

### Events

| Method | Endpoint                    | Description               |
| ------ | --------------------------- | ------------------------- |
| POST   | /events/transaction-created | Process transaction event |

---

## Example Transaction Event

```json
{
  "transaction_id": 1,
  "invoice_number": "INV-2026-000001",
  "product_id": 1,
  "quantity": 5
}
```

---

## Example Reservation Response

```json
{
  "transaction_id": 1,
  "reservation_id": 12,
  "status": "RESERVED"
}
```

---

## Security Model

Protected endpoints require:

- Valid JWT access token
- Permission-based authorization

Example permissions:

- view_products
- view_inventory
- reserve_inventory
- view_reservations
- dispatch_inventory
- view_dispatches
- process_events

---

## Configuration

Configuration is managed through environment variables.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/inventory_db

SECRET_KEY=your-secret-key

ALGORITHM=HS256

RESERVATION_TIMEOUT_MINUTES=1
```

Copy `.env.example` to `.env` before running the application.

---

## Running the Project

### Clone Repository

```bash
git clone <https://github.com/Abhiram-TK/inventory_dispatch_system>
```

### Navigate into Project

```bash
cd inventory_dispatch_system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Copy:

```text
.env.example
```

to

```text
.env
```

Update the values for your local environment.

### Seed Development Data

```bash
python -m app.database.seed_data
```

### Start API

```bash
uvicorn app.main:app --reload --port 8002
```

### Start Celery Worker

```bash
celery -A app.workers.celery_app worker --pool=solo --loglevel=info
```

### Start Celery Beat

```bash
celery -A app.workers.celery_app beat --loglevel=info
```

---

## Swagger UI

```text
http://127.0.0.1:8002/docs
```

Swagger provides:

- Interactive endpoint testing
- Request validation
- Response schemas
- JWT authentication support

---

## Related Projects

This service is designed to work with:

- Authentication Service
- Sales Transaction Service

Together these services demonstrate a simple event-driven backend architecture using multiple FastAPI services.

---

## Current Status

Implemented

- Product management
- Inventory batch management
- FIFO inventory reservation
- Dispatch management
- Event-driven reservation processing
- Reservation lookup by transaction ID
- JWT authentication
- Permission-based authorization
- Celery worker
- Celery Beat
- Automatic reservation expiration
- Swagger documentation

Next Phase

- Docker containerization
- Docker Compose deployment
