# 🚀 Job Hunter

**Job Hunter** is a cross-platform desktop application designed to monitor job offers, automatically detect new opportunities, filter them according to a user's profile, and notify the user as quickly as possible.

The goal is to reduce the time between the publication of a job offer and the user's application.

## ✨ Features

### Current

- 🐍 Python-based application
- 🗃️ Local SQLite database
- 🧱 SQLAlchemy ORM
- 🔎 Job offer persistence and retrieval
- ♻️ Duplicate offer detection
- 🧪 Automated tests with pytest
- 🧹 Code quality with Ruff

### Planned

- 🌐 Job offer collectors
- ⏱️ Automatic monitoring and scheduling
- 🎯 Profile-based job matching
- 🔔 Desktop notifications
- 🖥️ PySide6 desktop interface
- 📌 System tray integration
- ⚙️ Application settings
- 📦 Cross-platform packaging
- 🤖 AI-assisted job matching
- 📄 CV and cover-letter assistance

## 🛠️ Tech Stack

| Technology        | Purpose                  |
| ----------------- | ------------------------ |
| Python 3.12+      | Application language     |
| PySide6           | Desktop user interface   |
| SQLAlchemy        | Database ORM             |
| SQLite            | Local database           |
| HTTPX             | HTTP requests            |
| BeautifulSoup     | HTML parsing             |
| Pydantic Settings | Configuration            |
| pytest            | Testing                  |
| Ruff              | Linting and code quality |
| PyInstaller       | Application packaging    |

## 🏗️ Architecture

The application is designed around a modular architecture so that collectors, business logic, database access, notifications, and the user interface remain independent.

```text
job-hunter/
│
├── app/
│   ├── config/          # Application configuration
│   ├── collectors/      # Job offer collectors
│   ├── models/          # Database models
│   ├── repositories/    # Database access
│   ├── services/        # Business logic
│   ├── notifications/   # Desktop notifications
│   ├── system/          # OS-specific functionality
│   └── ui/              # PySide6 interface
│
├── tests/               # Automated tests
│
├── .gitignore
├── pyproject.toml
├── README.md
└── job_hunter.db        # Local database (not committed)
```

### Application flow

```text
┌──────────────┐
│   Collector  │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│  JobOfferService │
└──────┬───────────┘
       │
       ▼
┌──────────────────────┐
│ JobOfferRepository   │
└──────┬───────────────┘
       │
       ▼
┌──────────────────┐
│      SQLite      │
└──────────────────┘
```

Additional components such as matching, notifications, scheduling, and the desktop interface will consume the service layer without directly depending on the database implementation.

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Python 3.12 or newer
- Git
- pip

### Clone the repository

```bash
git clone <repository-url>
cd job-hunter
```

### Create a virtual environment

#### Windows — PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents script execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -e ".[dev]"
```

### Initialize the database

```bash
python -m app.init_db
```

### Run the application

```bash
python -m app
```

## 🧪 Testing

Run the complete test suite:

```bash
pytest
```

Run Ruff:

```bash
ruff check .
```

You can also automatically fix supported Ruff issues:

```bash
ruff check . --fix
```

## 📦 Project Development

The project is being developed incrementally.

### Roadmap

- [x] Initialize Python project
- [x] Set up project architecture
- [x] Configure SQLite
- [x] Create SQLAlchemy models
- [x] Create repository layer
- [ ] Create service layer
- [ ] Implement first job collector
- [ ] Implement duplicate detection
- [ ] Implement job monitoring scheduler
- [ ] Implement profile matching
- [ ] Implement desktop notifications
- [ ] Build PySide6 interface
- [ ] Add system tray support
- [ ] Add application settings
- [ ] Add comprehensive tests
- [ ] Package for Windows
- [ ] Package for macOS
- [ ] Package for Linux

## 🖥️ Cross-Platform

Job Hunter is designed to run on:

- 🪟 Windows
- 🍎 macOS
- 🐧 Linux

The application avoids OS-specific logic whenever possible. Platform-specific functionality is isolated inside the `system/` layer.

The final releases are intended to provide native executables for each supported platform.

## 🔐 Data & Privacy

Job Hunter is designed as a local-first application.

Job offers, configuration, and user data are intended to be stored locally whenever possible.

External services will only be used when required by a specific feature, such as retrieving job offers from external sources or using an AI service.

## 🤝 Development Principles

The project follows a few principles:

- **Keep the architecture modular**
- **Separate business logic from infrastructure**
- **Prefer simple solutions over premature complexity**
- **Write tests for business-critical behavior**
- **Keep the application cross-platform**
- **Avoid unnecessary external dependencies**
- **Make every component independently testable**

## 📄 License

This project is currently under development.

A license will be added before the first public release.
