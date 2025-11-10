# Streamlit Cloud Deployment Guide

## Prerequisites

1. **GitHub Repository**: Push your code to a GitHub repository
2. **Azure Services**: Ensure you have the following Azure services set up:
   - Azure OpenAI Service with an Assistant
   - Azure Blob Storage
   - Azure Cosmos DB

## Deployment Steps

### 1. Prepare Your Repository

1. Push all files to your GitHub repository
2. Ensure your repository is public or you have Streamlit Cloud access to private repos

### 2. Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository
5. Set the main file path to: `rbpd_dev/application.py`
6. Click "Deploy"

### 3. Configure Secrets

In your Streamlit Cloud app dashboard:

1. Go to "Settings" → "Secrets"
2. Add the following secrets (replace with your actual values):

```toml
AZURE_OPENAI_KEY = "your_azure_openai_key"
AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
AZURE_OPENAI_VERSION = "2024-02-15-preview"
ASSISTANT_ID = "your_assistant_id"

BLOB_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=your_account;AccountKey=your_key;EndpointSuffix=core.windows.net"
BLOB_CONTAINER_NAME = "your_container_name"
ACCOUNT_NAME = "your_storage_account_name"
ACCOUNT_KEY = "your_storage_account_key"

COSMOS_ENDPOINT = "https://your-cosmos-account.documents.azure.com:443/"
COSMOS_KEY = "your_cosmos_key"
COSMOS_DB_NAME = "your_database_name"
COSMOS_CONTAINER_NAME = "your_container_name"
```

### 4. Verify Deployment

1. Wait for the app to build and deploy
2. Test the login functionality
3. Test file upload and chat features
4. Verify Azure service connections

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are in `requirements.txt`
2. **Authentication Errors**: Verify your Azure credentials in secrets
3. **File Upload Issues**: Check Azure Blob Storage permissions
4. **Database Errors**: Verify Cosmos DB connection and permissions

### Logs

Check the Streamlit Cloud logs in your app dashboard for detailed error messages.

## Local Development

For local development:

1. Create a `.env` file with your environment variables
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run rbpd_dev/application.py`

## Security Notes

- Never commit secrets to your repository
- Use Streamlit Cloud's secrets management
- Regularly rotate your Azure keys
- Monitor your Azure resource usage