Little Lemon REST API - Back-end Developer Capstone

API paths to test in Insomnia REST client:

1. Home page serving static HTML content:
   GET /

2. User registration:
   POST /api/registration/
   Body JSON:
   {
     "username": "learner",
     "email": "learner@example.com",
     "password": "StrongPass123"
   }

3. Obtain authentication token:
   POST /api-token-auth/
   Body JSON:
   {
     "username": "learner",
     "password": "StrongPass123"
   }

4. Category API:
   GET /api/categories/
   POST /api/categories/
   Body JSON:
   {
     "slug": "mains",
     "title": "Mains"
   }

5. Menu item API:
   GET /api/menu-items/
   POST /api/menu-items/
   Body JSON:
   {
     "title": "Greek Salad",
     "price": "12.50",
     "featured": true,
     "category_id": 1
   }
   GET /api/menu-items/1/
   PUT /api/menu-items/1/
   DELETE /api/menu-items/1/

6. Table booking API:
   GET /api/bookings/
   POST /api/bookings/
   Body JSON:
   {
     "first_name": "Maryam",
     "reservation_date": "2026-05-02",
     "reservation_slot": 18
   }
   GET /api/bookings/1/
   PUT /api/bookings/1/
   DELETE /api/bookings/1/

7. Admin-only manager group assignment:
   POST /api/groups/manager/users/
   Body JSON:
   {
     "username": "learner"
   }

How to run:

1. Create a MySQL database named littlelemon.
2. Install packages:
   pip install -r requirements.txt
3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
4. Create admin user:
   python manage.py createsuperuser
5. Run server:
   python manage.py runserver
6. Run unit tests:
   python manage.py test

This project includes Django REST Framework APIs for menu items and table bookings, user registration and token authentication, MySQL database settings, unit tests, and a Readme.txt file with API paths for reviewers.
