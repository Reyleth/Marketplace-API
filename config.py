from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define the base configuration
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DATABASE_URI = os.getenv('DATABASE_URI', 'default_database_uri')

# Define the specific configurations of each environment
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

# Set the appropriate configuration based on the environment
environment = os.getenv('FLASK_ENV', 'development')
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}.get(environment, DevelopmentConfig)  # Default to DevelopmentConfig if not found