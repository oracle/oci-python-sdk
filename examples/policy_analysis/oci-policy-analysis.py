# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# @author    : Andrew Gregory
#
# Supports Python 3
#
# DISCLAIMER – This is not an official Oracle application,  It is not supported by Oracle Support
#
# This example shows how the API can be used to build and analyze OCI Policies in a tenancy.
# The script recursively builds (and caches) a list of policy statements with provenance
# across a tenancy.  Because policies can be located in sub-compartments, it is generally harder
# to find which policies apply to a resource, a group, a compartment, and such.
# By running this script, you build a list of all statements in the tenancy, regardless of where they
# are located, and then you use the filtering commands to retrieve what you want.
# Please look at the argument parsing section or run with --help to see what is possible

from oci import config
from oci import identity
from oci import loggingingestion
from oci import pagination

from oci.auth.signers import InstancePrincipalsSecurityTokenSigner
from oci.loggingingestion.models import PutLogsDetails, LogEntry, LogEntryBatch

import argparse
import json
import os
import datetime
import uuid
import logging


# Lists
dynamic_group_statements = []
service_statements = []
regular_statements = []
special_statements = []

########################################
# Helper Methods


def print_statement(statement_tuple):
    a, b, c, d, e = statement_tuple
    logging.debug(f"Subject: {a}, Verb: {b}, Resource: {c}, Location: {d}, Condition: {e}")


def parse_statement(statement, comp_string, policy):
    # Parse tuple and partition
    # (subject, verb, resource, location, condition)
    # Pass 1 - where condition
    # Pass 2 - group subject
    # Pass 3 - location
    # Pass 4 - verb and resource
    pass1 = statement.casefold().partition(" where ")
    condition = pass1[2]
    pass2a = pass1[0].partition("allow ")
    pass2b = pass2a[2].partition(" to ")
    subject = pass2b[0]
    pass3 = pass2b[2].partition(" in ")
    location = pass3[2]
    pass4 = pass3[0].partition(" ")
    verb = pass4[0]
    resource = pass4[2]

    # Location Update
    # If compartment name, use hierarchy, if id then leave alone
    if "compartment id" in location:
        pass
    elif "tenancy" in location:
        pass
    else:
        sub_comp = location.partition("compartment ")[2]
        if comp_string == "":
            # if root, then leave compartment alone
            # location = f"compartment {comp_name}"
            pass
        else:
            location = f"compartment {comp_string}:{sub_comp}"

    # Build tuple based on modified location
    statement_tuple = (subject, verb, resource, location, condition,
                       f"{comp_string}", policy.name, policy.id, policy.compartment_id, statement)
    return statement_tuple


# Recursive Compartments / Policies
def getNestedCompartment(identity_client, comp_ocid, level, max_level, comp_string, verbose):

    # Level Printer
    level_string = ""
    for i in range(level):
        level_string += "|  "

    # Print with level
    get_compartment_response = identity_client.get_compartment(compartment_id=comp_ocid)
    comp = get_compartment_response.data
    logging.debug(f"{level_string}| Compartment Name: {comp.name} ID: {comp_ocid} Hierarchy: {comp_string}")

    # Get policies First
    list_policies_response = identity_client.list_policies(
        compartment_id=comp_ocid,
        limit=1000
    )
    for policy in list_policies_response.data:
        logging.debug(f"{level_string}| > Policy: {policy.name} ID: {policy.id}")
        for index, statement in enumerate(policy.statements, start=1):
            logging.debug(f"{level_string}| > -- Statement {index}: {statement}")

            # Make lower case
            statement = str.casefold(statement)

            # Root out "special" statements (endorse / define / as)
            if str.startswith(statement, "endorse") or str.startswith(statement, "admit") or str.startswith(statement, "define"):
                # Special statement tuple
                statement_tuple = (statement,
                                   f"{comp_string}", policy.name, policy.id, policy.compartment_id)

                special_statements.append(statement_tuple)
                continue

            # Helper returns tuple with policy statement and lineage
            statement_tuple = parse_statement(
                statement=statement,
                comp_string=comp_string,
                policy=policy
            )

            if statement_tuple[0] is None or statement_tuple[0] == "":
                logging.debug(f"****Statement {statement} resulted in bad tuple: {statement_tuple}")

            if "dynamic-group " in statement_tuple[0]:
                dynamic_group_statements.append(statement_tuple)
            elif "service " in statement_tuple[0]:
                service_statements.append(statement_tuple)
            else:
                regular_statements.append(statement_tuple)

    if level == max_level:
        # return, stop
        return

    # Using the paging API
    paginated_response = pagination.list_call_get_all_results(
        identity_client.list_compartments,
        comp_ocid,
        access_level="ACCESSIBLE",
        sort_order="ASC",
        lifecycle_state="ACTIVE",
        limit=1000)
    comp_list = paginated_response.data

    # Iterate and if any have sub-compartments, call recursive until none left
    if len(comp_list) == 0:
        # print(f"fall back level {level}")
        return
    for comp in comp_list:
        logging.debug(f"L{level} / Comp: {comp.name}")
        # Recurse
        if comp_string == "":
            getNestedCompartment(identity_client=identity_client,
                                 comp_ocid=comp.id,
                                 level=level + 1,
                                 max_level=max_level,
                                 comp_string=comp_string + comp.name,
                                 verbose=verbose)
        else:
            getNestedCompartment(identity_client=identity_client,
                                 comp_ocid=comp.id,
                                 level=level + 1,
                                 max_level=max_level,
                                 comp_string=comp_string + ":" + comp.name,
                                 verbose=verbose)

########################################
# Main Code


if __name__ == "__main__":
    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-pr", "--profile", help="Config Profile, named", default="DEFAULT")
    parser.add_argument("-o", "--ocid", help="OCID of compartment (if not passed, will use tenancy OCID from profile)", default="TENANCY")
    parser.add_argument("-sf", "--subjectfilter", help="Filter all statement subjects by this text")
    parser.add_argument("-vf", "--verbfilter", help="Filter all verbs (inspect,read,use,manage) by this text")
    parser.add_argument("-rf", "--resourcefilter", help="Filter all resource (eg database or stream-family etc) subjects by this text")
    parser.add_argument("-lf", "--locationfilter", help="Filter all location (eg compartment name) subjects by this text")
    parser.add_argument("-m", "--maxlevel", help="Max recursion level (0 is root only)", type=int, default=6)
    parser.add_argument("-c", "--usecache", help="Load from local cache (if it exists)", action="store_true")
    parser.add_argument("-w", "--writejson", help="Write filtered output to JSON", action="store_true")
    parser.add_argument("-ip", "--instanceprincipal", help="Use Instance Principal Auth - negates --profile", action="store_true")
    parser.add_argument("-lo", "--logocid", help="Use an OCI Log - provide OCID")
    args = parser.parse_args()
    verbose = args.verbose
    use_cache = args.usecache
    ocid = args.ocid
    profile = args.profile
    sub_filter = args.subjectfilter
    verb_filter = args.verbfilter
    resource_filter = args.resourcefilter
    location_filter = args.locationfilter
    max_level = args.maxlevel
    write_json_output = args.writejson
    use_instance_principals = args.instanceprincipal
    log_ocid = None if not args.logocid else args.logocid

    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    if use_instance_principals:
        logging.info("Using Instance Principal Authentication")
        signer = InstancePrincipalsSecurityTokenSigner()
        identity_client = identity.IdentityClient(config={}, signer=signer)
        loggingingestion_client = loggingingestion.LoggingClient(config={}, signer=signer)
        if ocid == "TENANCY":
            ocid = signer.tenancy_id
    else:
        # Use a profile (must be defined)
        logging.info(f"Using Profile Authentication: {profile}")
        config = config.from_file(profile_name=profile)
        if ocid == "TENANCY":
            logging.info(f'Using tenancy OCID from profile: {config["tenancy"]}')
            ocid = config["tenancy"]

        # Create the OCI Client to use
        identity_client = identity.IdentityClient(config)
        loggingingestion_client = loggingingestion.LoggingClient(config)

    # Load from cache (if exists)
    if use_cache:
        logging.info("Loading Policy statements from cache")

        if os.path.isfile(f'./.policy-special-cache-{ocid}.dat'):
            with open(f'./.policy-special-cache-{ocid}.dat', 'r') as filehandle:
                special_statements = json.load(filehandle)
        if os.path.isfile(f'./.policy-dg-cache-{ocid}.dat'):
            with open(f'./.policy-dg-cache-{ocid}.dat', 'r') as filehandle:
                dynamic_group_statements = json.load(filehandle)
        if os.path.isfile(f'.policy-svc-cache-{ocid}.dat'):
            with open(f'./.policy-svc-cache-{ocid}.dat', 'r') as filehandle:
                service_statements = json.load(filehandle)
        if os.path.isfile(f'.policy-statement-cache-{ocid}.dat'):
            with open(f'./.policy-statement-cache-{ocid}.dat', 'r') as filehandle:
                regular_statements = json.load(filehandle)
    else:
        # Run Recursion Process
        level = 0
        logging.info("Loading policies recursively. Be patient (or run again with -v)...")
        logging.debug("========Enter Recursion==============")
        getNestedCompartment(identity_client=identity_client,
                             comp_ocid=ocid,
                             level=level,
                             max_level=max_level,
                             comp_string="",
                             verbose=verbose)
        logging.debug("========Exit Recursion==============")

    # Write to local cache (per type)
    with open(f'.policy-special-cache-{ocid}.dat', 'w') as filehandle:
        json.dump(special_statements, filehandle)
    with open(f'.policy-dg-cache-{ocid}.dat', 'w') as filehandle:
        json.dump(dynamic_group_statements, filehandle)
    with open(f'.policy-svc-cache-{ocid}.dat', 'w') as filehandle:
        json.dump(service_statements, filehandle)
    with open(f'.policy-statement-cache-{ocid}.dat', 'w') as filehandle:
        json.dump(regular_statements, filehandle)

    # Perform Filtering
    if sub_filter:
        logging.info(f"Filtering subject: {sub_filter}. Before: {len(dynamic_group_statements)}/{len(service_statements)}/{len(regular_statements)} DG/SVC/Reg statements")
        dynamic_group_statements = list(filter(lambda statement: sub_filter.casefold() in statement[0].casefold(), dynamic_group_statements))
        service_statements = list(filter(lambda statement: sub_filter.casefold() in statement[0].casefold(), service_statements))
        regular_statements = list(filter(lambda statement: sub_filter.casefold() in statement[0].casefold(), regular_statements))
        logging.info(f"After: {len(dynamic_group_statements)}/{len(service_statements)}/{len(regular_statements)} DG/SVC/Reg statements")

    if verb_filter:
        logging.info(f"Filtering verb: {verb_filter}. Before: {len(dynamic_group_statements)}/{len(service_statements)}/{len(regular_statements)} DG/SVC/Reg statements")
        dynamic_group_statements = list(filter(lambda statement: verb_filter.casefold() in statement[1].casefold(), dynamic_group_statements))
        service_statements = list(filter(lambda statement: verb_filter.casefold() in statement[1].casefold(), service_statements))
        regular_statements = list(filter(lambda statement: verb_filter.casefold() in statement[1].casefold(), regular_statements))
        logging.info(f"After: {len(dynamic_group_statements)}/{len(service_statements)}/{len(regular_statements)} DG/SVC/Reg statements")

    if resource_filter:
        logging.info(f"Filtering resource: {resource_filter}. Before: {len(dynamic_group_statements)}/{len(service_statements)}/{len(regular_statements)} DG/SVC/Reg statements")
        dynamic_group_statements = list(filter(lambda statement: resource_filter.casefold() in statement[2].casefold(), dynamic_group_statements))
        service_statements = list(filter(lambda statement: resource_filter.casefold() in statement[2].casefold(), service_statements))
        regular_statements = list(filter(lambda statement: resource_filter.casefold() in statement[2].casefold(), regular_statements))
        logging.info(f"After: {len(dynamic_group_statements)}/{len(service_statements)}/{len(regular_statements)} DG/SVC/Reg statements")

    if location_filter:
        logging.info(f"Filtering location: {location_filter}. Before: {len(dynamic_group_statements)}/{len(service_statements)}/{len(regular_statements)} DG/SVC/Reg statements")
        dynamic_group_statements = list(filter(lambda statement: location_filter.casefold() in statement[3].casefold(), dynamic_group_statements))
        service_statements = list(filter(lambda statement: location_filter.casefold() in statement[3].casefold(), service_statements))
        regular_statements = list(filter(lambda statement: location_filter.casefold() in statement[3].casefold(), regular_statements))
        logging.info(f"After: {len(dynamic_group_statements)}/{len(service_statements)}/{len(regular_statements)} DG/SVC/Reg statements")

    # Print Special
    entries = []
    logging.info("========Summary Special==============")
    for index, statement in enumerate(special_statements, start=1):
        logging.info(f"Statement #{index}: {statement[0]} | Policy: {statement[2]}")
        entries.append(LogEntry(id=str(uuid.uuid1()),
                                data=f"Statement #{index}: {statement}"))
    logging.info(f"Total Special statement in tenancy: {len(special_statements)}")

    # Create Log Batch
    special_batch = LogEntryBatch(defaultlogentrytime=datetime.datetime.utcnow(),
                                  source="oci-policy-analysis",
                                  type="special-statement",
                                  entries=entries)

    # Print Dynamic Groups
    entries = []
    logging.info("========Summary DG==============")
    for index, statement in enumerate(dynamic_group_statements, start=1):
        logging.info(f"Statement #{index}: {statement[9]} | Policy: {statement[5]}/{statement[6]}")
        entries.append(LogEntry(id=str(uuid.uuid1()),
                                data=f"Statement #{index}: {statement[9]} | Policy: {statement[5]}/{statement[6]}"))
    logging.info(f"Total Service statement in tenancy: {len(dynamic_group_statements)}")

    # Create Log Batch
    dg_batch = LogEntryBatch(defaultlogentrytime=datetime.datetime.utcnow(),
                             source="oci-policy-analysis",
                             type="dynamic-group-statement",
                             entries=entries)

    # Print Service
    entries = []
    logging.info("========Summary SVC==============")
    for index, statement in enumerate(service_statements, start=1):
        logging.info(f"Statement #{index}: {statement[9]} | Policy: {statement[5]}/{statement[6]}")
        entries.append(LogEntry(id=str(uuid.uuid1()),
                                data=f"Statement #{index}: {statement[9]} | Policy: {statement[5]}/{statement[6]}"))
    logging.info(f"Total Service statement in tenancy: {len(service_statements)}")

    # Create Log Batch
    service_batch = LogEntryBatch(defaultlogentrytime=datetime.datetime.utcnow(),
                                  source="oci-policy-analysis",
                                  type="service-statement",
                                  entries=entries)

    # Print Regular
    entries = []
    logging.info("========Summary Reg==============")
    for index, statement in enumerate(regular_statements, start=1):
        logging.info(f"Statement #{index}: {statement[9]} | Policy: {statement[5]}/{statement[6]}")
        entries.append(LogEntry(id=str(uuid.uuid1()),
                                data=f"Statement #{index}: {statement[9]} | Policy: {statement[5]}/{statement[6]}"))
    logging.info(f"Total Regular statement in tenancy: {len(regular_statements)}")

    # Create Log Batch
    regular_batch = LogEntryBatch(defaultlogentrytime=datetime.datetime.now(datetime.UTC),
                                  source="oci-policy-analysis",
                                  type="regular-statement",
                                  entries=entries)

    # Write batches to OCI Logging
    if log_ocid:
        put_logs_response = loggingingestion_client.put_logs(
            log_id=log_ocid,
            put_logs_details=PutLogsDetails(
                specversion="1.0",
                log_entry_batches=[special_batch, dg_batch, service_batch, regular_batch]
            )
        )

    # To output file if required
    if write_json_output:
        # Empty Dictionary
        statements_list = []
        for i, s in enumerate(special_statements):
            statements_list.append({"type": "special", "statement": s[0],
                                    "lineage": {"policy-compartment-ocid": s[4], "policy-relative-hierarchy": s[1],
                                                "policy-name": s[2], "policy-ocid": s[3]}
                                    })
        for i, s in enumerate(dynamic_group_statements):
            statements_list.append({"type": "dynamic-group", "subject": s[0], "verb": s[1],
                                    "resource": s[2], "location": s[3], "conditions": s[4],
                                    "lineage": {"policy-compartment-ocid": s[8], "policy-relative-hierarchy": s[5],
                                                "policy-name": s[6], "policy-ocid": s[7], "policy-text": s[9]}
                                    })
        for i, s in enumerate(service_statements):
            statements_list.append({"type": "service", "subject": s[0], "verb": s[1],
                                    "resource": s[2], "location": s[3], "conditions": s[4],
                                    "lineage": {"policy-compartment-ocid": s[8], "policy-relative-hierarchy": s[5],
                                                "policy-name": s[6], "policy-ocid": s[7], "policy-text": s[9]}
                                    })
        for i, s in enumerate(regular_statements):
            statements_list.append({"type": "regular", "subject": s[0], "verb": s[1],
                                    "resource": s[2], "location": s[3], "conditions": s[4],
                                    "lineage": {"policy-compartment-ocid": s[8], "policy-relative-hierarchy": s[5],
                                                "policy-name": s[6], "policy-ocid": s[7], "policy-text": s[9]}
                                    })
        # Serializing json
        json_object = json.dumps(statements_list, indent=2)

        # Writing to sample.json
        with open(f"policyoutput-{ocid}.json", "w") as outfile:
            outfile.write(json_object)
