# URL Shortener using Django restframework

This is a solution to the URL shortener project on roadmap.sh : https://roadmap.sh/projects/url-shortening-service


This project is a lightweight URL shortening service built using Django, Django REST Framework, and PostgreSQL. It provides a RESTful API for creating and managing shortened URLs, along with tracking access statistics.

## Key Features
- **URL Shortening:** Create a compact, unique short code for any given URL.
- **Redirection Support:** Retrieve and redirect to the original URL using the short code.
- **URL Management:** Update or deactivate existing shortened URLs.
- **URL Deletion:** Remove URL mappings when no longer needed.
- **Usage Analytics:** Monitor how often each shortened URL is accessed along with last accessed time.


---

## 🚀 Setup & Installation

### ✅ Prerequisites

- Python 3.8+
- [`uv`](https://github.com/astral-sh/uv)
- Docker & Docker Compose

---

### 📦 1. Clone the Repository

```bash
git clone https://github.com/sudocodedev/url_shortner.git
cd url-shortener
```

### 🔒 2. Set Up Environment Variables
Create a .env file in the root directory and configure it as follows:

```env
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_DB=
DATABASE_PORT=
DATABASE_HOST=
VOLUME_PATH=
```

### 📦 3. Install Dependencies

```bash
uv sync
```

✨ And vola you are done with the setup!!


### 🐳 4. Start PostgreSQL via Docker Compose

```bash
docker compose up -d
```

### ⚙️ 5. Apply Migrations

```bash
uv run manage.py migrate
```


### 🔢 6. Initialize Counter Sequence (One-Time Setup)

To enable your counter system, run the custom management command that creates the PostgreSQL sequence:

```bash
python manage.py init_counter
```

This command creates a sequence named url_shortner starting at 1000000000, if it doesn't already exist.


### ▶️ 7. Start the Development Server

```bash
python manage.py runserver
```
Visit: http://localhost:8000


### 📁 8. API Docs
Visit:
- http://localhost:8000/api/docs/swagger/
- http://localhost:8000/api/docs/redoc/
