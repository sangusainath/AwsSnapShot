# AwsSnapShot
Project to manage AWS EC2 Instances

##About

This project uses boto3 to manage AWS EC2 instance snapshots

## Configuation

snapshotuser uses the configuation file created by AWS CLI
Example:

`aws configure --profile snapshotuser`

##Running

`pipenv run python snapshotuser/snapshotuser.py
<--project=PROJECT>`

*command*
list: To List EC2 Instances
start: To Start EC2 Instances
stop: To Stop EC2 Instances

*project* is optional
