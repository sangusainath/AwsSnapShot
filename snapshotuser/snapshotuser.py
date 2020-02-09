import boto3
import click

session=boto3.Session(profile_name='snapshotuser')
ec2 =session.resource('ec2')

def filter_instances(project):
        instances=[]

        if project:
            filters = [{'Name':'tag:Project','Values':[project]}]
            instances=ec2.instances.filter(Filters=filters)
        else:
            instances=ec2.instances.all()

        return instances
@click.group()
def cli():
    """snapshotuser manages EC2 instances and snapshots"""

@cli.group('snapshot')
def snapshot():
    """Commands for Snapshots"""
@snapshot.command('list')
@click.option('--project',default=None,
    help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    "To List of EC2 Volume's snapshots"
    instances=filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print(",".join((
                s.id,
                v.id,
                i.id,
                s.state,
                s.progress,
                s.start_time.strftime("%c")
                )))
    return


@cli.group('volumes')
def volumes():
    """Commands for Volumes"""

@volumes.command('list')
@click.option('--project',default=None,
    help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    "To List of EC2 Volumes"

    instances=filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            print(",".join((
                v.id,
                i.id,
                v.state,
                str(v.size)+"GiB",
                v.encrypted and "Encrypted" or "Not Encrypted"
            )))
    return


@cli.group('instances')
def instances():
    """Commands for instances"""

@instances.command('snapshots',
    help="Create snapshots for all volumes")
@click.option('--project',default=None,
    help="Only instances for project (tag Project:<name>)")
def create_snapshots(project):
    "Crate snapshots for EC2 Instances"

    instances = filter_instances(project)

    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
        i.wait_until_stopped()
        for v in i.volumes.all():
            print("Creating snapshot for {0} Instance and {1} Volume".format(i.id,v.id))
            v.create_snapshot(Description="Created by SnapshotUser")
        print("Starting {0}...".format(i.id))
        i.start()
        i.wait_until_running()

    print("Job Completed!!!")

    return


@instances.command('list')
@click.option('--project',default=None,
    help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    "To List of EC2 Instances"

    instances=filter_instances(project)

    for i in instances:
        tags={t['Key']:t['Value'] for t in i.tags or []}
        print(','.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project','<no project>'))))

    return
@instances.command('stop')
@click.option('--project',default=None,
    help='Only instances for project')
def stop_instances(project):
    "To Stop EC2 Instances"

    instances=filter_instances(project)

    for i in instances:
        print("Stopping {0} instance...".format(i.id))
        i.stop()

    return

@instances.command('start')
@click.option('--project',default=None,
    help='Only instances for project')
def stop_instances(project):
    "To Start EC2 Instances"

    instances=filter_instances(project)

    for i in instances:
        print("Starting {0} instance...".format(i.id))
        i.start()

    return

if __name__ == '__main__':
    cli()
