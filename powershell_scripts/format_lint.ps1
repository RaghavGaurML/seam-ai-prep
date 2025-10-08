# ----------------------------------------
# format_lint.ps1 - Auto-format, lint, and type-check project
# ----------------------------------------
Write-Host "[START] Running project format/lint/type checks..."

# Activate virtual environment
$venvPath = ".venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    & $venvPath
} else {
    Write-Host "[WARN] Virtual environment not found! Please run setup.ps1 first."
    exit 1
}

# -------------------------------
# 1. Black - auto-format
# -------------------------------
Write-Host "[FORMAT] Running Black to auto-format files..."
black . --quiet

# -------------------------------
# 2. Ruff - auto-fix linting
# -------------------------------
Write-Host "[LINT] Running Ruff to check/fix linting issues..."
ruff check . --fix

# -------------------------------
# 3. Flake8 - safe reporting
# -------------------------------
# Write-Host "[LINT] Running Flake8 (safe mode, no hanging)..."
# # max-line-length matches Black, exit-zero avoids hanging in PowerShell
# # flake8 . --max-line-length=88 --exit-zero --statistics > flake8_report.txt
# Write-Host "[INFO] Flake8 finished. Check flake8_report.txt for details."

# -------------------------------
# 4. Mypy - type checking
# -------------------------------
Write-Host "[TYPE CHECK] Running Mypy..."
mypy .

Write-Host "[DONE] Format, lint, and type checks complete!"
