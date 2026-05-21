"""
nist-compliance-checker
------------------------
Checks a target system's config against key NIST SP 800-53 controls.
Runs a series of checks and outputs a compliance report.
"""

import subprocess
import platform
import json
from datetime import datetime


def check_password_policy() -> dict:
    result = {"control": "AC-2 / IA-5", "name": "Password Policy"}
    try:
        if platform.system() == "Linux":
            out = subprocess.check_output(["cat", "/etc/login.defs"], text=True)
            result["status"] = "PASS" if "PASS_MIN_LEN" in out else "FAIL"
            result["detail"] = "Password min length policy found." if result["status"] == "PASS" else "No PASS_MIN_LEN in /etc/login.defs"
        else:
            result["status"] = "MANUAL"
            result["detail"] = "Run on Linux to auto-check. Verify password policy manually."
    except Exception as e:
        result["status"] = "ERROR"
        result["detail"] = str(e)
    return result


def check_audit_logging() -> dict:
    result = {"control": "AU-2", "name": "Audit Logging"}
    try:
        out = subprocess.check_output(["pgrep", "auditd"], text=True)
        result["status"] = "PASS"
        result["detail"] = f"auditd running (PID {out.strip()})"
    except subprocess.CalledProcessError:
        result["status"] = "FAIL"
        result["detail"] = "auditd not running. Enable with: sudo systemctl start auditd"
    except FileNotFoundError:
        result["status"] = "MANUAL"
        result["detail"] = "pgrep not available. Verify audit logging manually."
    return result


def check_disk_encryption() -> dict:
    result = {"control": "SC-28", "name": "Disk Encryption"}
    try:
        if platform.system() == "Linux":
            out = subprocess.check_output(["lsblk", "-o", "NAME,TYPE"], text=True)
            result["status"] = "PASS" if "crypt" in out else "FAIL"
            result["detail"] = "Encrypted volume found." if result["status"] == "PASS" else "No encrypted volumes detected."
        else:
            result["status"] = "MANUAL"
            result["detail"] = "Verify FileVault (macOS) or BitLocker (Windows) is enabled."
    except Exception as e:
        result["status"] = "ERROR"
        result["detail"] = str(e)
    return result


def check_os_updates() -> dict:
    result = {"control": "SI-2", "name": "OS Patching"}
    try:
        if platform.system() == "Linux":
            out = subprocess.check_output(
                ["bash", "-c", "apt list --upgradable 2>/dev/null | wc -l"], text=True
            )
            count = int(out.strip()) - 1
            result["status"] = "PASS" if count == 0 else "FAIL"
            result["detail"] = f"{count} pending updates." if count > 0 else "System is up to date."
        else:
            result["status"] = "MANUAL"
            result["detail"] = "Check for updates manually via your OS update manager."
    except Exception as e:
        result["status"] = "ERROR"
        result["detail"] = str(e)
    return result


def run_checks() -> list:
    return [
        check_password_policy(),
        check_audit_logging(),
        check_disk_encryption(),
        check_os_updates(),
    ]


def print_report(results: list) -> None:
    print("\nNIST SP 800-53 Compliance Check Report")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"System: {platform.system()} {platform.release()}")
    print("=" * 60)

    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = sum(1 for r in results if r["status"] == "FAIL")
    manual = sum(1 for r in results if r["status"] in ("MANUAL", "ERROR"))

    for r in results:
        icon = {"PASS": "[PASS]", "FAIL": "[FAIL]", "MANUAL": "[MANUAL]", "ERROR": "[ERROR]"}.get(r["status"], "?")
        print(f"\n{icon} {r['control']} - {r['name']}")
        print(f"   {r['detail']}")

    print(f"\n{'='*60}")
    print(f"Summary: {passed} PASS | {failed} FAIL | {manual} MANUAL REVIEW")

    with open("compliance_report.json", "w") as f:
        json.dump({"timestamp": str(datetime.now()), "results": results}, f, indent=2)
    print("Full report saved to compliance_report.json")


if __name__ == "__main__":
    results = run_checks()
    print_report(results)
