from setuptools import setup


setup(
    name='snapshot_analyzer',
    version='0.1',
    author='sainath sangu',
    author_email='sainath.sangu@gmail.com',
    description='SnapshotAnalyzer is tool to mangage AWS EC2 snapshots automatically from CLI',
    license='GPLv3+',
    packages=['snapshotuser'],
    url='https://github.com/sangusainath/AwsSnapShot',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        snapshotuser=snapshotuser.snapshotuser:cli
    ''',
)
