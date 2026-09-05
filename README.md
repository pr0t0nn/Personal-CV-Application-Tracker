# Proton's Personal CV Tracker
A python project tahts developed to keep track of Applications made. To never lose track of whats going on

## Features

- Add an application with a company name, application date, and CV file.
- Pick your CV from the file explorer (PDF, Word, or any file).
- Mark each application as **Passed** or **Failed** later on when the response comes.
- Every application is stored in a local SQLite database (`Applications.db`) which can be accessible from the VS Code Explorer.
- Your saved applications load automatically on startup of the program.

## Tech Stack

- **Python**
- **customtkinter**
- **sqlite3**

## Project Structure

```
Cv Tracker/
├── app.py              
├── backend.py          
├── Applications.db
└── README.md
```

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install the dependency:

   ```bash
   pip install customtkinter
   ```

## Running

```bash
python app.py
```

On first launch the app creates `Applications.db` automatically.

## Usage

1. Click **Add Application**.
2. Enter the company name and application date (today's date is filled in for you).
3. Click **Add CV** and select your CV file.
4. Click **Save Application** to store it.
5. Open a saved application from the list to mark it **Passed** or **Failed**.