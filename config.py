# Configuration file for Discord Anti-Raid Bot

# Raid Detection Settings
RAID_JOIN_THRESHOLD = 10  # Number of joins to trigger raid detection
RAID_JOIN_THRESHOLD_SECONDS = 30  # Time window in seconds

# Spam Detection Settings
SPAM_MESSAGE_THRESHOLD = 5  # Number of messages to trigger spam detection
SPAM_CHECK_SECONDS = 10  # Time window for checking messages in seconds
MUTE_DURATION_SECONDS = 300  # How long to mute a user (5 minutes)

# Optional: Whitelist for trusted users or bots
WHITELIST_IDS = []  # Add user IDs to bypass spam detection