# Week 10 Reflection

## What I Learned

This week focused on AWS migration, data transfer, and cost optimisation. The biggest takeaway for me was that migration is not simply about moving an existing workload into AWS. The migration approach needs to be selected based on the workload, its requirements, technical limitations, and the amount of change that makes sense.

The AWS 6Rs framework gave me a structured way to think about these decisions. Rehosting can be useful when speed and minimal changes are important, while replatforming or refactoring can provide greater long-term benefits when a workload is suitable for cloud-native services.

I also learned how AWS DMS and AWS DataSync address different migration requirements. DMS is focused on database migration and replication, while DataSync is designed for transferring larger amounts of data between storage environments. Cost also needs to be considered when choosing how data should be transferred, particularly when dealing with large volumes.

## Practical Experience

The practical part of the week allowed me to apply these concepts through the `fintrust_migration` Python package. I organised migration functionality into separate modules for DMS, DataSync, S3, workload classification, and shared AWS session handling.

This helped me understand how migration automation can be structured rather than putting all functionality into one script. The package also provides a foundation for extending the FinTrust architecture with migration-specific tooling.

## Challenges

One of the main challenges was understanding how the different AWS migration services fit together. DMS, DataSync, S3, and other transfer options solve different problems, so selecting the appropriate service requires understanding the type and scale of data being moved.

Another challenge was translating the migration concepts into a practical architecture rather than treating each AWS service as an isolated topic.

## What I Would Improve

I would like to spend more time working with real migration scenarios where the workload characteristics are known and I can make and justify an actual 6R decision. I would also like to gain more hands-on experience with DMS and DataSync in a controlled AWS environment.

## Overall Reflection

Week 10 helped connect AWS infrastructure knowledge with a broader view of cloud migration. I now have a clearer understanding of how migration strategy, data movement, automation, monitoring, and cost considerations need to work together.

The work also extended FinTrust beyond simply running an application in the cloud and introduced the migration planning and automation layer needed when moving existing workloads into an AWS environment.