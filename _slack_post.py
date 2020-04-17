import json
import slack # module is called slackclient

# Local image taken from https://ccsearch.creativecommons.org/photos/a376def5-1f22-4e28-b2f0-8cf67398afa8

# Load global config
with open("../network_config/slack.json") as slack_f:
    slack_settings = json.load(slack_f)

OATH = slack_settings["OAUTH_TOKEN"]
WEBHOOK_URL = slack_settings["WEBHOOK"]
USEWEBHOOK = slack_settings["USE_WEBHOOK"] # set 1 in ../network_config/slack.json if you can't use OATH (no graph though)
SLACKCHANNEL = slack_settings["CHANNEL"]

with open("blocks.json", "rt") as block_f:
    data = json.load(block_f)

client = slack.WebClient(token=OATH)

client.files_upload(
    channels=SLACKCHANNEL,
    file="slacks.jpg",
    title="Local File"
)
client.chat_postMessage(
    channel=SLACKCHANNEL,
    blocks=data
)
