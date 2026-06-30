# Changelog

## [Unreleased]
- Planned: HTML report export
- Planned: multi-system batch scan support

## [1.8.0] - 2026-06-30
- Added AT-2 Security Awareness Training check to validate training completion records within the past 12 months
- Added MP-6 Media Sanitization check for verification that decommissioned storage volumes are wiped before disposal
- Improved control runner to surface skipped controls with a reason when required AWS permissions are absent
- Updated OSCAL catalog references to align with NIST SP 800-53 Rev 5 errata release (June 2026)

## [1.7.0] - 2026-06-26
- Added PL-8 Information Security Architecture check for network segmentation documentation coverage
- Added SC-28 Protection of Information at Rest check for RDS and S3 encryption compliance
- Improved finding output to include CVE references where applicable for vulnerability-related controls
- Added `--output-dir` flag to direct report files to a configurable directory

## [1.6.0] - 2026-06-22
- Added CA-7 Continuous Monitoring check for stale vulnerability scan results older than 30 days
- Added AC-6 Least Privilege check for IAM policies granting wildcard ("*") actions
- Improved batch scan mode to report per-control execution time for performance tuning
- Updated remediation priority ratings to factor in exploit availability from the CISA KEV catalog

## [1.5.0] - 2026-06-19
- Added SA-9 External Information System Services check for third-party integration compliance scope
- Added PM-6 Information Security Measures of Performance check for metric tracking coverage
- Improved control output to include remediation priority ratings (Critical, High, Medium, Low)
- Added batch scan mode to run all controls in parallel for faster environment assessments
- Updated NIST SP 800-53 Rev 5 control descriptions with latest OSCAL catalog references

## [1.4.0] - 2026-06-08
- Added RA-5 Vulnerability Scanning check for Inspector scan age and unresolved critical findings
- Added CP-9 Information System Backup check for RDS automated backup retention policy
- Improved control output formatting with remediation guidance links per finding
- Refactored report writer to support pluggable output formats (JSON, text, future HTML)

## [1.3.0] - 2026-06-05
- Added IR-4 Incident Handling check for CloudTrail log integrity validation
- Added SI-4 Information System Monitoring check for GuardDuty detector status
- Improved control output to include NIST 800-53 revision 5 references

## [1.2.0] - 2026-06-02
- Added CM-6 Configuration Settings check for insecure default configurations
- Added AU-9 Protection of Audit Information check for CloudWatch log group retention
- Improved report output to include control descriptions alongside pass/fail status

## [1.1.0] - 2026-05-30
- Added SC-7 Boundary Protection check for open security group rules
- Improved AC-2 account management check to flag stale IAM users
- Refactored control mapping into separate controls/ module for easier extension

## [1.0.0] - 2026-05-20
- Initial release
- NIST SP 800-53 compliance checks for AWS environments
- Pass/fail JSON report output
- Checks for AC-2, AC-3, AU-2, IA-5, SC-7, SI-2 controls
