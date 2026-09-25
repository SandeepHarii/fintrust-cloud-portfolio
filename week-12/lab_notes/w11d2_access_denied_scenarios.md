# Access Denied Scenarios

## SCP-001: GuardDuty Detector

The Access Denied occurs because an explicit Deny is being applied by an AWS Organizations Service Control Policy (SCP). The account administrator's IAM permissions do not override an explicit SCP Deny, so the effective permissions remain restricted. The appropriate fix is to review the effective SCPs attached to the account and determine whether the GuardDuty protection restriction is intentional. If the action is required and approved, the SCP must be changed by an authorized organization administrator.

## IAM-002: S3 Object Deletion

The IAM identity policy allows `s3:DeleteObject`, but the S3 bucket policy contains an explicit Deny for delete operations in the affected environment. The resource policy therefore prevents the delete operation even though the identity policy contains an Allow. The appropriate fix is to review the bucket policy and remove or modify the explicit Deny if the deletion is authorized for that environment.

## PB-003: IAM Role Creation

The Admin role has `AdministratorAccess`, but a permission boundary is restricting the effective permissions available to the role. Because `iam:CreateRole` is not permitted by the permission boundary, the identity policy's AdministratorAccess does not make the action effective. The appropriate fix is to update or replace the permission boundary so that `iam:CreateRole` is included, subject to the organization's security requirements.