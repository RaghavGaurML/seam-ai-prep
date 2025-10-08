# powershell_scripts/setup.ps1
Write-Host "[SETUP] Starting Seam AI Prep environment setup..."

# Determine project root (one level up from this script)
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
$projectRoot = Split-Path -Parent $scriptPath
Set-Location $projectRoot

# Define paths
$rootVenvPath = ".venv"
$requirementsFile = "requirements.txt"
$pyprojectFile = "pyproject.toml"

# -------------------------------------------------------
# 1. Create or reuse virtual environment
# -------------------------------------------------------
if (-not (Test-Path $rootVenvPath)) {
    Write-Host "[SETUP] Creating virtual environment..."
    python -m venv $rootVenvPath
} else {
    Write-Host "[INFO] Using existing virtual environment..."
}

# Activate the virtual environment
& "$rootVenvPath\Scripts\Activate.ps1"

# -------------------------------------------------------
# 2. Safety check – ensure Python and pip come from .venv
# -------------------------------------------------------
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

# -------------------------------------------------------
# 3. Upgrade pip
# -------------------------------------------------------
python -m pip install --upgrade pip

# -------------------------------------------------------
# 4. Install dependencies
# -------------------------------------------------------
if (Test-Path $requirementsFile) {
    Write-Host "[SETUP] Installing dependencies from $requirementsFile..."
    pip install -r $requirementsFile
} else {
    Write-Host "[WARN] No requirements.txt found in root. Skipping dependency install."
}

# -------------------------------------------------------
# 5. Verify pyproject.toml exists
# -------------------------------------------------------
if (Test-Path $pyprojectFile) {
    Write-Host "[INFO] pyproject.toml detected — tools will use this for config."
} else {
    Write-Host "[WARN] No pyproject.toml found. Linting/config tools may not function properly."
}

# -------------------------------------------------------
# 6. Create VSCode workspace settings if not present
# -------------------------------------------------------
$vscodeFolder = ".vscode"
if (-not (Test-Path $vscodeFolder)) {
    New-Item -ItemType Directory -Path $vscodeFolder | Out-Null
}

$settingsPath = Join-Path $vscodeFolder "settings.json"
if (-not (Test-Path $settingsPath)) {
    $settings = @{
        "python.defaultInterpreterPath" = ".venv\\Scripts\\python.exe"
        "editor.formatOnSave" = $true
        "editor.codeActionsOnSave" = @{
            "source.organizeImports" = "explicit"
        }
        "python.formatting.provider" = "black"
        "python.sortImports.args" = @("--profile", "black")
        "python.linting.enabled" = $true
        "python.linting.ruffEnabled" = $true
        "python.linting.mypyEnabled" = $true
        "python.linting.pylintEnabled" = $false
        "python.languageServer" = "None"
        "[powershell]" = @{
            "editor.formatOnSave" = $false
        }
    }

    $settings | ConvertTo-Json -Depth 5 | Out-File -Encoding utf8 $settingsPath
    Write-Host "[DONE] .vscode/settings.json created."
} else {
    Write-Host "[INFO] .vscode/settings.json already exists. Skipping creation."
}

# -------------------------------------------------------
# 7. Optional: Prompt to run tests (if any exist)
# -------------------------------------------------------
$testsPath = "tests"
if (Test-Path $testsPath) {
    $runTests = Read-Host "Run tests in /tests? (y/n)"
    if ($runTests -eq "y") {
        Write-Host "[SETUP] Running pytest..."
        pytest -q $testsPath
    }
}

Write-Host "[DONE] Seam AI Prep setup complete!"
