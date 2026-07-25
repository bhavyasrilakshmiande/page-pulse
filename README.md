# Page Pulse

## Overview
Page Pulse is a web application designed to audit any webpage URL and provide useful SEO and page metrics. It features a clean and responsive interface that allows users to input a URL and receive a detailed report on various metrics, including HTTP status, response time, page title, meta description, H1 count, images missing alt attributes, and approximate word count.

## Features
- URL input for auditing any webpage.
- Detailed metrics report including:
  - HTTP Status Code
  - Response Time (in milliseconds)
  - Page Title
  - Meta Description
  - Number of H1 Tags
  - Number of Images Missing Alt Attributes
  - Approximate Visible Word Count
- Error handling for various failure scenarios.
- Responsive design for mobile and desktop users.
- Loading spinner during the audit process.
- Success and error notifications.
- Clear results and copy JSON response functionality.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd page-pulse
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Locally
To run the application locally, use the following command:
```
flask run
```
Make sure to set the `FLASK_APP` environment variable to `app.py`.

## API Documentation
### POST /audit
- **Request Body:**
  ```json
  {
      "url": "https://example.com"
  }
  ```

- **Response:**
  - On success:
    ```json
    {
        "success": true,
        "data": {
            "http_status": 200,
            "response_time": 120,
            "page_title": "Example Domain",
            "meta_description": "This domain is for use in illustrative examples in documents.",
            "h1_count": 1,
            "images_missing_alt": 0,
            "word_count": 50
        }
    }
    ```
  - On error:
    ```json
    {
        "success": false,
        "error": "Request timed out"
    }
    ```

## Deployment Instructions
To deploy the application on Render, ensure you have the following files in your project:

- `requirements.txt` for dependencies.
- `Procfile` specifying the command to run the application.

## Folder Structure
```
page-pulse
├── app.py
├── utils.py
├── requirements.txt
├── Procfile
├── README.md
├── templates
│   └── index.html
└── static
    ├── style.css
    └── script.js
```

## Technologies Used
- Python
- Flask
- BeautifulSoup4
- Requests
- HTML/CSS/JavaScript
- Deployment on Render

This README provides a comprehensive overview of the Page Pulse project, its features, and how to set it up and run it locally.