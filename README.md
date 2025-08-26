# Blog API (Django REST Framework)

This is a blog-style REST API built using **Django REST Framework** with JWT authentication.  
It supports user registration/login, creating & managing blog posts, comments, and likes.  
Admins can manage users and posts, while bloggers can create and manage their own posts.

---

## Features

- **User Authentication** (Sign up / Sign in using JWT)
- Role-based permissions: `Admin`, `Blogger`, `User`
- CRUD operations for:
  - Users (admin only)
  - Posts (admin & bloggers)
  - Comments (authenticated users)
  - Likes (authenticated users)
- Admin dashboard endpoints

---

## Tech Stack

- Python 3.12+
- Django 5.x
- Django REST Framework
- SimpleJWT for authentication

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/medatik/blogApi.git
cd alxApiBlog
```

### 2. Create and activate virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

*(Create `requirements.txt` using: `pip freeze > requirements.txt`)*

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (admin)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will run at:  
`http://127.0.0.1:8000/api/`

---

## API Endpoints

| Method | Endpoint                   | Description                               | Access                  |
|--------|----------------------------|-------------------------------------------|-------------------------|
| POST   | `/api/signup`             | Register new user                        | Public                  |
| POST   | `/api/signin`             | Obtain JWT token                         | Public                  |
| GET    | `/api/users`              | List all users                           | Admin only              |
| GET    | `/api/users/:id`          | Get a specific user                      | Admin only              |
| PUT    | `/api/users/:id`          | Edit or ban a user                       | Admin only              |
| DELETE | `/api/users/:id`          | Delete a user                            | Admin only              |
| GET    | `/api/posts`              | List all posts                           | Public                  |
| POST   | `/api/posts`              | Create a new post                        | Blogger/Admin           |
| GET    | `/api/posts/:id`          | Get post by ID                           | Public                  |
| PUT    | `/api/posts/:id`          | Edit/Publish/Unpublish post              | Admin or Creator        |
| DELETE | `/api/posts/:id`          | Delete a post                            | Admin or Creator        |
| GET    | `/api/admin/posts`        | List all published & unpublished posts   | Admin only              |
| GET    | `/api/admin/dashboard`    | View admin dashboard                     | Admin only              |

---

## Testing with Thunder Client / Postman

API Routes & Test JSON Examples
Authentication
POST : /api/auth/register/
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "strongpassword"
}
POST : /api/auth/login/
{
  "username": "john_doe",
  "password": "strongpassword"
}
Posts
GET : /api/posts/
{}
POST : /api/posts/
{
  "title": "First Post",
  "content": "This is the content of the first post.",
  "author": 1
}
GET : /api/posts/{id}/
{}
PUT : /api/posts/{id}/
{
  "title": "Updated Post Title",
  "content": "Updated content.",
  "author": 1
}
DELETE : /api/posts/{id}/
{}
Comments
GET : /api/posts/{post_id}/comments/
{}
POST : /api/posts/{post_id}/comments/
{
  "content": "This is a comment.",
  "author": 1
}
PUT : /api/comments/{id}/
{
  "content": "Updated comment content."
}
DELETE : /api/comments/{id}/
{}
Users
GET : /api/users/
{}
GET : /api/users/{id}/
{}
Testing

Use Thunder Client, Postman, or similar tools to send requests to the above endpoints with the provided JSON structures.
