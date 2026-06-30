# OSCAL Catalog Mapping Reference

This document maps the controls implemented in `nist-compliance-checker` to their corresponding entries in the NIST SP 800-53 Rev 5 OSCAL catalog.

## What Is OSCAL?

The Open Security Controls Assessment Language (OSCAL) is a set of machine-readable formats developed by NIST for representing security controls, assessments, and system security plans. The checker uses OSCAL catalog references to link each finding back to the authoritative control definition.

## Implemented Controls

| Control ID | Control Name | OSCAL UUID (Rev 5) | Checker Module |
|------------|--------------|-------------------|----------------|
| AC-2  | Account Management | `ac-2` | `controls/access.py` |
| AC-3  | Access Enforcement | `ac-3` | `controls/access.py` |
| AC-6  | Least Privilege | `ac-6` | `controls/access.py` |
| AU-2  | Event Logging | `au-2` | `controls/audit.py` |
| AU-9  | Protection of Audit Information | `au-9` | `controls/audit.py` |
| AT-2  | Security Awareness Training | `at-2` | `controls/awareness.py` |
| CA-7  | Continuous Monitoring | `ca-7` | `controls/assessment.py` |
| CM-6  | Configuration Settings | `cm-6` | `controls/config.py` |
| CP-9  | Information System Backup | `cp-9` | `controls/contingency.py` |
| IA-5  | Authenticator Management | `ia-5` | `controls/identity.py` |
| IR-4  | Incident Handling | `ir-4` | `controls/incident.py` |
| MP-6  | Media Sanitization | `mp-6` | `controls/media.py` |
| PL-8  | Information Security Architecture | `pl-8` | `controls/planning.py` |
| PM-6  | Information Security Measures | `pm-6` | `controls/program.py` |
| RA-5  | Vulnerability Scanning | `ra-5` | `controls/risk.py` |
| SA-9  | External System Services | `sa-9` | `controls/acquisition.py` |
| SC-7  | Boundary Protection | `sc-7` | `controls/system.py` |
| SC-28 | Protection of Info at Rest | `sc-28` | `controls/system.py` |
| SI-2  | Flaw Remediation | `si-2` | `controls/integrity.py` |
| SI-4  | Information System Monitoring | `si-4` | `controls/integrity.py` |

## OSCAL References in Output

Each finding in the JSON report includes an `oscal_ref` field:

```json
{
  "control_id": "AC-6",
  "title": "Least Privilege",
  "status": "FAIL",
  "finding": "IAM policy arn:aws:iam::123456789012:policy/DevAccess grants wildcard (*) actions on all resources.",
  "remediation": "Scope IAM policies to the minimum required actions and resources.",
  "oscal_ref": "https://csrc.nist.gov/extensions/oscal/sp800-53-rev5/ac/ac-6",
  "severity": "High"
}
```

## Updating OSCAL References

NIST publishes updated OSCAL catalog files at:
- https://github.com/usnistgov/OSCAL/tree/main/content/nist.gov/SP800-53/rev5

When NIST releases errata, update the catalog pin in `config/oscal_catalog.yaml`:

```yaml
oscal_catalog:
  source: nist-sp800-53-rev5
  version: "5.1.1"
  errata_date: "2026-06"
  url: "https://csrc.nist.gov/projects/oscal"
```

Then run `python -m tools.validate_oscal_refs` to confirm all control IDs resolve correctly.
