# Django CRM (Customer Relationship Management System)

## Project Overview
A robust Customer Relationship Management (CRM) system built with Django, designed to help businesses manage customer relationships, track sales performance, and monitor revenue metrics. The system provides real-time analytics, user activity tracking, and comprehensive order management capabilities.

## Project Structure and Design Choices

### Core Applications

#### API Application (`api/`)
The main application handling core business logic:

- **Models** (`models.py`):
  - `Order`: Manages customer order data with history tracking
  - `Campaign`: Tracks marketing campaign performance
  - `Activity`: Records user activities for audit trails
  - `Comment`: Enables communication and status updates on orders
  
  Design Choice: Implemented Django's built-in history tracking for orders to maintain a complete audit trail of changes, crucial for business accountability.

- **Views** (`views.py`):
  - Class-based views for better code organization and reusability
  - Custom manager methods for filtering orders (today, week, month)
  - Search functionality using PostgreSQL's full-text search
  
  Design Choice: Chose class-based views over function-based views for better code organization and inheritance capabilities.

#### Authentication System
- Custom user model extending Django's AbstractUser
- Role-based access control
- Secure login/logout functionality

Design Choice: Implemented custom user model from the start to allow future extensions without database migrations.

### Templates Structure (`templates/`)
Organized in modular components:
- `base.html`: Base template with common elements
- `navbar.html`: Responsive navigation component
- `order/`: Order-related templates
- `admin/`: Administrative interface templates

Design Choice: Used template inheritance to maintain DRY principles and ensure consistent styling.

### Settings Configuration (`dcrm/settings/`)
Split into multiple files for better environment management:
- `base.py`: Common settings
- `dev.py`: Development-specific settings
- `prod.py`: Production-specific settings

Design Choice: Separated settings to maintain clean development/production environments and secure sensitive data.

## Technical Implementation

### Backend Architecture
- **Django ORM**: Utilized for database operations
- **Custom Model Managers**: Implemented for specialized queries
- **Middleware**: Custom middleware for activity tracking
- **Signal Handlers**: For order history and notification systems

### Frontend Implementation
- **Bootstrap 5**: Responsive design framework
- **JavaScript**: Dynamic UI updates and form handling
- **Custom CSS**: Tailored styling with dark mode support

### Database Design
- PostgreSQL for production
- Optimized queries using select_related() and prefetch_related()
- Indexed fields for improved search performance

Design Choice: Chose PostgreSQL over SQLite for its advanced features like full-text search and better concurrency.

## Security Measures
- Django's built-in XSS protection
- CSRF protection on all forms
- Secure password hashing
- Environment variables for sensitive data
- Regular security updates

## Performance Optimizations
- Database query optimization
- Caching strategy for frequently accessed data
- Efficient pagination implementation
- Static file serving with WhiteNoise

## Deployment
Hosted on Heroku with:
- Gunicorn as WSGI HTTP Server
- WhiteNoise for static files
- Heroku PostgreSQL for database
- Automatic deployments from main branch

## Future Enhancements
1. API endpoint documentation with Swagger
2. Enhanced reporting capabilities
3. Email notification system
4. Mobile application integration
5. Advanced analytics dashboard

## Technologies Used

### Backend
- **Python 3** - Core programming language
- **Django** - Web framework
- **PostgreSQL** - Primary database
- **Django REST Framework** - API development

### Frontend
- **HTML5** - Page structure
- **CSS3** - Styling
- **JavaScript** - Client-side interactions
- **Bootstrap 5** - Frontend framework
- **Font Awesome** - Icons

### Deployment & Hosting
- **Heroku** - Cloud platform hosting
- **Heroku PostgreSQL** - Production database
- **Gunicorn** - WSGI HTTP Server
- **WhiteNoise** - Static files serving

## Getting Started

### Viewing Live - [crm.laytonreynolds.com](http://crm.laytonreynolds.com/)

### Running Locally

#### Clone
`git clone git@github.com:laytreynolds/dcrm.git`

#### Activate Virtual Env

`python -m venv ./venv`<br /><br />
**Linux** / **MAC** - source ./venv/bin/activate<br /><br />
**Windows** - ./venv/Scripts/Activate.ps1<br />

#### Install Requirements
`pip install -r requirements.txt`

#### Create Environment Variables
- **Filename** - `.env.dev`
- **Variables**<br />
  - `SECRET_KEY="asdadgtuyi78654ew@#$&*ikjnbvcxsa23$%^&*IKjnbvcxzq12!123456"`<br />
  - `DB_NAME=`<br />
  - `DB_USER=`<br />
  - `DB_PASSWORD=`<br />
  - `DB_HOST=`<br />
  - `PORT=5432`<br />
  - `DEBUG=False`<br />

### Create Self Signed Cert
`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"`
#### Running Server
`python ./manage.py runserver_plus`

## Endpoints

### Authentication
- `/login/` - User login page
- `/logout/` - User logout page

### Home
- `/` - Home page (login required)

### Orders
- `/orders/` - List all orders (paginated)
- `/orders/today/` - View orders from today
- `/orders/week/` - View orders from this week
- `/orders/month/` - View orders from this month
- `/orders/search/` - Search orders by email, company name, order number, mobile, first name, or last name
- `/orders/<order_id>/` - View detailed information about a specific order
- `/orders/new/` - Create a new order
- `/orders/<order_id>/update/` - Update an existing order
- `/orders/connected/month/` - View connected orders for current month

### Comments
- `/orders/<order_id>/comment/` - Add a comment to an order
- `/orders/<order_id>/comment/update/` - Update comment status

### Dashboard
- `/dashboard/` - View dashboard with:
  - Daily revenue
  - Weekly revenue
  - Monthly revenue
  - Connected revenue for current month
  - Top 10 users leaderboard
  - Campaign performance

### Admin
- `/admin/users/` - List all users
- `/admin/users/new/` - Create new user
- `/admin/users/<id>/edit/` - Edit existing user
- `/admin/users/<id>/delete/` - Delete user

## Authentication

All endpoints (except login/logout) require user authentication. Protected routes are decorated with `@login_required` or inherit from `LoginRequiredMixin`.

## Pagination

List views are paginated with 9 items per page.

## Search Functionality

The order search supports:
- Order Email
- Company Name
- Order Number
- Mobile Number
- First Name
- Last Name

## Models

The system includes the following main models:
- User
- Order
- Campaign
- Activity
- Comment

## Features

- Full order management system
- User activity tracking
- Order history tracking
- Comment system
- Revenue analytics
- User performance tracking
- Campaign tracking
- Responsive design
