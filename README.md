# EV Charging Station Finder and Management System

A Django-based REST API for locating and managing electric vehicle (EV) charging stations in Germany, built with PostgreSQL (PostGIS), Django REST Framework, and Celery for background tasks.

## Features
- **User Side:**
  - Search charging stations by latitude/longitude, name, or station ID.
  - Reserve a charging slot with authentication.
  - View station details (power, connectors, pricing, renewable source).
- **Operator Side:**
  - Dashboard to monitor stations and usage stats (restricted to Operators group).
  - Update station details (admin-only).
- **Technical Highlights:**
  - Geospatial queries with PostGIS.
  - JWT authentication with role-based permissions.
  - Logging to file and console.
  - Background task processing with Celery and Redis.
  - API versioning and filtering.

## Prerequisites
- Python 3.12
- PostgreSQL with PostGIS extension
- Redis (for Celery)

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ev-charging-backend.git
   cd ev-charging-backend

API Endpoints
GET /api/v1/stations/ - List all stations or filter by location/name.

GET /api/v1/stations/<station_id>/ - Get station details.

POST /api/v1/reservations/ - Reserve a station (authenticated).

GET /api/v1/operator/dashboard/ - Operator dashboard (read-only for all, write for Operators).

POST /api/v1/operator/stations/<station_id>/ - Update station (admin-only).

Testing
Run tests: python manage.py test

Manual testing: Use Postman or curl with the above endpoint

