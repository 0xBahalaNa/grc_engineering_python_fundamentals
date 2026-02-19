finding_controls = ["AC-2", "AC-6", "IA-2", "AC-2", "SC-28", "AU-6",
                    "AC-2", "IA-2", "SC-7", "AU-2", "AC-6", "IA-5"]

finding_count = {}

for finding_control in finding_controls:
    finding_count[finding_control] = finding_count.get(finding_control, 0) + 1

print(finding_count)

max_control = max(finding_count, key=finding_count.get)
print(f"\nMost findings: {max_control} ({finding_count[max_control]})")

sorted_controls = sorted(finding_count, key=finding_count.get, reverse=True)

for control in sorted_controls:
    print(f"    {control}: {finding_count[control]}")
