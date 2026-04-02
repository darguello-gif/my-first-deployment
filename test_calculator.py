"""
Tests for Calculator App
These tests will run automatically every time you push code!
"""

import pytest
from calculator import add, subtract, multiply, divide, greet


class TestBasicMath:
    """Test basic math operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-5, -3) == -8
        assert add(-10, 5) == -5
    
    def test_subtract(self):
        """Test subtraction"""
        assert subtract(10, 5) == 5
        assert subtract(0, 5) == -5
    
    def test_multiply(self):
        """Test multiplication"""
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(0, 100) == 0
    
    def test_divide(self):
        """Test division"""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
        assert divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises an error"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestGreeting:
    """Test greeting functionality"""
    
    def test_greet_with_name(self):
        """Test greeting with a name"""
        assert greet("Diego") == "Hello, Diego!"
        assert greet("Alice") == "Hello, Alice!"
    
    def test_greet_without_name(self):
        """Test greeting without a name"""
        assert greet("") == "Hello, stranger!"
        assert greet(None) == "Hello, stranger!"
