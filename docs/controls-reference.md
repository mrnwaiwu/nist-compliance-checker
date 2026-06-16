# Implemented Controls Reference

This document maps each implemented check to its NIST SP 800-53 Rev. 5
control and explains what the scanner evaluates in an AWS environment.

| Control | Name | What the check evaluates |
|---------|------|--------------------------|
| AC-2 | Account Management | Flags stale IAM users with no recent activity |
| AC-3 | Access Enforcement | Reviews IAM policies for overly broad permissions |
| AU-2 | Event Logging | Confirms CloudTrail is enabled in all regions |
| AU-9 | Protection of Audit Information | Checks CloudWatch log group retention settings |
| CM-6 | Configuration Settings | Detects insecure default configurations |
| CP-9 | Information System Backup | Validates RDS automated backup retention policy |
| IA-5 | Authenticator Management | Verifies password policy and key rotation age |
| IR-4 | Incident Handling | Validates CloudTrail log file integrity |
| RA-5 | Vulnerability Scanning | Checks Inspector scan age and critical findings |
| SC-7 | Boundary Protection | Flags open (0.0.0.0/0) security group rules |
| SI-2 | Flaw Remediation | Reports unpatched managed resources |
| SI-4 | Information System Monitoring | Confirms GuardDuty detector is active |

## Reading the report

Each finding includes a pass/fail status, the control reference, and a
short remediation note. Failures are grouped by control family so teams
can route them to the right owner.

## Adding a new check

1. Add a check function under `controls/`.
2. Register it in the control mapping table.
3. Add a test fixture covering both pass and fail cases.

See `CHANGELOG.md` for the history of added controls.
