# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the Email Service in the Python SDK. This script accepts two
# will demonstrate:
#
#   * Creating, retrieving, moving, listing and deleting email senders
#   * Creating, retrieving, listing and deleting email suppressions
#   * Obtaining SMTP credentials for your IAM user so that you can send emails.
#     See https://docs.cloud.oracle.com/Content/Email/Tasks/configuresmtpconnection.htm for more
#     information on sending emails
#
# This script accepts four arguments:
#
#   * The compartment ID where email senders will be created
#   * The target compartment ID where email senders will be moved to
#   * The address of the email sender
#   * The address of the email suppression
#
# Note that email senders are created in the compartment which you specify, but the suppressions are always created at the tenancy
# level. The tenancy will be read from your configuration file.

import oci
import sys

# Default config file and profile
config = oci.config.from_file()
email_client = oci.email.EmailClient(config)
identity_client = oci.identity.IdentityClient(config)

if len(sys.argv) != 5:
    raise RuntimeError('This script expects an argument of a compartment OCID, a target compartment OCID, sender email address and suppression email address')

# The first argument is the name of the script, so start the index at 1
compartment_id = sys.argv[1]
target_compartment_id = sys.argv[2]
sender_address = sys.argv[3]
suppression_address = sys.argv[4]

create_sender_response = email_client.create_sender(
    oci.email.models.CreateSenderDetails(
        compartment_id=compartment_id,
        email_address=sender_address
    )
)
print('Created sender:\n{}'.format(create_sender_response.data))
print('\n=========================\n')

# A sender has a lifecycle state, so we can wait for it to become available
get_sender_response = oci.wait_until(email_client, email_client.get_sender(create_sender_response.data.id), 'lifecycle_state', 'ACTIVE')
print('Waited for sender to become available:\n{}'.format(get_sender_response.data))
print('\n=========================\n')

# change sender compartment
change_sender_response = email_client.change_sender_compartment(
    create_sender_response.data.id,
    oci.email.models.ChangeSenderCompartmentDetails(
        compartment_id=target_compartment_id
    )
)
print('Moved sender:\n{}'.format(create_sender_response.data.id))
print('\n=========================\n')

# We can list all senders, and also provide optional filters and sorts. Here we'll list all
# senders sorted by their email address, and also demonstrate filtering by sender email
# address (an exact match filter)
#
# Listing senders is a paginated operation, so we can use the functions in oci.pagination
senders = oci.pagination.list_call_get_all_results(
    email_client.list_senders,
    compartment_id,
    sort_by='EMAILADDRESS',
    sort_order='ASC'
).data
print('Listing senders sorted by email address:')
for s in senders:
    print(s)
print('\n=========================\n')

senders = oci.pagination.list_call_get_all_results(
    email_client.list_senders,
    compartment_id,
    email_address='fake-{}'.format(sender_address)
).data
print('Listing senders filtered by email address - no data expected:')
for s in senders:
    print(s)
print('\n=========================\n')

# Suppressions do not have a lifecycle state, so we don't have to wait on anything after creation
create_suppression_response = email_client.create_suppression(
    oci.email.models.CreateSuppressionDetails(
        compartment_id=config['tenancy'],
        email_address=suppression_address
    )
)
print('Created suppression:\n{}'.format(create_suppression_response.data))
print('\n=========================\n')

# We can list all suppressions, and also provide optional filters and sorts. Here we'll list all
# suppressions sorted by their time created, and also demonstrate filtering by suppression email
# address (an exact match filter)
#
# Listing senders is a paginated operation, so we can use the functions in oci.pagination
suppressions = oci.pagination.list_call_get_all_results(
    email_client.list_suppressions,
    config['tenancy'],
    sort_by='TIMECREATED',
    sort_order='DESC'
).data
print('Listing suppressions sorted by time created:')
for s in suppressions:
    print(s)
print('\n=========================\n')

suppressions = oci.pagination.list_call_get_all_results(
    email_client.list_suppressions,
    config['tenancy'],
    email_address='fake-{}'.format(suppression_address)
).data
print('Listing suppressions filtered by email address - no data expected:')
for s in suppressions:
    print(s)
print('\n=========================\n')

# We can also delete a sender and then wait for it to be deleted. The sender may already be deleted
# by the time we call oci.wait_until, so pass the get_sender_response to the waiter. It is recommended that
# you have a get response prior to calling the delete, INSTEAD OF doing:
#
#   oci.wait_until(email_client, email_client.get_sender(sender_id), ...)
#
# When deleting, since the resource may be gone, we set succeed_on_not_found on the waiter so that we consider
# receiving a 404 back from the service as a successful delete
email_client.delete_sender(get_sender_response.data.id)
oci.wait_until(email_client, get_sender_response, 'lifecycle_state', 'DELETED', succeed_on_not_found=True)
print('Deleted sender')

# Suppressions do not have a lifecycle state, so we don't have to wait on anything after deletion
email_client.delete_suppression(create_suppression_response.data.id)
print('Deleted suppression')

# In order to send email, we'll need to create an SMTP credential associated with an IAM user. More
# information on sending email can be found here:
# https://docs.cloud.oracle.com/Content/Email/Tasks/configuresmtpconnection.htm
#
# Note, also, that an IAM user can only have two active SMTP credentials at any time
#
# Also the password for the SMTP credential is ONLY available in the create response, so you
# should store/save this as it won't be retrievable later
create_smtp_credential_response = identity_client.create_smtp_credential(
    oci.identity.models.CreateSmtpCredentialDetails(
        description='new credential'
    ),
    user_id=config['user']
)
print('Created SMTP credential:\n{}'.format(create_smtp_credential_response.data))
print('\n=========================\n')

# We can update the description of an SMTP credential
update_smtp_credential_response = identity_client.update_smtp_credential(
    config['user'],
    create_smtp_credential_response.data.id,
    oci.identity.models.UpdateSmtpCredentialDetails(
        description='updated credential description'
    )
)
print('Updated SMTP credential:\n{}'.format(update_smtp_credential_response.data))
print('\n=========================\n')

# We can list the credentials for a user. Note that this is not a paginated operation
list_smtp_credentials_response = identity_client.list_smtp_credentials(config['user'])
print('SMTP credentials for user:\n{}'.format(list_smtp_credentials_response.data))
print('\n=========================\n')

identity_client.delete_smtp_credential(config['user'], create_smtp_credential_response.data.id)
print('Deleted SMTP credential')

print('\nScript Finished')
