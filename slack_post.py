import json
import slack # module is called slackclient

# Local image taken from https://ccsearch.creativecommons.org/photos/a376def5-1f22-4e28-b2f0-8cf67398afa8

OATH = 'MY_OATH_TOKEN'

with open("block.json", "rt") as block_f:
    data = json.load(block_f)

client = slack.WebClient(token=OATH)

client.files_upload(
    channels="my-channel",
    file="slacks.jpg",
    title="Local File"
)
client.chat_postMessage(
    channel="my-channel",
    blocks=data
)
