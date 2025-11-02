# Game Design Notepad - Backend

The backend API for the Game Design Notepad application - a tool designed to help developers and designers analyze and document game elements, their relationships, and structure.

## Overview

This is a RESTful Flask API that provides comprehensive endpoints for managing game design data. The application supports:

- **Collections** - Organize games or projects into collections
- **Types** - Define categories for game elements (characters, items, locations, etc.)
- **Items** - Create and manage individual game elements
- **Relationships** - Link items together with descriptive relationships
- **Tags** - Label and organize items across collections
- **Notes** - Take detailed notes on any item
- **Color Schemes** - Customize visual appearance for different types
- **User Management** - Multi-user support with authentication

## Tech Stack

- **Framework**: Flask (Python)
- **ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **Authentication**: Flask-Bcrypt + session-based auth
- **Serialization**: Marshmallow
- **CORS**: Flask-CORS

## Getting Started

### Prerequisites

- Python 3.9.6
- PostgreSQL
- pipenv

### Installation

1. Clone the repository
2. Navigate to the backend directory:

   ```bash
   cd gd-notepad-be
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m pipenv shell
   ```

4. Install dependencies:

   ```bash
   pipenv install
   ```

5. Create the database:

   ```bash
   createdb gd-notepad
   ```

6. Set up the environment variable:

   ```bash
   export DATABASE_URI=postgresql://localhost/gd-notepad
   ```

7. Run the application:
   ```bash
   python app.py
   ```

The server will start on `http://127.0.0.1:8086`

## Database Schema

The application uses the following main tables:

- **Users** - User accounts and authentication
- **Auth Tokens** - Session management
- **Collections** - Game/project collections
- **Types** - Element categories
- **Items** - Individual game elements
- **Relationships** - Links between items
- **Tags** - Labeling system
- **Notes** - Item documentation
- **Color Schemes** - Visual styling
- **Items Tags Xref** - Many-to-many relationship between items and tags
- **Roles Permissions Xref** - User permissions
- **Change Logs** - Audit trail

## API Endpoints

### Authentication

- `POST /user/auth` - Login
- `GET /user/check-login` - Verify authentication
- `POST /user/logout` - Logout

### Users

- `POST /user` - Create user
- `GET /users` - Get all users
- `GET /user/<id>` - Get user by ID
- `PUT /user/<id>` - Update user
- `DELETE /user/delete/<id>` - Delete user

### Collections

- `POST /collection` - Create collection
- `GET /collections` - Get all collections
- `GET /collection/<id>` - Get collection by ID
- `PUT /collection/<id>` - Update collection
- `DELETE /collection/delete/<id>` - Delete collection

### Types

- `POST /type` - Create type
- `GET /types` - Get all types
- `GET /types/collection/<collection_id>` - Get types for collection
- `GET /type/<id>` - Get type by ID
- `PUT /type/<id>` - Update type
- `DELETE /type/delete/<id>` - Delete type

### Items

- `POST /item` - Create item
- `GET /items` - Get all items
- `GET /items/collection/<collection_id>` - Get items for collection
- `GET /item/<id>` - Get item by ID
- `PUT /item/<id>` - Update item
- `DELETE /item/delete/<id>` - Delete item
- `POST /item/tag` - Add tags to item

### Relationships

- `POST /relationship` - Create relationship
- `GET /relationships` - Get all relationships
- `GET /relationships/collection/<collection_id>` - Get relationships for collection
- `GET /relationship/<id>` - Get relationship by ID
- `PUT /relationship/<id>` - Update relationship
- `DELETE /relationship/delete/<id>` - Delete relationship

### Tags

- `POST /tag` - Create tag
- `GET /tags` - Get all tags
- `GET /tag/<id>` - Get tag by ID
- `PUT /tag/<id>` - Update tag
- `DELETE /tag/delete/<id>` - Delete tag

### Notes

- `POST /note` - Create note
- `GET /notes` - Get all notes
- `GET /notes/collection/<collection_id>` - Get notes for collection
- `GET /note/<id>` - Get note by ID
- `PUT /note/<id>` - Update note
- `DELETE /note/delete/<id>` - Delete note

### Color Schemes

- `POST /color-scheme` - Create color scheme
- `GET /color-schemes` - Get all color schemes
- `GET /color-scheme/<id>` - Get color scheme by ID
- `PUT /color-scheme/<id>` - Update color scheme
- `DELETE /color-scheme/delete/<id>` - Delete color scheme

## Demo Data

The application automatically loads demo data on startup, including:

- Sample collections
- Game element types
- Items with relationships
- Tags and notes
- Color schemes

This demo data uses examples from "Watership Down" and "Super Mario Bros." to demonstrate the system's capabilities.

## Development

The project structure follows Flask best practices:

```
gd-notepad-be/
├── app.py                 # Application entry point
├── db.py                  # Database configuration
├── models/                # SQLAlchemy models
├── controllers/           # Business logic
├── routes/                # URL routing
├── util/                  # Utility functions
├── lib/                   # Libraries and helpers
│   ├── authenticate.py    # Auth decorators
│   └── demo_data/         # Demo data scripts
└── Pipfile                # Python dependencies
```

## Testing

API endpoints can be tested using:

- Postman collections (included in repository)
- curl commands
- Frontend application
- API testing tools
