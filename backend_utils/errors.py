class AppError(Exception):
    """Base class for application errors."""
    pass

class ValidationError(AppError):
    """Raised when invalid data is provided."""
    pass

class DatabaseError(AppError):
    """Raised when database operation fails."""
    pass
