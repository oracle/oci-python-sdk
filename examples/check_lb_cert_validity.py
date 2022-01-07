# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script checks all load balancer certificates in the tenancy if they will remain valid
# after N (user supplied) number of days.  It traverses the compartment tree, locating
# load balancer ctificates in each compartment.  It extracts the "Not Valid After" attribute
# and checks if the certificate will expire after N (user supplied) days.
#
# Usage:
# python check_lb_cert_validity.py -d 'expiry-in-the-next-days' -c 'compartment-ocid'
#
# The script uses the default OCI SDK/CLI configuration file ~/.oci/config .


import argparse
import oci
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta


def verify_cert_expiry(compartment_id, load_balancer_id, cert_bundle):

    pem_cert = cert_bundle.public_certificate
    cert = x509.load_pem_x509_certificate(bytes(str(pem_cert), 'utf-8'), default_backend())
    cert_not_valid_after = cert.not_valid_after.date()

    validity_date = datetime.utcnow().date().today() + timedelta(days=int(cert_validity_days))

    if cert_not_valid_after <= validity_date:
        print("========================================================")
        print("Compartment Id: ", compartment_id)
        print("Load Balancer ID: ", load_balancer_id)
        print("Certificate Name: ", cert_bundle.certificate_name)
        print("Certificate Validity: ", cert.not_valid_after)
        print("Certificate expiring within {0} days.".format(cert_validity_days))
        print("========================================================\n")


# Check certificates in a load balancer.
def verify_certificates(compartment_id, load_balancer_id):

    response = lb_client.list_certificates(load_balancer_id)

    cert_list = response.data
    for i in cert_list:
        verify_cert_expiry(compartment_id, load_balancer_id, i)


# Check certificates in all load balancers in a compartment.
def inpect_lb_certs(compartment_id):

    response = lb_client.list_load_balancers(compartment_id)
    lb_list = response.data

    for i in lb_list:
        lb_id = i.id
        verify_certificates(compartment_id, lb_id)


# Traverse the compartment tree and identify any expired certificates.
def traverse_compartment_tree(compartment_id):

    response = identity_client.list_compartments(compartment_id)
    child_compartment_list = response.data

    length = len(child_compartment_list)

    if length > 0:
        for i in child_compartment_list:
            child_compartment_id = i.id
            traverse_compartment_tree(child_compartment_id)

    # Look for expiring certificates in load balancers belonging to this compartment.
    inpect_lb_certs(compartment_id)


def main():

    # Traverse the compartment heirarchy and identify the expiring certificates.
    traverse_compartment_tree(top_compartment)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",
                        "--expiry-in-the-next-days",
                        action="store",
                        help="check certificates which will expire in the coming days",
                        required=True)
    parser.add_argument("-c",
                        "--compartment-id",
                        action="store",
                        default="root",
                        help="Compartment and its child compartments to be searched for expired load balancer certs ")

    args = parser.parse_args()

    # Get hold of the arguments.
    cert_validity_days = args.expiry_in_the_next_days
    top_compartment = args.compartment_id

    try:
        config = oci.config.from_file()
    except oci.exceptions.ConfigFileNotFound as e:
        print("")
        print("ConfigFileNotFound: {}".format(e))
        print("")
        exit(-1)

    # If compartment was not provided, default value is root.
    if "root" == top_compartment:
        top_compartment = config["tenancy"]

    # Service clients
    identity_client = oci.identity.IdentityClient(config)
    lb_client = oci.load_balancer.LoadBalancerClient(config)

    main()
