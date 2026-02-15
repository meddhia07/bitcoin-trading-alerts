# Bitcoin Alert System - Setup Script (Windows PowerShell)

# This script automates the setup of the Bitcoin Alert System on Windows.
# It checks for Python, creates a virtual environment, installs dependencies, and prepares environment files.

Write-Host "🚀 Setting up Bitcoin Alert System..."

# Check if Python is installed
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "❌ Python is not installed. Please install Python 3.8 or higher."
    exit 1
}

Write-Host "✅ Python found: $(python --version)"

# Create virtual environment
Write-Host "📦 Creating virtual environment..."
python -m venv .venv

# Activate virtual environment
Write-Host "🔌 Activating virtual environment..."
. .venv/Scripts/Activate.ps1

# Install dependencies
Write-Host "📥 Installing dependencies..."
pip install --upgrade pip
pip install requests twilio python-dotenv

# Create .env file if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "📝 Creating .env file..."
    Set-Content .env "# Add your API keys here\nNEWS_API_KEY=\nTWILIO_ACCOUNT_SID=\nTWILIO_AUTH_TOKEN=\nTWILIO_FROM_NUMBER=\nTWILIO_TO_NUMBER="
    Write-Host "⚠️ Please edit .env file and add your API keys!"
} else {
    Write-Host "✅ .env file already exists"
}

Write-Host ""
Write-Host "✅ Setup complete!"
Write-Host ""
Write-Host "📋 Next steps:"
Write-Host "1. Edit .env file and add your API keys"
Write-Host "2. Run: python main.py"
Write-Host ""
