# Inventory Reservation & Dispatch System

Transaction-safe backend inventory reservation and dispatch simulation system built using PostgreSQL and SQLAlchemy ORM.

---

# Project Overview

This project simulates a backend inventory reservation engine capable of:

- tracking inventory batches
- reserving stock transactionally
- validating inventory consistency
- protecting against over-reservation
- maintaing relational integrity
- generating synthetic datasets for scaled validation

---

# Current Features

## ORM models

Implemented relational models:

- Product
- InventoryBatch
- Reservation
- Dispatch

---

## Database Relationships

| Relationship                 | Type        |
| ---------------------------- | ----------- |
| Product → InventoryBatch     | One-to-Many |
| InventoryBatch → Reservation | One-to-Many |
| Reservation → Dispatch       | One-to-One  |

---

## Transactional Reservation Workflow

Implemented reservation workflow:

Find Inventory Batch
→ Validate Quantity
→ Reduce Available Inventory
→ Create Reservation
→ Commit Transaction

Features:

- rollback protection
- inventory consistency validation
- over-reservation prevention

---

## Database Constraints

Implemented:

- Foreign Key constraints
- CHECK constraints
- UNIQUE constraints
- NOT NULL constraints

Examples:

- positive product price
- non-negative inventory quantity
- unique SKU values
- unique batch numbers

---

# Faker Integration

Project uses Faker for synthetic dataset generation.

Generated datasets include:

- products
- inventory batches
- reservations

Purpose:

- simulate scaled inventory activity
- validate schema stability
- expose integrity issues
- test transactional consistency

---

# Scaled Validation

Project validates backend behavior under repeated synthetic workload.

Validation includes:

- repeated product creation
- repeated inventory batch generation
- repeated reservation workflows
- transaction rollback testing
- relationship integrity verification

---

# Rollback Protection

System validates transactional rollback behavior.

Example scenario:

Available Inventory:
5

Attempted Reservation:
50

Expected Result:

- reservation fails safely
- inventory remains unchanged
- no negative inventory created

This prevents transactional corruption.

---

# Schema Stability Validation

Repeated validation cycles test:

- ORM relationship stability
- foreign key integrity
- uniqueness enforcement
- transaction safety
- inventory consistency

Validation confirms:

- no negative inventory
- no broken relationships
- no schema corruption under repeated operations

---

# Event-Driven Reservation Workflow

This project now includes simulated event-driven inventory reservation processing.

Instead of manually triggering reservation operations directly, transaction events are emitted and processed through a dedicated event handling layer.

Workflow:

Transaction Created
→ Event Emitted
→ Reservation Event Handler
→ Inventory Reservation Processing
→ Success / Failure Logging

Example simulated event payload:

```json
{
  "transaction_id": 1,
  "invoice_number": "INV-5001",
  "product_id": 1,
  "quantity": 2
}
```

# Project Structure

```text
inventory_dispatch_system/
│
├── app/
│   ├── database/
│   │   ├── connection.py
│   │   ├── seed_data.py
│   │   ├── relationship_validation.py
│   │   ├── rollback_validation.py
│   │   └── schema_validation.py
│   │
|   ├── events/
|   |   ├── __init__.py
|   |   └── reservation_event_handler.py
|   |
│   ├── models/
│   │   ├── product.py
│   │   ├── inventory_batch.py
│   │   ├── reservation.py
│   │   └── dispatch.py
│   │
│   ├── operations/
│   │   └── inventory_ops.py
│   │
|   ├── simulate_transaction_event.py
|   |
│   └── main.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Technologies Used

| Technology     | Purpose                         |
| -------------- | ------------------------------- |
| Python         | Backend programming             |
| PostgreSQL     | Relational database             |
| SQLAlchemy ORM | Database ORM layer              |
| Faker          | Synthetic dataset generation    |
| psycopg2       | PostgreSQL driver               |
| python-dotenv  | Environment variable management |

---

# Setup Instruction

## 1. Clone Repository

```bash
git clone <https://github.com/Abhiram-TK/inventory_dispatch_system>
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows:

```bash
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environemnt Variables

Create '.env':

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/inventory_db
```

## 6. Create Database Tables

```bash
python -m app.main
```

---

# Synthetic Dataset Generation

Run:

```bash
python -m app.database.seed_data
```

This generates:

- fake products
- fake inventory batches
- fake reservations

---

# Relationship Validation

Run:

```bash
python -m app.database.relationship_validation
```

Validates:

- Product → Batches
- Batch → Reservations
- Reservation → Dispatch

---

# Rollback Validation

Run:

```bash
python -m app.database.rollback_validation
```

Validates:

- failed reservations rollback safely
- inventory remains consistent

---

# Schema Stability Validation

Run:

```bash
python -m app.database.schema_validation
```

Validates:

- repeated transactional workload
- inventory consistency
- relational integrity
- schema stability

## Current Project State

Completed:

- ORM architecture
- transactional reservation workflow
- rollback protection
- Faker-based synthetic scaling
- schema stability validation
- event-driven reservation workflow
- reservation event handling
- event logging workflow
- validation matrix testing

Not Yet Implemented:

- FastAPI APIs
- Redis Pub/Sub
- Celery workers
- Docker
- Authentication
- Deployment
- Automated API testing

These features will be added in future.

---

# Engineering Focus

This project emphasizes:

- transactional safety
- relational consistency
- scalable validation
- backend workflow reliability
- synthetic workload simulation

instead of frontend complexity.

---

# License

Educational backend engineering project.
