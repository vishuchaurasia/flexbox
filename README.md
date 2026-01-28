# FlexBook – E-Commerce Platform

A modern, feature-rich e-commerce platform built with Flask and modern web technologies. FlexBook provides a complete solution for online shopping with an intuitive user interface, robust product management, and secure payment processing.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Login Credentials](#login-credentials)
- [Development](#development)
- [Project Management](#project-management)
- [License](#license)
- [Author](#author)

## ✨ Features

### Customer Features
- **Product Browsing**: Explore products with advanced filtering and search capabilities
- **Shopping Cart**: Add/remove items, manage quantities, and persistent cart sessions
- **Checkout Process**: Multi-step checkout with shipping and billing information
- **Order Management**: View order history and track order status
- **User Accounts**: Register, login, and manage account details
- **Address Management**: Save multiple addresses for quick checkout
- **Payment Integration**: Secure Alipay payment gateway integration

### Admin Features
- **Dashboard**: Comprehensive admin dashboard with analytics and overview
- **Product Management**: Create, edit, delete products with categories and collections
- **Order Management**: Track and manage all customer orders
- **User Management**: View and manage customer accounts
- **Discount Management**: Create and manage discount codes
- **Site Configuration**: Manage site settings, pages, and plugins
- **Plugin System**: Extensible plugin architecture for custom functionality

## 🛠️ Tech Stack

### Backend
- **Python 3.9+** - Programming language
- **Flask** - Web framework
- **SQLAlchemy** - ORM for database operations
- **Flask-SQLAlchemy** - Flask-SQLAlchemy integration
- **Alembic** - Database migrations
- **WTForms** - Form validation and rendering
- **Jinja2** - Template engine

### Frontend
- **Webpack** - Module bundler
- **HTML5** - Markup
- **CSS3** - Styling with modern layout techniques
- **JavaScript** - Client-side interactivity

### Database
- **SQLite** (development) - Lightweight database for local development
- **MySQL** (production) - Scalable relational database

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.9+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **Git** - [Download](https://git-scm.com/)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vishuchaurasia/flexbox.git
cd FlexBook
```

### 2. Backend Setup (Windows PowerShell)

Create a Python virtual environment and install dependencies:

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install build tools
python -m pip install --upgrade pip setuptools wheel

# Install project dependencies
pip install --no-compile -r requirements.txt
```
## ⚙️ Configuration

### Database Configuration

The application uses **SQLite** for local development and **MySQL** for production.

#### For SQLite (Development - Default)

Create a `.env` file in the project root:

```env
# Database Configuration
DB_URI=sqlite:///flaskshop.db

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
```

#### For MySQL (Production)

Update your `.env` file:

```env
DB_URI=mysql+pymysql://username:password@localhost:3306/flaskshop
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=your-secret-key-here
```

## 🎯 Running the Application

### 1. Initialize the Database

```powershell
# Create database tables
python -m flask --app app createdb

# Load demo data and users
python manage.py seed
```

### 2. Start the Development Server

```powershell
python app.py
# or
python -m flask --app app run
```

The application will be available at: **http://localhost:5000**

### 3. Login Credentials

#### Admin User
- **Email**: `visaladmin121@test.com`
- **Password**: `vishal@123`
- **Access**: Full admin dashboard at `/dashboard`

#### Regular Customer
- **Email**: `visal121@test.com`
- **Password**: `vishal@123`
- **Access**: Shop products, checkout, view orders

#### Legacy Admin (for compatibility)
- **Email**: `admin@163.com`
- **Password**: `admin`

### 4. Access Admin Dashboard

- **URL**: `http://localhost:5000/dashboard`
- **Login**: Use admin credentials above
- **Features**: Manage products, orders, users, discounts, and more

## 💻 Development

### Project Commands

```powershell
# Run development server
python -m flask --app app run

# Create database
python -m flask --app app createdb

# Seed demo data
python -m flask --app app seed

# Run tests (if configured)
pytest

# Code formatting
black flaskshop/

# Linting
flake8 flaskshop/
```


## 📦 Project Management Features

### Admin Dashboard Capabilities

1. **Analytics & Overview**: View sales, orders, and customer metrics
2. **Product Catalog**: Complete CRUD operations for products, categories, and collections
3. **Order Management**: Track, update, and manage customer orders
4. **Customer Management**: View and manage user accounts and profiles
5. **Promotional Tools**: Create and manage discount codes and promotions
6. **Site Settings**: Configure site-wide settings and static pages
7. **Plugin Management**: Install and manage plugins for extended functionality

### Customer Features

1. **Product Discovery**: Browse products with filtering and search
2. **Shopping Experience**: Intuitive cart and checkout process
3. **Account Management**: User registration, login, and profile management
4. **Order Tracking**: View order history and current order status
5. **Address Book**: Save multiple addresses for faster checkout
6. **Secure Payments**: Integrated Alipay payment gateway

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Vishwajeet Chaurasia**

- GitHub: [@vishuchaurasia](https://github.com/vishuchaurasia)
- Email: Contact via GitHub

---

### Additional Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **SQLAlchemy ORM**: https://docs.sqlalchemy.org/
- **Jinja2 Templates**: https://jinja.palletsprojects.com/

### Support

For issues, questions, or contributions, please create an issue on [GitHub Issues](https://github.com/vishuchaurasia/flexbox/issues).

---

**Last Updated**: January 28, 2026
