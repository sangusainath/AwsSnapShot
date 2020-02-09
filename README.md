# AwsSnapShot
Project to manage AWS EC2 Instances

##About

This project uses boto3 to manage AWS EC2 instance snapshots

## Configuation

snapshotuser uses the configuation file created by AWS CLI
Example:

`aws configure --profile snapshotuser`

##Running

`pipenv run python snapshotuser/snapshotuser.py <commad> <subcommand>
<--project=PROJECT>`

*command*
is instances, volumes, or snapshots
*subcommand* - depends in command
*project* is optional
