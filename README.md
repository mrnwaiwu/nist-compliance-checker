# nist-compliance-checker

Python tool that runs automated checks against key NIST SP 800-53 security controls and outputs a pass/fail compliance report.

## Controls Checked
| Control | Name |
|---------|------|
| AC-2 / IA-5 | Password Policy |
| AU-2 | Audit Logging |
| SC-28 | Disk Encryption |
| SI-2 | OS Patching |

## Setup
```bash
python checker.py
```
No dependencies required — uses Python standard library only.

## Output
- Color-coded terminal report
- `compliance_report.json` saved locally

## Tech Stack
Python · subprocess · JSON · NIST SP 800-53
