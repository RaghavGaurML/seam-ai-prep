# setup.ps1

Write-Host "[SETUP] Starting Seam AI Prep environment setup..."

# Create or reuse virtual environment
if (-not (Test-Path ".venv")) {
    Write-Host "[SETUP] Creating virtual environment..."
    python -m venv .venv
} else {
    Write-Host "[INFO] Using existing virtual environment..."
}

# Activate the virtual environment
& .\.venv\Scripts\Activate.ps1

# --- SAFETY CHECK: Ensure we're using the correct Python and pip ---
$pythonPath = (Get-Command python).Source
$pipPath = (Get-Command pip).Source
$venvPath = (Resolve-Path ".\.venv").Path

if ($pythonPath -notlike "$venvPath*") {
    Write-Host "[ERROR] Python is not running from .venv! Currently using: $pythonPath"
    Write-Host "Aborting setup to avoid global installs."
    exit 1
}

if ($pipPath -notlike "$venvPath*") {
    Write-Host "[ERROR] Pip is not running from .venv! Currently using: $pipPath"
    Write-Host "Aborting setup to avoid global installs."
    exit 1
}

Write-Host "[SAFE] Python and pip are correctly using .venv."

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies if requirements.txt exists
if (Test-Path "requirements.txt") {
    Write-Host "[SETUP] Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Host "[WARN] No requirements.txt found. Skipping dependency install."
}

# Run tests if tests folder exists (optional)
$runTests = Read-Host "Run tests? (y/n)"
if ($runTests -eq "y") {
    if (Test-Path tests) {
        Write-Host "[SETUP] Running tests..."
        pytest -q
    } else {
        Write-Host "[WARN] No tests folder found."
    }
}

# Create VSCode settings.json if it doesn't exist
if (-not (Test-Path ".vscode")) {
    New-Item -ItemType Directory -Path ".vscode" | Out-Null
}

$settingsPath = ".vscode\settings.json"

if (-not (Test-Path $settingsPath)) {

    $settings = @{
        "python.pythonPath" = "venv\\Scripts\\python.exe"
        "editor.formatOnSave" = $true
        "editor.codeActionsOnSave" = @{
            "source.organizeImports" = $true
        }
        "python.formatting.provider" = "black"
        "python.sortImports.args" = @("--profile", "black")
        "python.linting.enabled" = $true
        "python.linting.ruffEnabled" = $true
        "python.linting.ruffArgs" = @("--fix")
        "python.linting.pylintEnabled" = $false
        "python.languageServer" = "None"
        "python.formatting.blackArgs" = @()
        "[powershell]" = @{
            "editor.formatOnSave" = $false
        }
    }

    $settings | ConvertTo-Json -Depth 5 | Out-File -Encoding utf8 $settingsPath
    Write-Host "[DONE] .vscode/settings.json created."

} else {
    Write-Host "[INFO] .vscode/settings.json already exists. Skipping creation."
}

Write-Host "[DONE] Seam AI Prep setup complete!"
