# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from cryptography import x509
from cryptography.hazmat.backends import default_backend

import os.path
import requests
import six
import threading


# An abstract class which defines the interface via which certificates (and their corresponding private key) can be retrieved.
# Implementors should define their own concrete fetching mechanism (e.g. a URL, from a file, from provided PEM-format strings)
# but they are expected to be able to vend information in various ways:
#
#   - A dictionary containing all certificate and private key information. This is defined as:
#       - certificate: the certificate PEM string
#       - private_key_pem: the private key PEM string
#       - private_key: the private key as a cryptography.io X509 certificate object
#   - The certificate as a cryptography.io X509 certificate object
#   - The certificate PEM string
#   - The private key PEM string
#   - The private key as a cryptography.io X509 certificate object
#
# Certificates are optionally refreshable via a refresh() method. Where the refresh may not make sense (e.g. if the PEM-format strings
# are provided directly), implementors should make refersh() a no-op rather than throwing an exception.
class AbstractCertificateRetriever(object):
    def __init__(self, **kwargs):
        self.certificate_and_private_key = {
            'certificate': None,
            'private_key_pem': None,
            'private_key': None
        }

    # Refreshes the certificates held by this object (e.g. because they have been rotated)
    def refresh(self):
        raise NotImplementedError('Subclasses should implement this')

    # Returns the certificate_and_private_key dictionary contained by this object
    def get_certificate_and_private_key(self):
        raise NotImplementedError('Subclasses should implement this')

    # Retrieves the certificate as a cryptography.x509.Certificate
    def get_certificate_as_certificate(self):
        raise NotImplementedError('Subclasses should implement this')

    # Retrieves a string containing the certificate contents
    def get_certificate_raw(self):
        raise NotImplementedError('Subclasses should implement this')

    # Retrievea a string containing the PEM-encoded private key
    def get_private_key_pem(self):
        raise NotImplementedError('Subclasses should implement this')

    # Retrieves the private key as a cryptography private key
    def get_private_key(self):
        raise NotImplementedError('Subclasses should implement this')


class UrlBasedCertificateRetriever(AbstractCertificateRetriever):
    """
    A certificate retriever which reads PEM-format strings from URLs.

    :param str certificate_url:
        The URL from which to retrieve a certificate. It is assumed that what we retrieve is the PEM-formatted string for the certificate.
        This is mandatory

    :param str private_key_url (optional):
        The URL from which to retrieve the private key corresponding to certificate_url (if any). It is assumed that what we retrieve is the PEM-formatted string for
        the private key.

    :param str passphrase (optional):
        The passphrase of the private key (if any).
    """

    READ_CHUNK_BYTES = 1024 * 1024  # A mebibyte

    def __init__(self, **kwargs):
        super(UrlBasedCertificateRetriever, self).__init__()

        if 'certificate_url' not in kwargs:
            raise TypeError('certificate_url must be supplied as a keyword argument')

        self.cert_url = kwargs['certificate_url']
        self.private_key_url = kwargs.get('private_key_url')
        self.passphrase = kwargs.get('passphrase')

        if self.passphrase and isinstance(self.passphrase, six.text_type):
            self.passphrase = self.passphrase.encode('ascii')

        self._refresh_lock = threading.Lock()

        self.refresh()

    def refresh(self):
        import oci.signer

        self._refresh_lock.acquire()
        try:
            downloaded_certificate = six.BytesIO()
            response = requests.get(self.cert_url, stream=True)
            for chunk in response.raw.stream(self.READ_CHUNK_BYTES, decode_content=False):
                downloaded_certificate.write(chunk)

            self.certificate_and_private_key['certificate'] = downloaded_certificate.getvalue().strip()
            downloaded_certificate.close()
            if isinstance(self.certificate_and_private_key['certificate'], six.text_type):
                self.certificate_and_private_key['certificate'] = self.certificate_and_private_key['certificate'].encode('ascii')

            if self.private_key_url:
                downloaded_private_key_raw = six.BytesIO()
                response = requests.get(self.private_key_url, stream=True)
                for chunk in response.raw.stream(self.READ_CHUNK_BYTES, decode_content=False):
                    downloaded_private_key_raw.write(chunk)

                self.certificate_and_private_key['private_key_pem'] = downloaded_private_key_raw.getvalue().strip()
                downloaded_private_key_raw.close()

                if isinstance(self.certificate_and_private_key['private_key_pem'], six.text_type):
                    self.certificate_and_private_key['private_key_pem'] = self.certificate_and_private_key['private_key_pem'].encode('ascii')

                self.certificate_and_private_key['private_key'] = oci.signer.load_private_key(
                    self.certificate_and_private_key['private_key_pem'],
                    self.passphrase
                )
        finally:
            self._refresh_lock.release()

    def get_certificate_and_private_key(self):
        self._refresh_lock.acquire()
        ret_val = self.certificate_and_private_key.copy()
        self._refresh_lock.release()

        return ret_val

    def get_certificate_as_certificate(self):
        raw_cert = self.get_certificate_raw()
        if raw_cert:
            return x509.load_pem_x509_certificate(raw_cert, default_backend())
        else:
            return None

    def get_certificate_raw(self):
        self._refresh_lock.acquire()
        certificate = self.certificate_and_private_key.copy()['certificate']
        self._refresh_lock.release()

        return certificate

    def get_private_key_pem(self):
        self._refresh_lock.acquire()
        private_key = self.certificate_and_private_key.copy()['private_key_pem']
        self._refresh_lock.release()

        return private_key

    def get_private_key(self):
        self._refresh_lock.acquire()
        private_key = self.certificate_and_private_key.copy()['private_key']
        self._refresh_lock.release()

        return private_key


class PEMStringCertificateRetriever(AbstractCertificateRetriever):
    """
    A certificate retriever which is provided PEM format strings directly. This retriever is non-refreshable, and calling refresh() is a no-op.

    :param str certificate_pem:
        The PEM-formatted string of the certificate. This is mandatory.

    :param str private_key_pem (optional):
        The PEM-formatted string of the private key corresponding to certificate_pem (if any).

    :param str passphrase (optional):
        The passphrase of the private key (if any).
    """

    def __init__(self, **kwargs):
        import oci.signer

        super(UrlBasedCertificateRetriever, self).__init__()

        if 'certificate_pem' not in kwargs:
            raise TypeError('certificate_pem must be supplied as a keyword argument')

        if isinstance(kwargs['certificate_pem'], six.text_type):
            self.certificate_and_private_key['certificate'] = kwargs['certificate_pem'].encode('ascii')
        else:
            self.certificate_and_private_key['certificate'] = kwargs['certificate_pem']

        if 'private_key_pem' in kwargs and kwargs['private_key_pem']:
            if isinstance(kwargs['private_key_pem'], six.text_type):
                self.certificate_and_private_key['private_key_pem'] = kwargs['private_key_pem'].encode('ascii')
            else:
                self.certificate_and_private_key['private_key_pem'] = kwargs['private_key_pem']

            if 'passphrase' in kwargs and kwargs['passphrase']:
                passphrase = kwargs['passphrase'].encode('ascii')
            else:
                passphrase = None

            self.certificate_and_private_key['private_key'] = oci.signer.load_private_key(
                self.certificate_and_private_key['private_key_pem'],
                passphrase
            )

    def refresh(self):
        # Since these are just the string, there is no refresh as such. A new object should be created
        # if the strings change
        pass

    def get_certificate_and_private_key(self):
        return self.certificate_and_private_key.copy()

    def get_certificate_as_certificate(self):
        return x509.load_pem_x509_certificate(self.certificate_and_private_key['certificate'], default_backend())

    def get_certificate_raw(self):
        return self.certificate_and_private_key['certificate']

    def get_private_key_pem(self):
        return self.certificate_and_private_key['private_key_pem']

    def get_private_key(self):
        return self.certificate_and_private_key['private_key']


class FileBasedCertificateRetriever(PEMStringCertificateRetriever):
    """
    A specialization of PEMStringCertificateRetriever which reads certificates from a file. This retriever is non-refreshable, and calling refresh() is a no-op.

    :param str certificate_file_path:
        The file path from which to retrieve a certificate. It is assumed that what we retrieve is the PEM-formatted string for the certificate.
        This is mandatory

    :param str private_key_pem_file_path (optional):
        The file path from which to retrieve the private key corresponding to certificate_file_path (if any). It is assumed that what we retrieve is the PEM-formatted string for
        the private key.

    :param str passphrase (optional):
        The passphrase of the private key (if any).

    """

    def __init__(self, **kwargs):
        if 'certificate_file_path' not in kwargs:
            raise TypeError('certificate_file_path must be supplied as a keyword argument')

        if 'private_key_pem_file_path' in kwargs:
            private_key_pem = self._load_data_from_file(kwargs['private_key_pem_file_path'])
        else:
            private_key_pem = None

        parent_class_kwargs = {
            'certificate_pem': self._load_data_from_file(kwargs['certificate_file_path']),
            'private_key_pem_file_path': private_key_pem,
            'passphrase': kwargs.get('passphrase')
        }

        super(FileBasedCertificateRetriever, self).__init__(**parent_class_kwargs)

    def _load_data_from_file(self, filename):
        filename = os.path.expanduser(filename)
        with open(filename, mode="rb") as f:
            cert_data = f.read().strip()

        return cert_data
