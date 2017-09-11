.. _forward-compatibility:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Forward Compatibility
~~~~~~~~~~~~~~~~~~~~~~
Some response fields are enum-typed. In the future, individual services may return values not covered by existing enums for that field. To address this possibility, every enum-type response field has an additional value named "UNKNOWN_ENUM_VALUE". If a service returns a value that is not recognized by your version of the SDK, then the response field will be set to this value. Please ensure that your code handles the "UNKNOWN_ENUM_VALUE" case if you have conditional logic based on an enum-typed field.