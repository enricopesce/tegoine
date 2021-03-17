import sys
import boto3


stack_names = []
argument = sys.argv[1]

client = boto3.client('cloudformation')
paginator = client.get_paginator('list_stacks')
response_iterator = paginator.paginate(StackStatusFilter=[
        'CREATE_IN_PROGRESS',
        'CREATE_FAILED',
        'CREATE_COMPLETE',
        'ROLLBACK_IN_PROGRESS',
        'ROLLBACK_FAILED',
        'ROLLBACK_COMPLETE',
        'UPDATE_IN_PROGRESS',
        'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS',
        'UPDATE_COMPLETE',
        'UPDATE_ROLLBACK_IN_PROGRESS',
        'UPDATE_ROLLBACK_FAILED',
        'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS',
        'UPDATE_ROLLBACK_COMPLETE',
        'REVIEW_IN_PROGRESS',
        'IMPORT_IN_PROGRESS',
        'IMPORT_COMPLETE',
        'IMPORT_ROLLBACK_IN_PROGRESS',
        'IMPORT_ROLLBACK_FAILED',
        'IMPORT_ROLLBACK_COMPLETE'
    ])

for page in response_iterator:
    stack = page['StackSummaries']
    for output in stack:
        stack_names.append(output['StackName'])

for stack_name in stack_names:
    paginator = client.get_paginator('list_stack_resources')
    response_iterator = paginator.paginate(StackName=stack_name)
    try:
        for page in response_iterator:
            for resource in page['StackResourceSummaries']:
                phisical_name = resource['PhysicalResourceId']
                if argument in phisical_name:
                    print("found " + phisical_name + " on stack: " + stack_name)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
