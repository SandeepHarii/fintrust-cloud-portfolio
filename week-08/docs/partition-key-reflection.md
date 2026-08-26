# Partition Key Reflection

FinTrust uses `account_id` as the Kinesis partition key to preserve transaction ordering for each customer.

If one account generated 10,000 transactions in a short period, all records would be routed to the same shard. This could create a hot shard where one shard becomes overloaded while others remain underutilised.

An alternative approach would be to use a composite key such as:

account_id-timestamp

or

account_id-region

This would distribute traffic more evenly across shards.

However, doing so would sacrifice the guarantee that all transactions for a single account are processed in order, which may reduce the effectiveness of fraud detection and transaction analysis.