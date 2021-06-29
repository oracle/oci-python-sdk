.. _sdk-signing_bodies:

Signing bodies
~~~~~~~~~~~~~~

Some OCI APIs allows the user to sign bodies for a Put/Post/Patch request.
Python SDK uses the SHA256 algorithm present in the python Hashlib library for signing these bodies. As hashes only
work with bytes, the SDK handles non-byte bodies based on the body type. For string bodies, the SDK encodes them as utf-8
before signing them, whereas, for streaming bodies the SDK first tries determine if the stream can be rewound.
If the stream is rewindable, the SDK records its current position, reads the stream in chunks from that position and
also calculating its corresponding hash and content length, after which the stream is rewound back to its original position.
In cases where the stream cannot be rewound SDK tries to backup the body and read it into its bytes equivalent to calculate
the hash for signing. As the stream cannot rewound, the SDK updates the request body with the equivalent bytes content.


.. Note::
    The SDK Performance might be affected if you are signing a large streaming body, as such, we recommend the user to
    sign these bodies themselves to avoid having the SDK sign them instead. Users can sign the body by using the
    Python Hashlib library and update the `x-content-sha256` header as a custom header as mentioned in :ref:`setting custom headers<Setting custom headers>`
