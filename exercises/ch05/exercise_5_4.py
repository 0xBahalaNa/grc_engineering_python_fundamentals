mfa_enabled = True
mfa_type = "phishing_resistant"  # options: "phishing_resistant", "sms", "email", "none"
cji_access = True

if cji_access == True and mfa_enabled == False:
    print("CRITICAL: CJI access without MFA violates CJIS IA-2")
elif mfa_enabled == True and (mfa_type == "sms" or mfa_type == "email"):
    print("WARNING: MFA type does not meet AAL2 requirement")
elif mfa_enabled == True and mfa_type == "phishing_resistant":
    print("PASS: AAL2 MFA requirement satisfied")
elif cji_access == False:
    print("N/A: No CJI access, MFA check not required")
