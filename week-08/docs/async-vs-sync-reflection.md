# Reflection: Sync vs Async APIs

Athena uses an asynchronous execution model. When a query is submitted, Athena immediately returns a QueryExecutionId while the query continues running in the background. The application must repeatedly check the status until the query reaches a completed state.

Glue API operations such as get_databases() and get_tables() are synchronous because the results can be returned immediately.

Another AWS service that uses an asynchronous pattern is Amazon EMR. When an EMR cluster is created, AWS returns a cluster identifier immediately while the cluster continues provisioning in the background. The client must monitor the cluster state until it becomes available.

Synchronous execution would be impractical for services such as Athena and EMR because large datasets may take several minutes or even hours to process. Holding an HTTP connection open for the entire operation would be inefficient and more likely to time out.