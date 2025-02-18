# ZeBrands Backend Test

## Description

- This API allows you to manage a product catalog with two types of users:

- Administrators: They can create, update and delete products and other administrators.

- Anonymous users: They can view product information.

- In addition, the API records how many times each product is viewed and notifies administrators when a product is updated.
    
## Requirements

- Docker
- Docker Compose

## **Instalation and Configuration**

### 1. Clone the repository

```
git clone https://github.com/tuusuario/zebrands-catalog.git
cd zebrands-catalog
```

### 2. Configure the .env

Run `cp .env.example .env` and define the following variables:


```
SECRET_KEY=SECRET_KEY
DEBUG=True
EMAIL_HOST=smtp.amazon.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu_correo
EMAIL_HOST_PASSWORD=tu_contraseña
```

### 3. Run docker

1. Run `docker-compose up --build` or `docker compose up --build`
2. Access the service at `http://localhost`
3. The default administrator is `dinoadmin` and the password is `dino1234`
4. The default simple user is `dinouser` and the password is `dino1234`


# 📌 API Documentation

## 🔑 Authentication
This API uses **JWT authentication**. To make authenticated requests, you must include the `Authorization` header with the token obtained from the login endpoint.

### 🔹 Obtaining a Token
To get a JWT token, send a `POST` request to:

```http
POST /api/token/
```

**Body:**
```json
{
  "username": "dinoadmin",
  "password": "dino1234"
}
```

**Response:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MDQ5ODA1NywiaWF0IjoxNzM5ODkzMjU3LCJqdGkiOiJkNWVmYzljZDU1MWE0M2Q0OTcxOTg4NWViNmE4OTA2NSIsInVzZXJfaWQiOjF9.a4mvDL84yUiXLcEToSCHdawtRuP4qohjaSy4k5h_6PM",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5OTc5NjU3LCJpYXQiOjE3Mzk4OTMyNTcsImp0aSI6IjMxNjcyNjQ5NTVjNzQyMzBhNjQzNWJkMTVjM2U5MGIwIiwidXNlcl9pZCI6MX0.V7kmcTVORRboKK4uy-7ZDNToxJ8FkmZ_5OTxoUDPbtw"
}
```

### 🔹 Using the Token
For all **protected endpoints**, include the token in the `Authorization` header:

```http
Authorization: Bearer your_access_token
```


## 🛠️ Endpoints

### 🔹 Create a User (Admin Only)
```http
POST /api/users/
```
**Headers:**
```http
Authorization: Bearer your_access_token
```
**Body:**
```json
{
  "username": "newuser",
  "password": "testpass",
  "is_admin": true
}
```
**Response:**
```json
{
  "id": 1,
  "username": "newuser",
  "is_admin": true
}
```

### 🔹 Get User List (Admin Only)
```http
GET /api/users/
```
**Headers:**
```http
Authorization: Bearer your_access_token
```
**Response:**
```json
[
  {
    "id": 1,
    "username": "adminuser",
    "is_admin": true
  },
  {
    "id": 2,
    "username": "testuser",
    "is_admin": false
  }
]
```

### 🔹 Get a Single User (Admin Only)
```http
GET /api/users/{user_id}/
```
**Headers:**
```http
Authorization: Bearer your_access_token
```
**Response:**
```json
{
  "id": 1,
  "username": "adminuser",
  "is_admin": true
}
```

### 🔹 Update a User (Admin Only)
```http
PUT /api/users/{user_id}/
```
**Headers:**
```http
Authorization: Bearer your_access_token
```

### 🔹 Delete a User (Admin Only)
```http
DELETE /api/users/{user_id}/
```
**Headers:**
```http
Authorization: Bearer your_access_token
```

### 🔹 Get Product List (Public)
```http
GET /api/products/
```
**Response:**
```json
[
  {
    "id": 1,
    "sku": "12345",
    "name": "Test Product",
    "price": 10.00,
    "brand": "TestBrand"
  }
]
```

### 🔹 Get a Single Product (Public)
```http
GET /api/products/{product_id}/
```
**Response:**
```json
{
  "id": 1,
  "sku": "12345",
  "name": "Test Product",
  "price": 10.00,
  "brand": "TestBrand"
}
```

### 🔹 Create a Product (Admin Only)
```http
POST /api/products/
```
**Headers:**
```http
Authorization: Bearer your_access_token
```
**Body:**
```json
{
  "sku": "67890",
  "name": "New Product",
  "price": 20.00,
  "brand": "BrandX"
}
```
**Response:**
```json
{
  "id": 2,
  "sku": "67890",
  "name": "New Product",
  "price": 20.00,
  "brand": "BrandX"
}
```

### 🔹 Update a Product (Admin Only)
```http
PUT /api/products/{product_id}/
```
**Headers:**
```http
Authorization: Bearer your_access_token
```

### 🔹 Delete a Product (Admin Only)
```http
DELETE /api/products/{product_id}/
```
**Headers:**
```http
Authorization: Bearer your_access_token
```

---

## 🚀 Notes
- **Admin users** can manage users and products.
- **Non-admin users** can only view products.
- **Anonymous users** can also view products but cannot modify them.
