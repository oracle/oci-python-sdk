# Database Tools Examples

## Introduction
We show 3 Use Cases for the Database Tools Service

## Use Cases
- ADB-S with Public IP
- ADB-S with Private Endpoint
- Bare Metal, VM and Exadata with Private IP

## ADB-S with Public IP
![](images/ADB-S.with.Public.IP.png)
### Example
See: **adbs_create_connection_public_ip.py** where we:
1. Create a new Autonomous Database
2. Create required secrets
3. Create a connection
4. Validate the connection

## ADB-S with Private Endpoint
![](images/ADB-S.with.Private.Endpoint.png)
### Example
See: **adbs_create_connection_with_pe.py** where we:
1. Create a Database Tools Private Endpoint for a Reverse Connection to the Private Endpoint of an ADB-S
2. Create required secrets
3. Create a connection
4. Validate the connection

## Bare Metal, DB System and Exadata with Private IP
![](images/Bare.Metal.VM.Exadata.with.Private.IP.png)
### Example
See: **db_system_create_connection_private_subnet.py** where we:
1. Create a Database Tools Private Endpoint for a Reverse Connection to a VM DB System
2. Create required secrets
3. Create a connection
4. Validate the connection