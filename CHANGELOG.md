# Changelog

## [Unreleased]
- Planned: HTML report export
- Planned: multi-system batch scan support

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
