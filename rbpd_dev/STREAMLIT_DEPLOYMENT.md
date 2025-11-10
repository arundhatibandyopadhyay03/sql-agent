# Streamlit Cloud Deployment Guide

## Issue Fixed
The `binascii.Error` was caused by the application trying to use environment variables via `os.getenv()` instead of Streamlit's secrets management system. The error occurred because the `COSMOS_KEY` was either missing or not a valid base64 encoded string.

## Changes Made
1. **Updated rbpd_main.py** to use `st.secrets` for Streamlit Cloud deployment while maintaining backward compatibility with local development
2. **Added validation** for required environment variables and COSMOS_KEY format
3. **Created secrets.toml template** for proper configuration

## Deployment Steps

### 1. Configure Secrets in Streamlit Cloud
In your Streamlit Cloud app dashboard:

1. Go to your app settings
2. Click on "Secrets" tab
3. Add the following secrets (replace with your actual values):

```toml
# Azure OpenAI Configuration
AZURE_OPENAI_KEY = "your_actual_azure_openai_key"
AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
AZURE_OPENAI_VERSION = "2024-02-15-preview"
ASSISTANT_ID = "your_actual_assistant_id"

# Azure Blob Storage Configuration
BLOB_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=youraccount;AccountKey=yourkey;EndpointSuffix=core.windows.net"
BLOB_CONTAINER_NAME = "your_container_name"
ACCOUNT_NAME = "your_storage_account_name"
ACCOUNT_KEY = "your_storage_account_key"

# Azure Cosmos DB Configuration
COSMOS_ENDPOINT = "https://your-cosmos-account.documents.azure.com:443/"
COSMOS_KEY = "your_actual_cosmos_primary_key"
COSMOS_DB_NAME = "your_database_name"
COSMOS_CONTAINER_NAME = "your_container_name"
```

### 2. Important Notes
- **COSMOS_KEY**: Must be the primary or secondary key from your Cosmos DB account (not the connection string)
- **Keys must be valid base64**: The app now validates the COSMOS_KEY format
- **No quotes needed**: In Streamlit secrets, don't wrap values in quotes
- **Case sensitive**: Variable names are case sensitive

### 3. Local Development
For local development, you can still use the `.env` file or set environment variables as before. The code will automatically fall back to `os.getenv()` when not running in Streamlit.

### 4. Troubleshooting
If you still get errors:
1. Verify all secrets are set in Streamlit Cloud
2. Check that COSMOS_KEY is the actual key (not connection string)
3. Ensure no trailing spaces in secret values
4. Restart the app after updating secrets

## Security Notes
- Never commit real secrets to version control
- Use different keys for development and production
- Regularly rotate your Azure keys
- The `.gitignore` file already excludes `secrets.toml`