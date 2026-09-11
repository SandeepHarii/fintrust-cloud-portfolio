CREATE OR REPLACE VIEW v_migration_audit AS
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS full_name,
    a.account_id,
    ms.source_system,
    ms.validation_state,
    ms.migrated_at
FROM migration_status ms
JOIN customers c
    ON ms.asset_id = c.customer_id
LEFT JOIN accounts a
    ON a.customer_id = c.customer_id;