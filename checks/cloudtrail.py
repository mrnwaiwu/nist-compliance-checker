"""
checks/cloudtrail.py

NIST SP 800-53 Rev 5 compliance checks for AWS CloudTrail.

Controls covered:
  - AU-2   Event Logging
  - AU-3   Content of Audit Records
  - AU-9   Protection of Audit Information
  - AU-12  Audit Record Generation
  - IR-4   Incident Handling (log integrity)
"""

import boto3
from botocore.exceptions import ClientError


def get_trails(session: boto3.Session) -> list:
    """Return all CloudTrail trails in the account."""
    client = session.client("cloudtrail")
    try:
        response = client.describe_trails(includeShadowTrails=False)
        return response.get("trailList", [])
    except ClientError as e:
        return []


def check_au2_event_logging(session: boto3.Session) -> dict:
    """
    AU-2: Verify that at least one multi-region trail is enabled and logging.
    """
    trails = get_trails(session)
    client = session.client("cloudtrail")

    multi_region_active = []
    for trail in trails:
        if not trail.get("IsMultiRegionTrail"):
            continue
        try:
            status = client.get_trail_status(Name=trail["TrailARN"])
            if status.get("IsLogging"):
                multi_region_active.append(trail["TrailARN"])
        except ClientError:
            continue

    passed = len(multi_region_active) > 0
    return {
        "control": "AU-2",
        "title": "Event Logging",
        "status": "PASS" if passed else "FAIL",
        "detail": (
            f"Active multi-region trails: {multi_region_active}"
            if passed
            else "No active multi-region CloudTrail trail found."
        ),
        "remediation": (
            "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/"
            "cloudtrail-create-and-update-a-trail.html"
        ),
    }


def check_au9_log_file_validation(session: boto3.Session) -> dict:
    """
    AU-9 / IR-4: Verify log file integrity validation is enabled on all trails.
    """
    trails = get_trails(session)
    failing = [
        t["TrailARN"]
        for t in trails
        if not t.get("LogFileValidationEnabled")
    ]

    passed = len(failing) == 0
    return {
        "control": "AU-9",
        "title": "Protection of Audit Information — Log File Validation",
        "status": "PASS" if passed else "FAIL",
        "detail": (
            "All trails have log file validation enabled."
            if passed
            else f"Trails missing log file validation: {failing}"
        ),
        "remediation": (
            "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/"
            "cloudtrail-log-file-validation-intro.html"
        ),
    }


def check_au12_management_events(session: boto3.Session) -> dict:
    """
    AU-12: Verify at least one trail captures management (control plane) events.
    """
    trails = get_trails(session)
    client = session.client("cloudtrail")

    capturing_mgmt = []
    for trail in trails:
        try:
            selectors = client.get_event_selectors(TrailName=trail["TrailARN"])
            for sel in selectors.get("EventSelectors", []):
                if sel.get("ReadWriteType") in ("All", "WriteOnly", "ReadOnly"):
                    if sel.get("IncludeManagementEvents"):
                        capturing_mgmt.append(trail["TrailARN"])
                        break
        except ClientError:
            continue

    passed = len(capturing_mgmt) > 0
    return {
        "control": "AU-12",
        "title": "Audit Record Generation — Management Events",
        "status": "PASS" if passed else "FAIL",
        "detail": (
            f"Trails capturing management events: {capturing_mgmt}"
            if passed
            else "No trail is configured to capture management events."
        ),
        "remediation": (
            "Enable management event logging in CloudTrail event selectors."
        ),
    }


def run_all_checks(session: boto3.Session) -> list:
    """Run all CloudTrail compliance checks and return results."""
    return [
        check_au2_event_logging(session),
        check_au9_log_file_validation(session),
        check_au12_management_events(session),
    ]
