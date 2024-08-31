# Project Documentation: Instagram Follower Analysis

## Disclaimer

This project is intended for educational purposes only. It demonstrates techniques for processing and analyzing HTML data using Python and Flask. The code in this project should not be used to scrape or analyze data from websites without proper authorization. Always respect the terms of service and privacy policies of any website you interact with.

## Overview

This project is a web application that compares two lists of Instagram accounts: the accounts you follow (following) and the accounts that follow you (followers). The application identifies which accounts you follow but do not follow you back. It consists of a backend built with Flask and a frontend for uploading the necessary files and displaying the results.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Backend (`app.py`)](#backend-apppy)
   - [Dependencies](#dependencies)
   - [Functions](#functions)
   - [Routes](#routes)
3. [Frontend (`upload.html` and `result.html`)](#frontend-uploadhtml-and-resulthtml)
   - [Template Structure](#template-structure)
   - [Dynamic Content with JavaScript](#dynamic-content-with-javascript)
4. [Styles (Embedded CSS)](#styles-embedded-css)
5. [Usage](#usage)
   - [Setup](#setup)
   - [Run the Application](#run-the-application)
6. [Conclusion](#conclusion)
7. [Important Notes](#important-notes)

## Project Structure

Your project should be organized as follows:

```
/instagram-follower-analysis
├── app.py
├── /templates
│   ├── upload.html
│   └── result.html
└── /uploads
```

- `app.py`: The main Flask application script.
- `/templates`: Directory containing HTML templates for the web application.
- `/uploads`: Directory where uploaded files are temporarily stored.

## Backend (`app.py`)

### Dependencies

Make sure to install the following Python libraries:

- **Flask**: For building the web application.
- **BeautifulSoup** (`bs4`): For parsing HTML files.
- **os**: For file and directory management.
- **webbrowser**: To automatically open the web application in your browser.

You can install these dependencies using:

```bash
pip install flask beautifulsoup4
```

### Functions

- **`extract_users_from_html(file_path)`**:
  - **Purpose**: Extracts a list of usernames from an HTML file.
  - **Parameters**: `file_path` (str) - Path to the HTML file.
  - **Returns**: A set of usernames.
  - **Logic**: Opens the file, parses the HTML with BeautifulSoup, and extracts usernames from anchor (`<a>`) tags.

### Routes

- **`/`** (GET):
  - **Purpose**: Renders the file upload page.
  - **Template**: `upload.html`
  - **Description**: This route displays a form that allows users to upload their "followers" and "following" HTML files.

- **`/result`** (POST):
  - **Purpose**: Processes the uploaded files and displays the results.
  - **Template**: `result.html`
  - **Process**:
    - Saves the uploaded files to the `/uploads` directory.
    - Extracts usernames from the uploaded files.
    - Compares the lists and identifies users you follow but who do not follow you back.
    - Displays the results in a formatted list.

## Frontend (`upload.html` and `result.html`)

### Template Structure

- **`upload.html`**:
  - **Purpose**: Allows users to upload the "followers" and "following" files.
  - **Content**:
    - A form with a file input that supports uploading directories.
    - A submit button to process the uploaded files.

- **`result.html`**:
  - **Purpose**: Displays the list of accounts you follow but do not follow you back.
  - **Content**:
    - A heading indicating the purpose of the page.
    - The total count of accounts not following back.
    - Two columns listing the usernames, each linked to the corresponding Instagram profile.

### Dynamic Content with JavaScript

- **JavaScript Functions**:
  - **Drag-and-Drop Support**: Allows users to drag and drop files into the upload area.
  - **Upload Success Message**: Shows a message after files are successfully uploaded.

## Styles (Embedded CSS)

The CSS is embedded directly within the HTML files to style the user interface. The styles provide:

- A clean, centered upload area with dashed borders and hover effects.
- A structured result display with two columns of usernames.

## Usage

### Setup

1. **Install Python and Dependencies**:
   Ensure Python is installed on your system. Install required dependencies:

   ```bash
   pip install flask beautifulsoup4
   ```

2. **Directory Structure**:
   - Ensure that your project directory matches the structure outlined in the [Project Structure](#project-structure) section.

### Run the Application

1. **Start the Flask Server**:
   Run the `app.py` script to start the web application:

   ```bash
   python app.py
   ```

2. **Access the Application**:
   - The application should automatically open in your default browser at `http://127.0.0.1:5000`.
   - If not, manually open the link in your browser.

## Conclusion

This project offers a simple and intuitive tool for comparing Instagram follower lists. It helps you manage your social media presence by identifying accounts you follow that do not reciprocate. The combination of Python and Flask makes it easy to extend and customize this tool further.

## Important Notes

- **Data Privacy**: Use this tool responsibly and ensure it is only used for personal data analysis. Do not use it to analyze data you do not have the right to access.
- **Terms of Service Compliance**: Always adhere to the terms of service of the platforms from which you collect data.
