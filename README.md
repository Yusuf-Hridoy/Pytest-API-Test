# 🏨 Restful Booker API Automation

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-7.x-yellow?style=for-the-badge&logo=pytest&logoColor=white)
![Build Status](https://img.shields.io/badge/Build-Passing-green?style=for-the-badge)

A robust API automation framework built with **Python** and **Pytest** to test the booking functionalities of the [Restful Booker](https://restful-booker.herokuapp.com/apidoc/index.html) API.

---

## 🚀 Technologies Used

*   **[Python](https://www.python.org/)**: Core programming language.
*   **[Pytest](https://docs.pytest.org/en/7.1.x/)**: Testing framework for executing test cases and assertions.
*   **[Requests](https://requests.readthedocs.io/en/latest/)**: Simple HTTP library for making API calls.
*   **[JSONPath](https://pypi.org/project/jsonpath/)**: Tool to extract data from JSON responses.
*   **[Pytest-HTML](https://pypi.org/project/pytest-html/)**: Plugin for generating HTML test reports.

## 📂 Project Structure

```
Pytest-API-Test/
├── test/                   # Contains all test cases
│   ├── test_createuser.py  # Tests for creating bookings
│   ├── test_deletebooking.py # Tests for deleting bookings
│   └── test_getuser.py     # Tests for retrieving booking details
├── report/                 # Generated HTML test reports
├── Get.py, Post.py...      # Utility scripts for HTTP methods
└── requrment.txt           # Project dependencies
```

## 🧪 What It Does

This framework automates the verification of the following API endpoints:
*   **Create Booking (POST)**: Verifies that a new booking can be successfully created with valid data.
*   **Get Booking (GET)**: Fetches booking details and validates the response.
*   **Delete Booking (DELETE)**: Ensures bookings can be removed from the system.
*   *(Planned)* **Update Booking (PUT/PATCH)**: To modify existing booking details.

## 🛠️ Getting Started

### Prerequisites
*   Python 3.x installed
*   Git installed

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Yusuf-Hridoy/Pytest-API-Test.git
    cd Pytest-API-Test
    ```

2.  Install dependencies:
    ```bash
    pip install -r requrment.txt
    ```
    *(Note: Ensure you have `pytest` and `pytest-html` installed)*

### Running Tests

Run all tests from the root directory:
```bash
python -m pytest test/
```

To generate an HTML report:
```bash
python -m pytest --html=report/report.html
```

## 🔮 Future Improvements (Roadmap)

To make this framework more modern, scalable, and professional, the following features are planned:

1.  **CI/CD Integration**: Connect with GitHub Actions or Jenkins to run tests automatically on every commit.
2.  **Environment Variables**: Use `.env` files to manage sensitive data like Base URLs and Auth Tokens securely, separating configuration from code.
3.  **Data-Driven Testing (DDT)**: Read test data from external CSV or JSON files to run the same test with multiple data sets.
4.  **Allure Reporting**: Replace basic HTML reports with [Allure](https://allurereport.org/) for rich, interactive, and detailed test visualization.
5.  **Logging**: Implement Python’s `logging` module to replace `print()` statements for better debugging and log management.
6.  **Dockerization**: Containerize the tests using Docker to ensure consistency across different environments.
7.  **Pre-commit Hooks**: Add tools like `flake8` or `black` to ensure code quality and formatting before pushing code.



---
*Created by [Yusuf Hridoy]*
