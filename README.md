# Marketplace-API

Webserver API for Coder Academy T2A2

Github link: <https://github.com/Reyleth/Marketplace-API>

## Project Overview

### Problem Statement

In a massively multiplayer online (MMO) game environment, managing in-game economies can be complex. Players need a seamless way to buy, sell, and trade items with each other. This process can be inefficient and frustrating without a proper system, leading to a negative gaming experience. Common issues include:

1. **Inefficient Trading**: Without a centralized marketplace, players have to rely on direct trades, which can be time-consuming and difficult to coordinate.
2. **Price Inconsistencies**: Lack of a standardized pricing mechanism can lead to unfair trades and price gouging.
3. **Inventory Management**: Players may struggle to keep track of their items and available inventory, leading to disorganization.
4. **Transaction Security**: Without a reliable system, players may face scams and insecure trades.

### Solution: Marketplace API

The Marketplace API addresses these problems by providing a structured and secure platform for item trading within a game. Here's how it solves the issues:

1. **Centralized Trading Platform**:
   - The API provides routes for creating and managing marketplace listings, allowing players to buy and sell items in a centralized location. This eliminates the need for direct player-to-player trades, making the process more efficient and accessible.

2. **Standardized Pricing Mechanism**:
   - By listing items with defined prices, the API ensures transparency and fairness in trades. Players can see the prices of items listed by others, helping to standardize market values and reduce price gouging.

3. **Inventory Management**:
   - The API includes routes for managing user inventories, allowing players to easily keep track of their items. Players can view their inventory, add new items, and remove items as needed, ensuring better organization.

4. **Secure Transactions**:
   - The API handles transactions securely, reducing the risk of scams and ensuring that trades are completed reliably. The transaction endpoints facilitate the buying and selling process, recording transaction details for accountability and security.

### Benefits

- **Efficiency**: Streamlines the buying and selling process, making it easier for players to trade items.
- **Fair Pricing**: Helps maintain fair market prices by displaying current listings and their prices.
- **Organization**: Simplifies inventory management, reducing clutter and confusion.
- **Security**: Ensures safe and reliable transactions, protecting players from scams and unreliable trades.

By addressing these key issues, the Marketplace API enhances the overall gaming experience, providing players with a robust and user-friendly platform for managing their in-game trades and inventory.

## Project Workflow

This project is being managed and tracked via a github project located at <https://github.com/users/Reyleth/projects/2/views/1>

### Early Stages

[Early Stages](./imgs/Early_Stages.png)

### Late Stages

[Late Stages](./imgs/Late_Stages.png)

## App Dependancies

This application uses several third-party Python packages, each serving a specific purpose within the project. Here's a breakdown of these dependencies:

1. **bcrypt (4.1.3)**: A library for hashing passwords. It's used to securely store user passwords by hashing them before they are stored in the database.

2. **blinker (1.8.2)**: Provides support for Signals. It is often used in applications that use Flask to allow different parts of the application to communicate with each other without being directly connected.

3. **cffi (1.16.0)**: Stands for C Foreign Function Interface. It's used to call C code from Python. It might be a dependency for other packages that need to compile C code.

4. **click (8.1.7)**: A package for creating command-line interfaces. It's a dependency for Flask and is used to create management commands for Flask applications.

5. **cryptography (42.0.8)**: Provides cryptographic recipes and primitives. It's used for secure password storage, generating tokens, and other security-related tasks.

6. **Flask (3.0.3)**: A lightweight WSGI web application framework. It's the core framework used for building web applications in this project.

7. **Flask-Bcrypt (1.0.1)**: An extension for Flask that provides bcrypt hashing utilities for your application. It integrates the bcrypt library with Flask.

8. **Flask-JWT-Extended (4.6.0)**: An extension for Flask that adds support for JSON Web Tokens (JWT) in Flask applications, providing a way to handle user authentication.

9. **flask-marshmallow (1.2.1)**: An integration layer for Flask and marshmallow (an ORM/ODM/schema validation library). It simplifies serialization and deserialization of complex data types to and from Python objects.

10. **Flask-SQLAlchemy (3.1.1)**: An extension for Flask that adds support for SQLAlchemy, a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It simplifies database operations.

11. **itsdangerous (2.2.0)**: A library to pass trusted data to untrusted environments and back. It's often used with Flask to securely sign data, like cookies or URLs.

12. **Jinja2 (3.1.4)**: A modern and designer-friendly templating language for Python, modeled after Django’s templates. It's Flask's default template engine.

13. **jwt (1.3.1)**: A library to work with JSON Web Tokens. This might be a dependency pulled in by Flask-JWT-Extended or used directly for handling JWTs.

14. **MarkupSafe (2.1.5)**: Escapes characters so a string is safe to use in HTML and XML. It's used by Jinja2 and Flask to prevent injection attacks.

15. **marshmallow (3.21.3)**: A library for object serialization and deserialization, ORM/ODM/schema validation. It works well with many ORMs, web frameworks, and databases.

16. **marshmallow-sqlalchemy (1.0.0)**: Provides SQLAlchemy integration with the marshmallow library, simplifying object serialization/deserialization for SQLAlchmey models.

17. **packaging (24.1)**: A core utility for version handling and package compatibility. It's often a dependency for other packages to parse versions and specifications.

18. **psycopg2 (2.9.9) and psycopg2-binary (2.9.9)**: PostgreSQL database adapters for Python. The binary package is a standalone package meant to avoid the need for compiling the C source code.

19. **pycparser (2.22)**: A C parser in Python. It's a dependency for packages that need to parse C code, like cffi.

20. **PyJWT (2.8.0)**: A Python library which allows you to encode and decode JSON Web Tokens (JWT). It's used for authentication mechanisms.

21. **python-dotenv (1.0.1)**: Reads key-value pairs from a [`.env`] file and sets them as environment variables. It's used for managing application configuration and secrets.

22. **SQLAlchemy (2.0.30)**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a full suite of well-known enterprise-level persistence patterns.

23. **typing_extensions (4.12.2)**: Backported and experimental type hints for Python. It's used to provide additional typing features not available in the standard `typing` module.

24. **Werkzeug (3.0.3)**: A WSGI utility library for Python. It's a dependency of Flask and provides various utilities for request, response objects, and other utility functions.

These packages together provide a robust foundation for web application development, offering tools for web server management, security, database interaction, data validation and serialization, and much more.

## Drawbacks and benefits to the underlying database and ORM system

This database setup involves using SQLAlchemy as the ORM (Object-Relational Mapping) tool with PostgreSQL as the underlying database.

### Benefits of the DB and ORM

1. **SQLAlchemy as ORM:**
   - **Abstraction and Flexibility:** SQLAlchemy provides a high-level abstraction for database interactions, allowing developers to work with Python objects instead of writing SQL queries directly. This can speed up development and reduce errors.
   - **Database Agnostic:** It supports multiple databases such as PostgreSQL, MySQL and SQLite, making it easier to switch underlying databases if needed without changing the application logic.
   - **Powerful Query Capabilities:** Offers a rich query language that is flexible and Pythonic, enabling complex queries to be written more intuitively and with ease.

2. **PostgreSQL:**
   - **Robustness and Reliability:** PostgreSQL is known for its reliability, data integrity, and correctness. It's a powerful, open-source object-relational database system with a strong reputation.
   - **Advanced Features:** Supports advanced data types (e.g., JSON/JSONB, arrays), full-text search, and other sophisticated features that are beneficial for complex applications.
   - **Scalability:** Good support for large datasets and complex queries, with capabilities to scale vertically and horizontally.
   - **Strong Community and Ecosystem:** A large community and a wide range of extensions and tools available.

### Drawbacks of the DB and ORM

1. **SQLAlchemy:**
   - **Performance Overhead:** The abstraction layer adds overhead, which can lead to slower performance compared to raw SQL for complex queries or high-load scenarios.
   - **Learning Curve:** While SQLAlchemy simplifies database interactions, mastering its advanced features and query optimizations can be challenging for new developers.

2. **PostgreSQL:**
   - **Resource Intensive:** Can be more resource-intensive than lighter databases like SQLite, especially in terms of memory usage, which might be a consideration for small-scale applications or environments with limited resources.
   - **Complexity:** With its advanced features comes complexity. Setting up, tuning, and maintaining a PostgreSQL database can require more expertise and effort compared to simpler database systems.

In summary, the combination of SQLAlchemy and PostgreSQL provides a powerful, flexible, and reliable foundation for web applications, with trade-offs in terms of performance overhead and complexity. The choice of this stack is well-suited for applications that require complex data models, data integrity, and scalability, while also benefiting from an ORM's productivity and flexibility.

### Example

```py
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

# Example usage
if __name__ == "__main__":
    engine = create_engine('sqlite:///example.db', echo=True)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_user = User(username='john_doe', email='john.doe@example.com', password='securepassword123')
    session.add(new_user)
    session.commit()
    
    user = session.query(User).filter_by(username='john_doe').first()
    print(user)
```

This code snippet defines a simple User model using SQLAlchemy's ORM capabilities. It includes fields for id, username, email, and password.

## ERD Diagram

[ERD Diagram](./imgs/ERD_diagram.png)

## Explanation of the models

The implemented models and their relationships in this project are designed to support a marketplace application. Here's a quick overview of the models and their relationships:

1. **User**: Represents users of the marketplace. Users can be buyers or sellers.

2. **Item**: Represents items that can be listed in the marketplace for sale.

3. **Listing**: Represents a specific sale listing in the marketplace. It links an item to a seller and includes details like price, quantity, and status (e.g., active).

4. **Inventory**: Represents the inventory of items that a user has. It links users to items and includes a quantity to indicate how many of each item a user possesses.

5. **Transaction**: Represents a transaction in the marketplace. It links a buyer to a seller, an item, and the specific listing from which the item was purchased. It includes details like price, quantity, and status (e.g., completed).

### Relationships

- **User to Listing (One-to-Many)**: A user can have multiple listings (as a seller), but each listing is associated with one seller. This relationship allows tracking of which user is selling what item.

- **Item to Listing (One-to-Many)**: An item can be part of multiple listings (e.g., sold by different users or listed multiple times by the same user), but each listing is for one specific item. This relationship facilitates the management of listings for the same item by different sellers.

- **User to Inventory (One-to-Many)**: A user can have multiple items in their inventory, but each inventory record is associated with one user. This relationship helps manage the items a user owns.

- **Item to Inventory (One-to-Many)**: An item can be in the inventories of multiple users, but each inventory record is for one specific item. This relationship allows tracking of which users own a particular item.

- **Transaction Specific Relationships**:
  - **Buyer to Transaction (One-to-Many)**: A user (as a buyer) can have multiple transactions, but each transaction is associated with one buyer. This relationship tracks the purchases made by a user.
  - **Seller to Transaction (One-to-Many)**: Similarly, a user (as a seller) can have multiple transactions, but each transaction is associated with one seller. This tracks the sales made by a user.
  - **Item to Transaction (One-to-Many)**: An item can be part of multiple transactions (sold multiple times), but each transaction is for one specific item. This helps in tracking the sales history of an item.
  - **Listing to Transaction (One-to-One)**: Each transaction is linked to a specific listing from which an item was purchased. This relationship ensures that each transaction can be traced back to the specific listing, including the sale conditions like price and quantity.

These relationships are crucial for the database implementation as they enable efficient data organization, retrieval, and integrity. They allow the application to easily query related data, such as all listings by a user, all transactions for an item, or the inventory of a user, facilitating the marketplace's core functionalities.

## Route Endpoints

Listed below are all the routes used in this API.

## Users API

### POST /users/login

- **Description**: Authenticates a user and returns a JWT token.
- **Body**: `{"email": "user@example.com", "password": "password"}`
- **Response**:
  - **200 OK**: `{"token": "<JWT_TOKEN>"}`
  - **401 Unauthorized**: `{"error": "Invalid email or password"}`

### GET /users/<int:user_id>/inventory

- **Description**: Retrieves the inventory of a specific user.
- **Parameters**: [`user_id`]("blueprints/users_bp.py") (in URL)
- **Response**:
  - **200 OK**: `{"inventory": [<items>]}`
  - **404 Not Found**: `{"error": "User not found"}`

### POST /users/<int:user_id>/inventory/add

- **Description**: Adds an item to a user's inventory. Requires admin privileges.
- **Parameters**: [`user_id`]("blueprints/users_bp.py") (in URL)
- **Body**: Login data in JSON format.

```json
{
  "email": "admin@spam.com",
  "password": "secretpassword"
}
```

- **Response**:
  - **200 OK**: `{"message": "Item added to inventory"}`
  - **404 Not Found**: `{"error": "User not found"}`

## Transactions API

### POST /transactions/create

- **Description**: Creates a new transaction. Requires admin privileges.
- **Body**: Transaction data in JSON format.
- **Response**:
  - **200 OK**: Transaction data.

### GET /transactions/<int:transaction_id>

- **Description**: Retrieves a specific transaction.
- **Parameters**: [`transaction_id`]("blueprints/transactions_bp.py") (in URL)
- **Response**: Transaction data.

### GET /users/<int:user_id>/transactions

- **Description**: Retrieves all transactions for a specific user.
- **Parameters**: [`user_id`]("blueprints/users_bp.py") (in URL)
- **Response**: List of transactions.

### POST /transactions/<int:transaction_id>/buy

- **Description**: Marks a transaction as purchased. Requires buyer privileges.
- **Parameters**: [`transaction_id`]("blueprints/transactions_bp.py") (in URL)
- **Response**: Updated transaction data.

## Listings API

### GET /listings

- **Description**: Retrieves all listings.
- **Response**: List of listings.

### GET /listings/<int:listing_id>

- **Description**: Retrieves a specific listing.
- **Parameters**: [`listing_id`]("blueprints/listings_bp.py") (in URL)
- **Response**: Listing data.

### POST /listings/create

- **Description**: Creates a new listing. Requires authentication.
- **Body**: Listing data in JSON format.

```json
{
  "item_id": 1,
  "price": 20
}
```

- **Response**:
  - **201 Created**: Listing data.
  - **403 Forbidden**: `{"message": "User not found"}`

### PUT /listings/<int:listing_id>

- **Description**: Updates a specific listing. Requires seller privileges.
- **Parameters**: [`listing_id`]("blueprints/listings_bp.py") (in URL)
- **Body**: Updated listing data in JSON format.

```json
{
  "item_id": 1,
  "price": 50
}
```

- **Response**: Updated listing data.

### DELETE /listings/<int:listing_id>

- **Description**: Deletes a specific listing. Requires seller privileges.
- **Parameters**: [`listing_id`]("blueprints/listings_bp.py") (in URL)
- **Response**: `{"message": "Listing deleted successfully"}`

## Items API

### GET /items

- **Description**: Retrieves all items.
- **Response**: List of items.

### GET /items/<int:item_id>

- **Description**: Retrieves a specific item.
- **Parameters**: [`item_id`]("blueprints/items_bp.py") (in URL)
- **Response**: Item data.

### POST /items/create

- **Description**: Creates a new item. Requires admin privileges.
- **Body**: Item data in JSON format.

```json
{
"name":"Sword",
"description":"Just a plain old sword",
"category":"Weapon",
"rarity":"Common",
"price":10.00,
}
```

- **Response**: Item data.

### PUT /items/<int:item_id>

- **Description**: Updates a specific item. Requires admin privileges.
- **Parameters**: [`item_id`]("blueprints/items_bp.py") (in URL)
- **Body**: Updated item data in JSON format.

```json
{
"name":"Sword",
"description":"Just a cooler sword",
"category":"Weapon",
"rarity":"Rare",
"price":50.00,
}
```

- **Response**: Updated item data.

### DELETE /items/<int:item_id>

- **Description**: Deletes a specific item. Requires admin privileges.
- **Parameters**: [`item_id`]("blueprints/items_bp.py") (in URL)
- **Response**: `{"message": "Item deleted successfully"}`
