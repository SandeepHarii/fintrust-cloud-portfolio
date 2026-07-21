-- ════════════════════════════════════════════════════════════
-- FinTrust Bank — Core Database Schema
-- Database: fintrust_db
-- Region: af-south-1 (Cape Town) — POPIA data residency
-- ════════════════════════════════════════════════════════════

CREATE DATABASE IF NOT EXISTS fintrust_db
    CHARACTER SET utf8mb4     -- supports all Unicode characters (names, emojis)
    COLLATE utf8mb4_unicode_ci; -- case-insensitive comparison

USE fintrust_db;

-- ────────────────────────────────────────────────────────────
-- TABLE: customers
-- One row per FinTrust Bank account holder.
-- ────────────────────────────────────────────────────────────
CREATE TABLE customers (
    customer_id  INT           PRIMARY KEY AUTO_INCREMENT,
                                -- Auto-incrementing PK: no manual ID management
    first_name   VARCHAR(100)  NOT NULL,
                                -- 100 chars covers all names including compound names
    last_name    VARCHAR(100)  NOT NULL,
    email        VARCHAR(200)  UNIQUE NOT NULL,
                                -- UNIQUE: one account per email. NOT NULL: required field.
    province     VARCHAR(50),  -- Nullable: customers may not disclose province
    created_at   DATETIME      DEFAULT CURRENT_TIMESTAMP
                                -- Audit timestamp — set by DB, not application code
);

-- ────────────────────────────────────────────────────────────
-- TABLE: accounts
-- One row per bank account. One customer may have multiple accounts.
-- ────────────────────────────────────────────────────────────
CREATE TABLE accounts (
    account_id      INT           PRIMARY KEY AUTO_INCREMENT,
    customer_id     INT           NOT NULL,
                                   -- FK to customers — references parent customer
    account_type    ENUM('CHEQUE','SAVINGS','CREDIT','BUSINESS') NOT NULL,
                                   -- ENUM: database enforces valid values
    account_number  VARCHAR(20)   UNIQUE NOT NULL,
                                   -- VARCHAR not INT: account numbers have prefixes (FT-CHQ-...)
    balance         DECIMAL(15,2) DEFAULT 0.00,
                                   -- DECIMAL not FLOAT: exact financial values
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
                                   -- Referential integrity: no orphaned accounts
);

-- ────────────────────────────────────────────────────────────
-- TABLE: transactions
-- One row per financial event. Links to accounts via FK.
-- ────────────────────────────────────────────────────────────
CREATE TABLE transactions (
    transaction_id    INT           PRIMARY KEY AUTO_INCREMENT,
    account_id        INT           NOT NULL,
                                     -- FK to accounts
    transaction_type  ENUM('DEBIT','CREDIT','PAYMENT') NOT NULL,
    amount            DECIMAL(15,2) NOT NULL,
                                     -- NOT NULL: every transaction must have an amount
    merchant_category VARCHAR(100), -- Nullable: internal transfers have no merchant
    transaction_date  DATETIME      DEFAULT CURRENT_TIMESTAMP,
                                     -- Immutable audit timestamp
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);