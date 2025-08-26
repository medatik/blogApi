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

Here is a JSON collection example for Thunder Client:

```json
[
  {
    "name": "Sign Up",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/signup",
    "body": {
      "username": "john_doe",
      "email": "john@example.com",
      "password": "123456",
      "role": "blogger"
    }
  },
  {
    "name": "Sign In",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/signin",
    "body": {
      "username": "john_doe",
      "password": "123456"
    }
  },
  {
    "name": "Create Post",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/posts",
    "headers": {
      "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    },
    "body": {
      "title": "My First Post",
      "content": "This is the content of my first post",
      "is_published": true
    }
  },
  {
    "name": "List Posts",
    "method": "GET",
    "url": "http://127.0.0.1:8000/api/posts"
  },
  {
    "name": "Add Comment",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/comments",
    "headers": {
      "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    },
    "body": {
      "text": "Great post!",
      "post": 1
    }
  },
  {
    "name": "Like Post",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/likes",
    "headers": {
      "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    },
    "body": {
      "post": 1
    }
  }
]
```

You can export this as a **Thunder Client collection** and directly test the API.

---

## Roles and Permissions

- **Admin**: Full access to users and posts.
- **Blogger**: Can create, edit, publish, and delete their own posts.
- **User**: Can read posts, like, and comment.

---

## Authentication

This project uses **JWT Authentication**:
- Obtain token: `POST /api/signin`
- Refresh token: `POST /api/token/refresh`

Add this to every request that requires authentication:
```
Authorization: Bearer <access_token>
```

---

## License

MIT
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
git clone https://github.com/yourusername/alxApiBlog.git
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

Here is a JSON collection example for Thunder Client:

```json
[
  {
    "name": "Sign Up",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/signup",
    "body": {
      "username": "john_doe",
      "email": "john@example.com",
      "password": "123456",
      "role": "blogger"
    }
  },
  {
    "name": "Sign In",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/signin",
    "body": {
      "username": "john_doe",
      "password": "123456"
    }
  },
  {
    "name": "Create Post",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/posts",
    "headers": {
      "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    },
    "body": {
      "title": "My First Post",
      "content": "This is the content of my first post",
      "is_published": true
    }
  },
  {
    "name": "List Posts",
    "method": "GET",
    "url": "http://127.0.0.1:8000/api/posts"
  },
  {
    "name": "Add Comment",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/comments",
    "headers": {
      "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    },
    "body": {
      "text": "Great post!",
      "post": 1
    }
  },
  {
    "name": "Like Post",
    "method": "POST",
    "url": "http://127.0.0.1:8000/api/likes",
    "headers": {
      "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    },
    "body": {
      "post": 1
    }
  }
]
```

You can export this as a **Thunder Client collection** and directly test the API.

---

## Roles and Permissions

- **Admin**: Full access to users and posts.
- **Blogger**: Can create, edit, publish, and delete their own posts.
- **User**: Can read posts, like, and comment.

---

## Authentication

This project uses **JWT Authentication**:
- Obtain token: `POST /api/signin`
- Refresh token: `POST /api/token/refresh`

Add this to every request that requires authentication:
```
Authorization: Bearer <access_token>
```

---

## License

MIT
