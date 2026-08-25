# Sync and async client examples

These examples make the same three OCI Generative AI chat API calls using the
synchronous client, the asynchronous client, or both clients for comparison.

Set the required compartment OCID before running an example:

```bash
export OCI_COMPARTMENT_ID="ocid1.compartment..."
python examples/SyncAsync/async_calls_example.py
python examples/SyncAsync/sync_calls_example.py
python examples/SyncAsync/sync_async_calls_example.py
```

The examples read the `DEFAULT` profile from `~/.oci/config`. These optional
environment variables override the defaults:

- `OCI_CONFIG_FILE`: OCI config file path
- `OCI_CONFIG_PROFILE`: profile name
- `OCI_GENAI_MODEL_ID`: on-demand chat model ID
- `OCI_GENAI_ENDPOINT`: Generative AI inference endpoint

The async example uses `asyncio.gather` so that its three calls are in flight at
the same time. The sync example performs the calls one after another. The
combined example runs both approaches and prints their elapsed times.
