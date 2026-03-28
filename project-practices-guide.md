# Professional Project Practices Guide

A reference for building clean, well-documented, team-ready code — specifically for the CellTalksInv inventory management project.

---

## 1. Project Structure

Keep a clear separation of concerns. For a FastAPI + React project:

```
CellTalksInv/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app + lifespan
│   │   ├── config.py            # env loading, settings
│   │   ├── db.py                # pool creation, helper functions
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── products.py
│   │   │   ├── categories.py
│   │   │   └── transactions.py
│   │   ├── models/              # Pydantic schemas (request/response)
│   │   │   ├── __init__.py
│   │   │   ├── product.py
│   │   │   └── transaction.py
│   │   └── sql/                 # Raw SQL files (since no ORM)
│   │       ├── schema.sql       # CREATE TABLE statements
│   │       ├── seed.sql         # Test data
│   │       └── queries/
│   │           ├── products.sql
│   │           └── transactions.sql
│   ├── tests/
│   │   ├── test_products.py
│   │   └── test_transactions.py
│   ├── .env                     # Never committed
│   ├── .env.example             # Committed — shows required vars without values
│   └── requirements.txt
├── frontend/
│   └── ...
├── docs/
│   ├── API.md                   # Endpoint documentation
│   ├── SCHEMA.md                # Database schema explanation
│   └── SETUP.md                 # How to run locally
├── .gitignore
├── README.md
└── LICENSE
```

**Key rules:**
- One file per resource/domain in routes (not one giant main.py)
- SQL files separate from Python — easy to review, version, and test independently
- `.env.example` committed with empty values so others know what's needed
- `docs/` folder for anything beyond the README

---

## 2. Git Branching Strategy

Use a simple branching model (GitHub Flow):

```
main (always deployable)
 └── feature/add-product-routes
 └── feature/inventory-dashboard
 └── fix/transaction-total-calc
 └── chore/update-dependencies
```

**Branch naming convention:**
- `feature/short-description` — new functionality
- `fix/short-description` — bug fixes
- `chore/short-description` — refactors, dependency updates, docs
- `data/short-description` — data engineering/pipeline work

**Workflow:**
1. Create a branch from `main`: `git checkout -b feature/add-product-routes`
2. Make small, focused commits as you work
3. Push the branch: `git push origin feature/add-product-routes`
4. Open a pull request (even if it's just you — builds the habit)
5. Review your own PR diff before merging
6. Merge to `main`, delete the branch

**Rules:**
- Never commit directly to `main`
- Each branch should represent one logical piece of work
- Keep branches short-lived (days, not weeks)

---

## 3. Commit Messages

Follow the Conventional Commits format:

```
<type>: <short description in imperative mood>

<optional body explaining WHY, not WHAT>
```

**Types:**
- `feat:` — new feature
- `fix:` — bug fix
- `refactor:` — code change that doesn't add a feature or fix a bug
- `docs:` — documentation only
- `test:` — adding or updating tests
- `chore:` — tooling, dependencies, config
- `style:` — formatting, no logic change

**Examples:**

```
feat: add POST endpoint for creating products

Accepts name, sku, price, and category_id.
Validates SKU uniqueness before inserting.
```

```
fix: prevent duplicate transactions on rapid form submission

Added a debounce check using the transaction timestamp.
Previously, double-clicking submit created two entries.
```

```
refactor: extract database helpers into db.py

Moved pool management and query helpers out of main.py
to keep the entry point clean.
```

**Rules:**
- Subject line under 50 characters
- Imperative mood: "add" not "added" or "adds"
- Body explains WHY the change was made, not what (the diff shows what)
- One logical change per commit — don't mix a feature + a refactor

---

## 4. Code Comments

**Comment the WHY, not the WHAT.** The code already shows what it does.

```python
# BAD — restates the code
# Get user by id
user = await conn.fetchrow("SELECT * FROM users WHERE id = $1", user_id)

# GOOD — explains a non-obvious decision
# Using fetchrow instead of fetch because IDs are unique,
# and we want to fail explicitly if somehow there are duplicates
user = await conn.fetchrow("SELECT * FROM users WHERE id = $1", user_id)
```

**When to comment:**
- Business logic that isn't obvious from the code
- Workarounds with a reason: `# asyncpg requires int for port, .env gives string`
- SQL queries that do something complex
- "Why not the obvious approach" explanations

**When NOT to comment:**
- Self-explanatory code
- Every function (use clear naming instead)
- Commented-out code (delete it — git has the history)

**Docstrings for functions that others will call:**

```python
async def get_products_by_category(pool, category_id: int, limit: int = 50):
    """Fetch active products in a category, ordered by most recently added.

    Returns an empty list if the category doesn't exist.
    Defaults to 50 results to prevent accidental full-table scans.
    """
```

---

## 5. Documentation

### README.md (root level)

Every project needs this. Keep it practical:

```markdown
# CellTalksInv

Inventory management system for [CellTalks] built with FastAPI + PostgreSQL + React.

## Quick Start

1. Clone the repo
2. Copy `.env.example` to `.env` and fill in your database credentials
3. Run `pip install -r requirements.txt`
4. Create the database: `psql -f backend/app/sql/schema.sql`
5. Start the server: `uvicorn app.main:app --reload`
6. Open http://localhost:8000/docs to see the API

## Project Structure

(brief overview)

## Tech Stack

- Backend: FastAPI, asyncpg, PostgreSQL
- Frontend: React
- Data: (whatever you add for the analytics layer)
```

### API.md

Document each endpoint. FastAPI generates Swagger docs automatically, but a written doc shows intentionality:

```markdown
## Products

### GET /products
Returns all active products. Supports pagination.

Query params:
- `page` (int, default 1)
- `limit` (int, default 20, max 100)
- `category_id` (int, optional) — filter by category

Response: `{ products: [...], total: int, page: int }`

### POST /products
Creates a new product. Requires auth.

Body: `{ name: str, sku: str, price: float, category_id: int }`
Returns: `201` with the created product
Errors: `409` if SKU already exists
```

### SCHEMA.md

Explain your database design decisions:

```markdown
## products
| Column      | Type         | Notes                        |
|-------------|--------------|------------------------------|
| id          | SERIAL PK    |                              |
| name        | VARCHAR(255) | NOT NULL                     |
| sku         | VARCHAR(50)  | UNIQUE, NOT NULL             |
| price       | DECIMAL(10,2)| NOT NULL, CHECK (price >= 0) |
| category_id | INT FK       | References categories.id     |
| created_at  | TIMESTAMPTZ  | DEFAULT NOW()                |
| is_active   | BOOLEAN      | DEFAULT TRUE (soft delete)   |

**Why soft delete?** Transactions reference products by ID.
Hard deleting a product would break transaction history.
```

---

## 6. Code Quality Habits

### Use .env.example

```env
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=
```

### Use a consistent .gitignore

```
# Python
__pycache__/
*.pyc
.env
venv/

# Node
node_modules/
.env.local

# IDE
.vscode/
.idea/

# OS
.DS_Store
```

### Use Pydantic models for request/response validation

```python
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    sku: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., ge=0)
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    price: float
    category_id: int
    is_active: bool
```

### Use HTTP status codes correctly

```python
from fastapi import HTTPException

@app.post("/products", status_code=201)
async def create_product(product: ProductCreate):
    # check for duplicate SKU
    existing = await conn.fetchrow("SELECT id FROM products WHERE sku = $1", product.sku)
    if existing:
        raise HTTPException(status_code=409, detail="SKU already exists")
    # ...create it
```

---

## 7. Development Workflow Checklist

For each feature you build, follow this order:

- [ ] Create a feature branch
- [ ] Write/update the SQL schema if needed
- [ ] Build the route(s) with Pydantic models
- [ ] Test with FastAPI /docs (Swagger UI)
- [ ] Add comments for non-obvious logic
- [ ] Update API.md if you added/changed endpoints
- [ ] Commit with a clear message
- [ ] Review your own diff before merging
- [ ] Merge to main

---

## 8. Preparing for IBM

These habits directly map to what you'll encounter on a real team:

| This project               | At IBM                            |
|----------------------------|-----------------------------------|
| Feature branches + PRs     | Required workflow for all code     |
| Conventional commits       | Makes code review easier           |
| .env.example               | Onboarding new devs quickly        |
| Pydantic validation        | API contracts between services     |
| SQL in separate files      | Database migration patterns        |
| docs/ folder               | Internal wikis and runbooks        |
| .gitignore done right      | Security — no leaked credentials   |
| Small focused commits      | Easy reverts, clean blame history  |

The goal isn't perfection — it's consistency. Pick these patterns, stick with them from commit one, and by the time you start at IBM you won't have to think about them.
