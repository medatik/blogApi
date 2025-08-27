# Blog API

A Django REST Framework based API for a blog application with JWT authentication.

## Features

- User authentication using JWT
- User roles (admin, blogger, user)
- CRUD operations for blog posts
- Comments system
- Like system

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication

1. Register a new user:
```http
POST /api/register/
Content-Type: application/json

{
    "username": "your_username",
    "email": "your_email@example.com",
    "password": "your_password"
}
```

2. Login (Get JWT token):
```http
POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

Success Response:
```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

3. Refresh Token:
```http
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "your_refresh_token"
}
```

4. Logout:
```http
POST /api/logout/
Authorization: Bearer your_access_token
```

Success Response:
```json
{
    "status": "success",
    "message": "Successfully logged out"
}
```

Note: After login, use the access token in the Authorization header for all protected endpoints:
```http
Authorization: Bearer your_access_token
```
  {
    "Authorization": "Bearer your_access_token",
    "Content-Type": "application/json"
  }
  // Request Body
  {
    "refresh_token": "your_refresh_token"
  }
  ```

### Users
- GET `/api/users/`: List users (admin only)
- POST `/api/users/`: Create user (admin only)
- GET `/api/users/{id}/`: Retrieve user
- PUT `/api/users/{id}/`: Update user
- DELETE `/api/users/{id}/`: Delete user

### Posts
- GET `/api/posts/`: List posts
- POST `/api/posts/`: Create post (authenticated)
- GET `/api/posts/{id}/`: Retrieve post
- PUT `/api/posts/{id}/`: Update post (author only)
- DELETE `/api/posts/{id}/`: Delete post (author only)

### Comments
- GET `/api/comments/`: List comments
- POST `/api/comments/`: Create comment (authenticated)
- GET `/api/comments/{id}/`: Retrieve comment
- PUT `/api/comments/{id}/`: Update comment (author only)
- DELETE `/api/comments/{id}/`: Delete comment (author only)

### Likes
- GET `/api/likes/`: List likes
- POST `/api/likes/`: Create like (authenticated)
- DELETE `/api/likes/{id}/`: Delete like (owner only)

## Testing

1. Get a JWT token:
```bash
curl -X POST http://localhost:8000/api/token/ -d "username=your_username&password=your_password"
```

2. Use the token in subsequent requests:
```bash
curl -H "Authorization: Bearer your_token_here" http://localhost:8000/api/posts/
```

3. Create a new post:
```bash
curl -X POST \
  -H "Authorization: Bearer your_token_here" \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Post","content":"This is a test post","is_published":true}' \
  http://localhost:8000/api/posts/
```

## Security Notes

For production:
1. Set DEBUG=False in settings.py
2. Use environment variables for sensitive data
3. Configure proper CORS settings
4. Enable HTTPS
5. Set up proper database (PostgreSQL recommended)
6. Configure proper logging (Django REST Framework)

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

## Testing with Thunder Client / Postman

API Routes & Test JSON Examples:

### Authentication

1. Register a new user:
```http
POST /api/register/
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "strongpassword",
  "role": "blogger"  // Optional: "user", "blogger", or "admin"
}
```

2. Get JWT Token:
```http
POST /api/token/
{
  "username": "john_doe",
  "password": "strongpassword"
}
```

3. Refresh Token:
```http
POST /api/token/refresh/
{
  "refresh": "your_refresh_token_here"
}
```
4. Log out:
  ```http
  POST /api/logout/
  Authorization: Bearer your_access_token
  ```

  Success Response (200 OK):
  ```json
  {
    "status": "success",
    "message": "Successfully logged out"
  }
  ```

### Posts

1. List all posts:
```http
GET /api/posts/
Authorization: Bearer your_token_here
```

2. Create a new post:
```http
POST /api/posts/
Authorization: Bearer your_token_here
{
  "title": "First Post",
  "content": "This is the content of the first post.",
  "is_published": true
}
```

3. Get a specific post:
```http
GET /api/posts/{id}/
Authorization: Bearer your_token_here
```

4. Update a post:
```http
PUT /api/posts/{id}/  # Note: The trailing slash is required
Authorization: Bearer your_token_here
{
  "title": "Updated Post Title",
  "content": "Updated content.",
  "is_published": true
}
```

5. Delete a post:
```http
DELETE /api/posts/{id}/
Authorization: Bearer your_token_here

Response (Success - 200 OK):
{
    "status": "success",
    "message": "Post deleted successfully"
}

Response (Error - 403 Forbidden):
{
    "status": "error",
    "message": "You can only delete your own posts"
}
```

### Comments

1. List all comments:
```http
GET /api/comments/
Authorization: Bearer your_token_here
```

2. Create a comment:
```http
POST /api/comments/
Authorization: Bearer your_token_here
{
  "text": "This is a comment.",
  "post": 1  // ID of the post to comment on
}

Response (Success - 201 Created):
{
  "status": "success",
  "message": "Comment created successfully",
  "data": {
    "id": 1,
    "text": "This is a comment.",
    "created_at": "2025-08-27T08:16:29Z",
    "post": 1,
    "user": "john_doe"  // Username is automatically set from the token
  }
}
```

3. Update a comment:
```http
PUT /api/comments/{id}/  # Note: The trailing slash is required
Authorization: Bearer your_token_here
{
  "text": "Updated comment content."  // Only the text can be updated
}

Response (Success - 200 OK):
{
  "status": "success",
  "message": "Comment updated successfully",
  "data": {
    "id": 1,
    "text": "Updated comment content.",
    "created_at": "2025-08-27T08:16:29Z",
    "post": 1,
    "user": "john_doe"
  }
}

Response (Error - 403 Forbidden):
{
  "status": "error",
  "message": "You can only edit your own comments"
}
```

4. Delete a comment:
```http
DELETE /api/comments/{id}/  # Note: The trailing slash is required
Authorization: Bearer your_token_here

Response (Success - 200 OK):
{
    "status": "success",
    "message": "Comment deleted successfully"
}

Response (Error - 403 Forbidden):
{
    "status": "error",
    "message": "You can only delete your own comments"
}
```

### Likes

1. List all likes:
```http
GET /api/likes/
Authorization: Bearer your_token_here
```

2. Create a like:
```http
POST /api/likes/
Authorization: Bearer your_token_here
{
  "post": 1
}
```

3. Delete a like:
```http
DELETE /api/likes/{id}/
Authorization: Bearer your_token_here
```

### Users (Admin Only)

To access these endpoints, you need to:
1. Register with an admin account (username containing 'admin' or role set to 'admin')
2. Login with those admin credentials
3. Use the received token in your requests

1. List all users:
```http
POST /api/register/  # First, create an admin account
Content-Type: application/json

{
    "username": "admin_user",  # or set role: "admin"
    "email": "admin@example.com",
    "password": "your_password"
}
```

```http
POST /api/token/  # Then login to get the admin token
Content-Type: application/json

{
    "username": "admin_user",
    "password": "your_password"
}
```

```http
GET /api/users/  # Now you can list users
Authorization: Bearer your_admin_token
```

2. Get a specific user:
```http
GET /api/users/{id}/
Authorization: Bearer your_admin_token
```

Note: Only users with admin privileges (is_staff=True) can access these endpoints. Make sure your username contains 'admin' or you set the role as 'admin' during registration.

Note: All requests except registration and token generation require a valid JWT token in the Authorization header. The token can be obtained by calling the `/api/token/` endpoint with valid credentials.
