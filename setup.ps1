# setup.ps1
Write-Host "[SETUP] Starting Seam AI Prep environment setup..."

# Define paths for root .venv and the day-specific folder
$rootVenvPath = ".venv"
$dayFolder = "day_2_shell_venv_codebase"
$requirementsFile = Join-Path $dayFolder "requirements.txt"
$pyprojectFile = Join-Path $dayFolder "pyproject.toml"

# Create or reuse the virtual environment
if (-not (Test-Path $rootVenvPath)) {
    Write-Host "[SETUP] Creating virtual environment..."
    python -m venv $rootVenvPath
} else {
    Write-Host "[INFO] Using existing virtual environment..."
}

# Activate the virtual environment
& "$rootVenvPath\Scripts\Activate.ps1"

# SAFETY CHECK: Ensure Python and pip are running from the .venv
$pythonPath = (Get-Command python).Source
$pipPath = (Get-Command pip).Source
$venvResolvedPath = (Resolve-Path $rootVenvPath).Path

if ($pythonPath -notlike "$venvResolvedPath*") {
    Write-Host "[ERROR] Python is not running from $rootVenvPath! Currently using: $pythonPath"
    Write-Host "Aborting setup to avoid global installs."
    exit 1
}

if ($pipPath -notlike "$venvResolvedPath*") {
    Write-Host "[ERROR] Pip is not running from $rootVenvPath! Currently using: $pipPath"
    Write-Host "Aborting setup to avoid global installs."
    exit 1
}

Write-Host "[SAFE] Python and pip are correctly using $rootVenvPath."

# Upgrade pip to latest version
python -m pip install --upgrade pip

# Install day-specific dependencies from requirements.txt if it exists
if (Test-Path $requirementsFile) {
    Write-Host "[SETUP] Installing dependencies from $requirementsFile..."
    pip install -r $requirementsFile
} else {
    Write-Host "[WARN] No requirements.txt found for $dayFolder. Skipping dependency install."
}

# Copy day-specific pyproject.toml to root if it exists
if (Test-Path $pyprojectFile) {
    Write-Host "[SETUP] Copying $pyprojectFile to root project folder..."
    Copy-Item -Path $pyprojectFile -Destination "pyproject.toml" -Force
} else {
    Write-Host "[WARN] No pyproject.toml found for $dayFolder. Skipping."
}

# Prompt to run tests from the day folder if they exist
$runTests = Read-Host "Run tests? (y/n)"
if ($runTests -eq "y") {
    $testsPath = Join-Path $dayFolder "tests"
    if (Test-Path $testsPath) {
        Write-Host "[SETUP] Running tests from $testsPath..."
        pytest -q $testsPath
    } else {
        Write-Host "[WARN] No tests folder found for $dayFolder."
    }
}

# Create VSCode .vscode folder if it doesn't exist
$vscodeFolder = ".vscode"
if (-not (Test-Path $vscodeFolder)) {
    New-Item -ItemType Directory -Path $vscodeFolder | Out-Null
}

# Create VSCode settings.json if it doesn't exist
$settingsPath = Join-Path $vscodeFolder "settings.json"
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
