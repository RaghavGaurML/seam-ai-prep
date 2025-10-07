param(
    [string]$branchName = $(throw "Please provide the branch name to delete.")
)

git checkout main
git pull origin main
git branch -d $branchName
git push origin --delete $branchName
git fetch --prune

Write-Host "Cleaned up branch: $branchName"
