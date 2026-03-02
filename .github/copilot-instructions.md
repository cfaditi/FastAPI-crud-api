# Copilot Instructions for FastAPI CRUD API

## Project Overview
This is a FastAPI-based REST API template for CRUD (Create, Read, Update, Delete) operations. The project uses Pydantic for data validation and Uvicorn as the ASGI server.

**Key Stack:**
- FastAPI 0.135.0 - Web framework
- Pydantic 2.12.5 - Data validation
- Uvicorn 0.41.0 - ASGI server
- Python virtual environment at `testenv/`

## Architecture Pattern
**Expected structure for CRUD endpoints:**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Define Pydantic models for request/response validation
class ItemCreate(BaseModel):
    name: str
    description: str = None

class Item(ItemCreate):
    id: int

# 2. Create CRUD endpoints following REST conventions
@app.post("/items", response_model=Item)
def create_item(item: ItemCreate):
    # Create logic
    pass

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    # Read logic
    pass

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate):
    # Update logic
    pass

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Delete logic
    pass
```

## Key Conventions

### Pydantic Models
- Define separate models for input (`*Create`) and output (full model with `id`)
- Use Pydantic's built-in validation (field constraints, types, custom validators)
- Example: `class UserCreate(BaseModel): email: str` then extend with `id` for response

### Endpoint Organization
- Group related endpoints by resource (e.g., `/users`, `/items`)
- Use appropriate HTTP methods: `POST` (create), `GET` (read), `PUT/PATCH` (update), `DELETE` (delete)
- Always specify `response_model` for automatic validation/documentation

### Type Hints
- Use full type hints on all functions and routes - Pydantic and FastAPI depend on them
- Import types from standard library: `from typing import List, Optional`

## Development Workflow

### Running the Server
```powershell
# Activate virtual environment
./testenv/Scripts/Activate.ps1

# Start development server (auto-reload enabled)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Testing
- API docs auto-generated at `http://localhost:8000/docs` (Swagger UI)
- ReDoc available at `http://localhost:8000/redoc`
- Test using curl, Postman, or the built-in Swagger UI

### Debugging
- FastAPI includes detailed error responses in development mode
- Use `response_model` validation errors to identify bad requests
- Pydantic validation errors are returned as 422 Unprocessable Entity

## Common Patterns

### Error Handling
Use FastAPI's HTTPException for proper error responses:
```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if not item_exists(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return get_item(item_id)
```

### Optional Fields
Define optional request fields clearly:
```python
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
```

## File Structure
- `main.py` - Application entry point; define all routes and models here or import from submodules as this grows
- `testenv/` - Python virtual environment (gitignored)
- `.github/copilot-instructions.md` - This file

## Dependency Management
Dependencies installed in the virtual environment via pip. Key packages are in `testenv/Lib/site-packages/`.

**When adding new endpoints/features:**
1. Always use Pydantic models for request/response bodies
2. Define models near the top of main.py or in separate `models.py` module as project grows
3. Use type hints and response_model for FastAPI automatic documentation
4. Test in Swagger UI at `/docs` before considering complete
