.. _quickstart:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Quickstart
~~~~~~~~~~

Clients only require a valid config object:

.. code-block:: pycon

    >>> from oci.identity import IdentityClient
    >>> identity = IdentityClient(config)

================================
 CRUD operations and Pagination
================================


-------------------
 Creating entities
-------------------

Let's create a new user and group, and add the user to the group.  Then we'll list all users in the tenancy, and
finally clean up the user and group we created.

First, we'll need to create a valid config object and service client.  If you haven't set up a config file, head over
to the :ref:`Configuration <configuration>` section to create one.  We'll use the default location ``~/.oci/config``
and default profile name ``DEFAULT`` to create an Identity client.  Since we'll be using the root compartment
(or tenancy) for most operations, let's also extract that from the config object:

.. code-block:: pycon

    >>> import oci
    >>> config = oci.config.from_file()
    >>> identity = oci.identity.IdentityClient(config)
    >>> compartment_id = config["tenancy"]

Next we'll need to populate an instance of the ``CreateGroupDetails`` model with our request, and then send it:

.. code-block:: pycon

    >>> from oci.identity.models import CreateGroupDetails
    >>> request = CreateGroupDetails()
    >>> request.compartment_id = compartment_id
    >>> request.name = "my-test-group"
    >>> request.description = "Created with the Python SDK"

    >>> group = identity.create_group(request)
    >>> print(group.data.id)
    "id": "ocid1.group.oc1..aaaaaaaaikib..."


Creating a user is very similar:

.. code-block:: pycon

    >>> from oci.identity.models import CreateUserDetails
    >>> request = CreateUserDetails()
    >>> request.compartment_id = compartment_id
    >>> request.name = "my-test-user"
    >>> request.description = "Created with the Python SDK"
    >>> user = identity.create_user(request)
    >>> print(user.data.id)
    "ocid1.user.oc1..aaaaaaaamkym..."

Using the ids from the ``group`` and ``user`` above, we can add the user to the group:

.. code-block:: pycon

    >>> from oci.identity.models import AddUserToGroupDetails
    >>> request = AddUserToGroupDetails()
    >>> request.group_id = group.data.id
    >>> request.user_id = user.data.id
    >>> response = identity.add_user_to_group(request)
    >>> print(response.status)
    200

-------------------------
 Listing with Pagination
-------------------------

List operations use pagination to limit the size of each response.  The Python SDK exposes the pagination values through
the ``has_next_page`` and ``next_page`` attributes on each response.  For example, listing users in the root
compartment:

.. code-block:: pycon

    >>> first_page = identity.list_users(compartment_id=compartment_id)
    >>> len(first_page.data)
    100
    >>> first_page.has_next_page
    True
    >>> first_page.next_page
    'AAAAAAAAAAHNo_rjHo6xZPxHLZZ020jMio...'

Even though a response includes a next page, there may not be more results.  The last page will return an empty list,
and will not have a ``next_page`` token.

You can manually iterate through responses, providing the page from the previous response to the next request. For example:

.. code-block:: python

    response = identity.list_users(compartment_id)
    users = response.data
    while response.has_next_page:
        response = identity.list_users(compartment_id, page=response.next_page)
        users.extend(response.data)


As a convenience over manually writing pagination code, you can make use of the functions in the :py:mod:`~oci.pagination` module to:

* Eagerly load all possible results from a list call
* Eagerly load all results from a list call up to a given limit
* Lazily load results (either all results, or up to a given limit) from a list call via a generator. These generators can yield either values/models or the raw response from calling the list operation

For examples on pagination, please check `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/pagination.py>`__.


-------------------
 Deleting entities
-------------------

Now to clean up the entities we created.  Users can't be deleted if they're still part of a group, and groups can't be
deleted if they still have users.  So we need to use ``identity.remove_user_from_group``, which takes a
``user_group_membership_id``.  Because users and groups can have any number of relationships, we'll use
``list_user_group_memberships`` and provide **both** optional parameters ``user_id`` and ``group_id`` to constrain the
result set:

.. code-block:: pycon

    >>> memberships = identity.list_user_group_memberships(
    ...     compartment_id=compartment_id,
    ...     user_id=user.data.id,
    ...     group_id=group.data.id)
    # There can never be more than one membership for a unique user/group combination
    >>> assert len(memberships.data) == 1
    >>> membership_id = memberships.data[0].id

Finally, we can remove the user from the group, and delete both resources.  Here we're using ``response.status`` to
make sure the delete responded with 204:

.. code-block:: pycon

    >>> identity.remove_user_from_group(
    ...     user_group_membership_id=membership_id).status
    204
    >>> identity.delete_user(user_id=user.data.id).status
    204
    >>> identity.delete_group(group_id=group.data.id).status
    204


====================
 Working with Bytes
====================

When using object storage, you'll need to provide a namespace, in addition to your compartment id:

.. code-block:: pycon

    >>> object_storage = oci.object_storage.ObjectStorageClient(config)
    >>> namespace = object_storage.get_namespace().data

To upload an object, we'll create a bucket:

.. code-block:: pycon

    >>> from oci.object_storage.models import CreateBucketDetails
    >>> request = CreateBucketDetails()
    >>> request.compartment_id = compartment_id
    >>> request.name = "MyTestBucket"
    >>> bucket = object_storage.create_bucket(namespace, request)
    >>> bucket.data.etag
    '5281759f-60bb-4b93-8676-f8d141b5f211'

Now we can upload arbitrary bytes:

.. code-block:: pycon

    >>> my_data = b"Hello, World!"
    >>> obj = object_storage.put_object(
    ...     namespace,
    ...     bucket.data.name,
    ...     "my-object-name",
    ...     my_data)

And to get it back:

.. code-block:: pycon

    >>> same_obj = object_storage.get_object(
    ...     namespace,
    ...     bucket.data.name,
    ...     "my-object-name")
    ... same_obj.data
    <Response [200]>
    ... same_obj.data.content
    b'Hello, World!'

============
 Next Steps
============

Next, head to the `User Guides`_ or jump right into the :ref:`API Reference <api-reference>`
to explore the available operations for each service, and their parameters. Additional Python examples can be found on `GitHub <https://github.com/oracle/oci-python-sdk/tree/master/examples>`__.


.. note::

    The Python SDK uses ``lowercase_with_underscores`` for operations and parameters.  For example, the
    `ListApiKeys`_ operation is called with ``IdentityClient.list_api_keys`` and its parameter
    ``userId`` is translated to ``user_id``.

    .. _ListApiKeys: https://docs.cloud.oracle.com/api/#/en/identity/20160918/ApiKey/ListApiKeys

.. _User Guides: https://docs.cloud.oracle.com/Content/services.htm
