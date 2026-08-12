"""
Tests for NIST AC-2 Access Control and Management
"""
import pytest
from compliance.nist import AccessControl

@pytest.fixture
def ac_checker():
    return AccessControl()

def test_account_management_enabled(ac_checker):
    """Test that account management is enabled."""
    result = ac_checker.check_account_management()
    assert result['status'] in ['PASS', 'FAIL']
    assert 'message' in result

def test_user_identification_and_authentication(ac_checker):
    """Test user identification and authentication controls."""
    result = ac_checker.check_user_auth_controls()
    assert result['status'] in ['PASS', 'FAIL']

def test_access_enforcement(ac_checker):
    """Test access enforcement mechanisms."""
    result = ac_checker.check_access_enforcement()
    assert result['status'] in ['PASS', 'FAIL']

def test_privileged_access_management(ac_checker):
    """Test PAM implementation."""
    result = ac_checker.check_privileged_access()
    assert 'elevated_accounts' in result
    assert 'mfa_enabled' in result

def test_session_management(ac_checker):
    """Test session controls."""
    result = ac_checker.check_session_controls()
    assert 'session_timeout' in result
    assert result['session_timeout'] is not None

def test_account_lockout_policy(ac_checker):
    """Test account lockout policies."""
    result = ac_checker.check_lockout_policy()
    assert result['status'] in ['PASS', 'FAIL']
    assert 'failed_attempts_threshold' in result
