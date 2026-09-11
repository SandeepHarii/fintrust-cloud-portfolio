CREATE OR REPLACE VIEW v_transfer_audit AS
SELECT
    v.volume_name,
    c.regulation,
    c.encryption_required,
    e.status AS execution_status,
    e.bytes_transferred,
    e.completed_at
FROM datasync_executions e
JOIN transfer_volumes v
    ON e.task_id = v.volume_id
JOIN compliance_requirements c
    ON v.volume_id = c.volume_id;