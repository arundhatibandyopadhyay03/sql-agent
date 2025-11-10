# RBPD - AI-Powered Document to BRD Converter

An intelligent Streamlit application that converts your documents into Business Requirements Documents (BRD) using Azure OpenAI and Azure services.

## Features

- 🤖 AI-powered document analysis and conversion
- 📁 Multi-format file upload support (PDF, DOCX, XLSX, CSV, TXT, PPTX, JSON, MD)
- 💬 Interactive chat interface
- 📊 Chat history management
- 🔐 Secure user authentication
- ☁️ Azure Cloud integration

## Deployment

This app is configured for deployment on Streamlit Cloud.

### Environment Variables Required

Set these in your Streamlit Cloud secrets:

```toml
AZURE_OPENAI_KEY = "your_azure_openai_key"
AZURE_OPENAI_ENDPOINT = "your_azure_openai_endpoint"
AZURE_OPENAI_VERSION = "your_api_version"
ASSISTANT_ID = "your_assistant_id"
BLOB_CONNECTION_STRING = "your_blob_connection_string"
BLOB_CONTAINER_NAME = "your_container_name"
COSMOS_ENDPOINT = "your_cosmos_endpoint"
COSMOS_KEY = "your_cosmos_key"
COSMOS_DB_NAME = "your_database_name"
COSMOS_CONTAINER_NAME = "your_container_name"
ACCOUNT_NAME = "your_storage_account_name"
ACCOUNT_KEY = "your_storage_account_key"
```

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your environment variables
4. Run: `streamlit run application.py`