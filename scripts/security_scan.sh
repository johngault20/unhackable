#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
logs_dir="${repo_root}/logs"
mkdir -p "${logs_dir}"

{
  echo "=== Linux Mint security scan ==="
  echo "Generated at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo
  echo "--- System ---"
  uname -a
  echo
  echo "--- User ---"
  whoami
  id
  echo
  echo "--- Firewall ---"
  if command -v ufw >/dev/null 2>&1; then
    sudo ufw status verbose || echo "ufw status unavailable"
  else
    echo "ufw not installed"
  fi
  echo
  echo "--- Listening sockets ---"
  if command -v ss >/dev/null 2>&1; then
    ss -tulnp || true
  else
    echo "ss not installed"
  fi
  echo
  echo "--- Enabled services ---"
  if command -v systemctl >/dev/null 2>&1; then
    systemctl list-unit-files --type=service --state=enabled --no-legend 2>/dev/null | head -n 50 || true
  else
    echo "systemctl not available"
  fi
  echo
  echo "--- Authentication log tail ---"
  for log in /var/log/auth.log /var/log/secure; do
    if [[ -f "$log" ]]; then
      echo "--- $log ---"
      grep -Ei '(Failed password|Invalid user|Accepted password|sudo:|session opened|session closed)' "$log" 2>/dev/null | tail -n 40 || true
    fi
  done
  echo
  echo "--- Upgradable packages ---"
  if command -v apt >/dev/null 2>&1; then
    apt list --upgradable 2>/dev/null | head -n 20 || true
  else
    echo "apt not available"
  fi
  echo
  echo "--- Network note ---"
  if command -v nmap >/dev/null 2>&1; then
    echo "nmap is installed; use it only with permission and for manual review."
  else
    echo "nmap not installed; consider it later for manual port review."
  fi
  echo
  echo "--- Security note ---"
  echo "Do not expose your real Mint PC to the internet unless you fully understand the risk."
  echo "If you use a decoy, isolate it from your real machine and home network."
} > "${logs_dir}/last_scan.txt"

printf '[unhackable] Wrote scan report to %s\n' "${logs_dir}/last_scan.txt"
cat "${logs_dir}/last_scan.txt"
