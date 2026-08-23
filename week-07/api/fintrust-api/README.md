# FinTrust Transaction API

A REST API built with FastAPI for managing FinTrust banking transactions.

The application was developed as part of Week 7 of the Cloud to Solutions Accelerator programme, focusing on Python API development with FastAPI and Pydantic.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

## Running the Application

Start the API with:

```bash
uvicorn main:app --reload --port 8000
````

The application will be available at:

```text
http://127.0.0.1:8000
```

FastAPI automatically provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method  | Endpoint                                | Purpose                                                                            |
| ------- | --------------------------------------- | ---------------------------------------------------------------------------------- |
| `GET`   | `/health`                               | Checks whether the API is running and healthy.                                     |
| `POST`  | `/transactions`                         | Creates a new transaction with validation for the account ID, amount and currency. |
| `GET`   | `/transactions`                         | Returns all transactions currently stored by the API.                              |
| `GET`   | `/transactions?account_id={account_id}` | Returns transactions filtered by a specific account ID.                            |
| `GET`   | `/transactions/{transaction_id}`        | Retrieves a single transaction using its unique transaction ID.                    |
| `PATCH` | `/transactions/{transaction_id}/status` | Updates an existing transaction status to either `approved` or `rejected`.         |

## Request Tracing

The API includes middleware that generates a unique `X-Request-ID` for every request.

The request ID is returned in the response headers and can be used to trace requests across services in a distributed architecture.

## Transaction Validation

The API uses Pydantic to validate incoming transaction data.

A transaction requires:

* A valid `account_id`
* An `amount` greater than zero
* An amount that does not exceed the FinTrust single-transaction limit
* A three-letter uppercase currency code
* An optional transaction description

Example transaction request:

```json
{
  "account_id": "ACC-001",
  "amount": 500.00,
  "currency": "ZAR",
  "description": "Payment to merchant"
}
```

New transactions are created with a `pending` status.

## Notes

Transactions are currently stored in memory for the purpose of this API exercise. This means the stored transactions are cleared when the application is restarted.

The application focuses on the FastAPI concepts covered during Week 7, including routing, request handling, Pydantic validation, transaction retrieval, status updates and request tracing.