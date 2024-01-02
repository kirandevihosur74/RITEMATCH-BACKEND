# Job Matching Portal

Welcome to the **Job Matching Portal**! This Django project serves as a powerful backend for a job portal, providing Rest APIs for user authentication, job retrieval, and job scoring. The project leverages natural language processing (NLP) cosine similarity to match user skills with given job descriptions and provides a score for all the jobs available on the portal.

## Project Description

The *Job Matching Portal* is designed to streamline the job search process by intelligently matching user skills with job requirements. The use of NLP cosine similarity ensures a sophisticated approach to job matching, enhancing the overall user experience.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/job-matching-portal.git
    cd job-matching-portal
    ```

2. **Create Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate Virtual Environment:**

    - *On Windows:*
      ```bash
      venv\Scripts\activate
      ```
    - *On Linux/macOS:*
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the Server:**

    ```bash
    python manage.py runserver
    ```

Now, you can access the Job Matching Portal at [http://localhost:8000/](http://localhost:8000/) in your web browser.

## Usage

- **User Authentication API:**
  - **Endpoint:** `/api/auth/`
  - **Description:** Handles user authentication, allowing users to register, log in, and log out.

- **Job Retrieval API:**
  - **Endpoint:** `/api/jobs/`
  - **Description:** Retrieves available jobs from the portal.

- **Job Score API:**
  - **Endpoint:** `/api/job-score/`
  - **Description:** Uses NLP cosine similarity to match user skills with job descriptions and provides a score for each job.

Feel free to explore the APIs and integrate them into your frontend application!

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

---
