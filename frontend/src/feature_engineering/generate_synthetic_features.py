import pandas as pd
import random

# Load original dataset
data = pd.read_csv(
    r"data/raw/ISTM.csv",
    low_memory=False
)

# -----------------------------
# REGION GENERATION
# -----------------------------

data['Region'] = random.choices(
    ['APAC', 'EMEA', 'NAM', 'LATAM'],
    weights=[40, 25, 25, 10],
    k=len(data)
)

# -----------------------------
# NETWORK TYPE GENERATION
# -----------------------------

network_types = [
    '5G Network',
    'Core Network',
    'Wireless Network',
    'VPN Service',
    'Mobile Core',
    'Fiber Network'
]

data['Network_Type'] = [
    random.choice(network_types)
    for _ in range(len(data))
]

# -----------------------------
# LINGUISTICALLY DIVERSE
# INCIDENT DESCRIPTIONS
# -----------------------------

incident_descriptions = [
    "Tower node experiencing signal degradation",
    "Unexpected packet loss detected in network",
    "Wireless transmission instability observed",
    "Network latency spike affecting enterprise users",
    "Intermittent connectivity disruption in telecom node",
    "Core router experiencing abnormal traffic congestion",
    "Repeated signal attenuation detected in mobile tower",
    "5G infrastructure showing unstable packet delivery",
    "Network outage impacting regional operations",
    "VPN tunnel experiencing connectivity interruptions"
]

request_info_descriptions = [
    "Information requested for access permissions",
    "Need clarification regarding network configuration",
    "Requested details for VPN access setup",
    "Inquiry raised regarding telecom maintenance window",
    "User requested operational status update",
    "Clarification needed for network routing policies",
    "Requested guidance for wireless service activation",
    "Information requested about firewall configuration",
    "Status inquiry raised for telecom infrastructure",
    "Need details regarding connectivity provisioning"
]

complaint_descriptions = [
    "Customer reported repeated connection drops",
    "User unhappy with delayed issue resolution",
    "Client reported unstable network performance",
    "Frequent service interruptions affecting customer operations",
    "Customer experiencing recurring wireless disruptions"
]

change_descriptions = [
    "Request submitted for router configuration update",
    "Infrastructure upgrade requested for telecom node",
    "Firewall rule modification requested by operations team",
    "Change request raised for 5G deployment settings",
    "Network optimization request submitted"
]

# -----------------------------
# DESCRIPTION GENERATOR
# -----------------------------

def generate_description(category):

    if category == 'incident':
        return random.choice(incident_descriptions)

    elif category == 'request for information':
        return random.choice(request_info_descriptions)

    elif category == 'complaint':
        return random.choice(complaint_descriptions)

    elif category == 'request for change':
        return random.choice(change_descriptions)

    else:
        return "General telecom operational issue reported"

# Generate synthetic descriptions
data['Incident Description'] = data['Category'].apply(
    generate_description
)

# -----------------------------
# WAS_REOPENED FLAG
# -----------------------------

data['Was_Reopened'] = data['Reopen_Time'].notnull().astype(int)

# -----------------------------
# DROP UNUSED COLUMNS
# -----------------------------

columns_to_drop = [
    'WBS',
    'number_cnt',
    'KB_number',
    'Related_Interaction',
    'Related_Change'
]

data.drop(
    columns=columns_to_drop,
    inplace=True,
    errors='ignore'
)

# -----------------------------
# SAVE FINAL DATASET
# -----------------------------

data.to_csv(
    r"data/processed/final_istm_data.csv",
    index=False
)

print("\nFinal synthetic telecom dataset created successfully.")
print("\nDataset Shape:", data.shape)

# Display full text properly
pd.set_option('display.max_colwidth', None)

print("\nSample Incident Descriptions:\n")

print(
    data[
        ['Category', 'Incident Description']
    ].head(10)
)