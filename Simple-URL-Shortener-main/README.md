# Simple URL Shortener

This is a simple URL Shortener built with Flask, SQLite, and Docker. The application takes a long URL and returns a shortened version, stores the mappings in a SQLite database, and redirects users when they visit the shortened URL.

## Features

- Input a long URL and generate a shortened version.
- Store the mappings of shortened URLs to the original in a simple SQLite database.
- Redirect shortened URLs to their original URLs.
- Containerize the application using Docker for easier sharing and deployment.

## Tech Stack

- **Flask**: A lightweight web framework for Python.
- **SQLite**: A lightweight database to store URL mappings.
- **Docker**: Containerization for easier deployment.

## Installation

### Prerequisites

- Python 3.12
- SQLite
- Postman 

### Local Setup

1. Clone the repository:
   ```bash
      git clone https://github.com/AkankshMadhur/url-shortener.git
   cd url-shortener
