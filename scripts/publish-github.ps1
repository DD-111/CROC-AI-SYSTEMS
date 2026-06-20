# Publish public artifact repo to GitHub (run after: gh auth login)
$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

$RepoName = "croc-ai-systems"

gh auth status
if ($LASTEXITCODE -ne 0) {
    Write-Host "Run: gh auth login -h github.com -p https -w"
    exit 1
}

git branch -M main
gh repo create $RepoName --public --source . --remote origin --description "CROC AI Systems by Croc Nexus AI Technologies" --push

Write-Host ""
Write-Host "Published: https://github.com/$(gh api user -q .login)/$RepoName"
