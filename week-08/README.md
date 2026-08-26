## Kinesis Partition Key Strategy

The FinTrust transaction stream uses `account_id` as the Kinesis partition key.

Using `account_id` ensures that all transactions belonging to the same customer are routed to the same shard.

This guarantees ordering for transactions associated with that account because records with the same partition key are always processed within the same shard.

This ordering is important for fraud detection, transaction auditing, and customer activity analysis because events are processed in the sequence in which they occur.