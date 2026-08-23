from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator


app = FastAPI(
    title="FinTrust Transaction API",
    version="1.0.0",
    description="A simple transaction API built with FastAPI for the FinTrust banking environment."
)


# In-memory transaction storage.
# This can later be replaced with a database or AWS service.
transactions: list[dict] = []


class TransactionIn(BaseModel):
    account_id: str = Field(
        ...,
        min_length=1,
        description="Account identifier"
    )

    amount: float = Field(
        ...,
        gt=0,
        description="Transaction amount. Must be greater than zero."
    )

    currency: str = Field(
        ...,
        pattern=r"^[A-Z]{3}$",
        description="Three-letter uppercase ISO 4217 currency code"
    )

    description: Optional[str] = None

    @field_validator("amount")
    @classmethod
    def amount_max(cls, value: float) -> float:
        if value > 1_000_000:
            raise ValueError(
                "Amount exceeds single-transaction limit of 1,000,000"
            )
        return value


class TransactionOut(TransactionIn):
    id: str
    status: str
    created_at: str


class TransactionStatusUpdate(BaseModel):
    status: str = Field(
        ...,
        description="Transaction status. Must be approved or rejected."
    )

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        allowed_statuses = {"approved", "rejected"}

        if value.lower() not in allowed_statuses:
            raise ValueError(
                "Status must be either 'approved' or 'rejected'"
            )

        return value.lower()


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid4())

    response = await call_next(request)

    response.headers["X-Request-ID"] = request_id

    return response


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }


@app.post(
    "/transactions",
    response_model=TransactionOut,
    status_code=201
)
async def create_transaction(body: TransactionIn):
    transaction = {
        "id": str(uuid4()),
        **body.model_dump(),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    transactions.append(transaction)

    return transaction


@app.get(
    "/transactions",
    response_model=list[TransactionOut]
)
async def list_transactions(
    account_id: Optional[str] = Query(
        default=None,
        description="Optional account ID used to filter transactions"
    )
):
    if account_id:
        return [
            transaction
            for transaction in transactions
            if transaction["account_id"] == account_id
        ]

    return transactions


@app.get(
    "/transactions/{transaction_id}",
    response_model=TransactionOut
)
async def get_transaction(transaction_id: str):
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return transaction

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )


@app.patch(
    "/transactions/{transaction_id}/status",
    response_model=TransactionOut
)
async def update_transaction_status(
    transaction_id: str,
    body: TransactionStatusUpdate
):
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transaction["status"] = body.status
            return transaction

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )