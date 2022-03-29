# Tegoine

With Tegoine you can find if an AWS resource was created with a CloudFormation stack or not. It is useful when you need to identify it the resource is created outside CloudFormation.


Example:

export AWS_DEFAULT_REGION=eu-west-1

% python3 tegoine.py vpc-094d08dc24396856456gdf5654e
found vpc-094d08dc24396856456gdf5654e on stack: vpc-tegoine

