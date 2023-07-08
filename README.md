# lco_tubers

## Description

This repository contains the project files for the lco_tubers project, which is part of the FullStack Django Developer course on Learn Code Online. The course provides a comprehensive guide to building a Django backend for web applications, covering various topics such as models, views, templates, forms, authentication, and more.

## Course Information

Course Title: FullStack Django Developer - Freelance Ready
Course URL: [https://courses.learncodeonline.in/learn/FullStack-Django-Developer-Freelance-ready](https://courses.learncodeonline.in/learn/FullStack-Django-Developer-Freelance-ready)

## Copyright Notice

This project includes images and names of YouTubers, as well as direct links to their YouTube videos. It is important to acknowledge the copyright of the rightful owners for the content used in this project.

The usage of YouTubers' images and names is solely for educational purposes within the context of this course project. The inclusion of these elements does not imply any endorsement, sponsorship, or affiliation with the YouTubers.

All copyrighted content, including images, names, and YouTube videos, belongs to their respective owners. Please note that the actual data for the YouTubers might not be available in the project due to changes in the database migrations and structure. However, the media files (images, video links, etc.) related to the YouTubers can still be found within the project files.

If you intend to use this project for any purpose other than educational, please ensure you have obtained the necessary permissions and adhere to the copyright guidelines set by the respective owners.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/Gaganraj2002/lco_tubers_django.git
   ```

2. Navigate to the project directory:
   ```
   cd lco_tubers_django
   ```

3. Install and configure PostgreSQL:
   - Install PostgreSQL: Follow the instructions provided in the PostgreSQL documentation for your specific operating system. You can find the documentation [here](https://www.postgresql.org/docs/).
   - Once installed, create a new database by opening a terminal or command prompt and running the following commands:
     ```
     psql
     CREATE DATABASE lco_tubers;
     ```

4. Install `pipenv` and update dependencies:
   - If you don't have `pipenv` installed, you can install it using `pip`:
     ```
     pip install pipenv
     ```
   - Navigate to the project directory and run the following command to install/update the project dependencies:
     ```
     pipenv update
     ```

5. Update the database settings:
   - Open the `settings.py` file located in the `lco_tubers` directory.
   - Modify the database configuration according to your PostgreSQL setup. Update the following settings:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'lco_tubers',
             'USER': 'your-postgres-username',
             'PASSWORD': 'your-postgres-password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

6. Apply the database migrations:
   - Run the following command to generate the necessary database migrations:
     ```
     pipenv run python manage.py makemigrations
     ```
   - Apply the migrations to create the database schema:
     ```
     pipenv run python manage.py migrate
     ```

7. Start the Django development server:
   ```
   pipenv run python manage.py runserver
   ```

8. Open your web browser and visit: `http://localhost:8000`

If you encounter any issues or have any questions, please feel free to ask for further assistance.

## Contribution

Contributions to this project are welcome. If you encounter any issues or would like to suggest improvements, please feel free to open an issue or submit a pull request. Your feedback and contributions are greatly appreciated.
