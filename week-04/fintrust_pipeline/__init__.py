"""
FinTrust Pipeline Package

This package contains the modules used to load transaction data,
store it in SQLite, and generate reports.
"""

from .loader import load_csv
from .database import setup_database, insert_transactions
from .reporter import generate_report