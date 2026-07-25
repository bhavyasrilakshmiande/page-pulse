# Page Pulse

A lightweight web application that audits any webpage URL and provides useful SEO and webpage metrics.

---

# Project Overview

Page Pulse is a Flask-based web application that accepts a webpage URL, fetches the page, analyzes its HTML content, and returns a detailed report. The tool measures page performance and extracts important SEO-related information such as page title, meta description, H1 tags, images without alt text, and approximate visible word count.

The application includes proper validation, error handling, and a clean user interface to make the audit process simple and user-friendly.

---

# Features

- Audit any valid HTTP or HTTPS URL
- Display HTTP Status Code
- Measure Response Time
- Extract Page Title
- Extract Meta Description
- Count H1 Tags
- Count Images Missing Alt Attributes
- Calculate Approximate Visible Word Count
- Copy JSON Response
- Clear Results
- Responsive User Interface
- Handles Invalid URLs
- Handles Timeouts
- Handles Non-HTML Responses
- Displays Friendly Error Messages

---

# Tech Stack

- Python
- Flask
- Requests
- BeautifulSoup4
- HTML
- CSS
- JavaScript

---

# Installation

Clone the repository.

```bash
git clone https://github.com/bhavyasrilakshmiande/page-pulse.git
cd page-pulse
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# API Contract

## Endpoint

```
POST /audit
```

### Request

```json
{
  "url": "https://example.com"
}
```

### Successful Response

```json
{
  "success": true,
  "http_status": 200,
  "response_time": 0.58,
  "page_title": "Example Domain",
  "meta_description": "",
  "h1_count": 1,
  "images_missing_alt": 0,
  "word_count": 18
}
```

### Error Response

```json
{
  "success": false,
  "error": "Invalid URL"
}
```

---

# Folder Structure

```
page-pulse/
│
├── app.py
├── utils.py
├── requirements.txt
├── Procfile
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── tests/
    └── test_utils.py
```

---

# Design Decisions

### 1. Flask Backend

Flask was selected because it is lightweight, easy to understand, and well suited for building REST APIs for small web applications.

### 2. BeautifulSoup for HTML Parsing

BeautifulSoup provides a simple and reliable way to extract webpage information such as the page title, meta description, headings, images, and visible text.

### 3. Robust Error Handling

The application validates URLs and gracefully handles invalid URLs, request failures, timeouts, and unsupported content types. This ensures the application never crashes and always returns meaningful error messages.

---

# AI Usage

ChatGPT and GitHub Copilot were used during development to understand Flask concepts, improve the project structure, generate initial code suggestions, and review implementation ideas. All generated code was manually reviewed, tested, debugged, and modified before the final submission.

---

# Testing

The project includes automated unit tests for the HTML parsing logic.

The tests cover:

- Happy path
- Invalid HTML input
- Empty HTML input

Run the tests using:

```bash
python -m unittest discover tests
```

---

# Future Improvements

- Support additional SEO metrics
- Generate downloadable audit reports
- Add performance charts
- Maintain audit history
- Support asynchronous page analysis

---

# Live Demo

https://page-pulse-30dg.onrender.com
Live URL:

```
(Add your Render deployment link here)
```

Loom Walkthrough:

```
(Add your Loom video link here)
```

---

## Footer Requirement

Built for Digital Heroes Training Task

https://digitalheroesco.com
