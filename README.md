# fastapi-hardcoded-items

A simple FastAPI project that demonstrates how to build a REST API with hardcoded JSON data.  
This example serves a small list of items (`Apple`, `Banana`, `Mango`) and provides endpoints to retrieve all items or a single item by ID.

---

## 🚀 Features
- Built with **FastAPI**
- Hardcoded JSON data (no database required)
- Endpoints for listing all items and retrieving items by ID
- Interactive API documentation at `/docs`

---

## 📂 Project Structure
fastapi-hardcoded-items/
│── app.py # Main FastAPI application
│── requirements.txt # Dependencies
│── README.md # Project documentation

## 🛠️ Installation & Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/fastapi-hardcoded-items.git
cd fastapi-hardcoded-items
```

### 2. Create virtual environment (optional but recommended)
python -m venv venv
# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the server
uvicorn app:app --host 0.0.0.0 --port 5000 --reload
