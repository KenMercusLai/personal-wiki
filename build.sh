#!/usr/bin/env bash
set -euo pipefail

HUGO_VERSION=0.163.3
CACHE_DIR="${PWD}/.cache/hugo-${HUGO_VERSION}"
BIN_DIR="${CACHE_DIR}/bin"
HUGO_BIN="${BIN_DIR}/hugo"

install_hugo() {
  local os arch asset archive checksums expanded
  os=$(uname -s)
  arch=$(uname -m)
  mkdir -p "${BIN_DIR}"
  archive="${CACHE_DIR}/archive"
  checksums="${CACHE_DIR}/checksums.txt"

  case "${os}:${arch}" in
    Linux:x86_64) asset="hugo_${HUGO_VERSION}_linux-amd64.tar.gz" ;;
    Linux:aarch64|Linux:arm64) asset="hugo_${HUGO_VERSION}_linux-arm64.tar.gz" ;;
    Darwin:arm64|Darwin:x86_64) asset="hugo_${HUGO_VERSION}_darwin-universal.pkg" ;;
    *) echo "Unsupported build platform: ${os} ${arch}" >&2; exit 1 ;;
  esac

  curl -fsSL -o "${checksums}" "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_checksums.txt"
  curl -fsSL -o "${archive}" "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${asset}"
  python3 - "${checksums}" "${asset}" "${archive}" <<'PY'
import hashlib, pathlib, sys
checksums, asset, archive = map(pathlib.Path, sys.argv[1:])
expected = None
for line in checksums.read_text(encoding="utf-8").splitlines():
    parts = line.split()
    if len(parts) >= 2 and parts[-1].lstrip("*") == asset.name:
        expected = parts[0].lower()
        break
if expected is None:
    raise SystemExit(f"No checksum found for {asset.name}")
actual = hashlib.sha256(archive.read_bytes()).hexdigest()
if actual != expected:
    raise SystemExit(f"Checksum mismatch for {asset.name}: {actual} != {expected}")
print(f"Verified {asset.name}: {actual}")
PY

  if [[ "${asset}" == *.pkg ]]; then
    expanded="${CACHE_DIR}/expanded"
    rm -rf "${expanded}"
    pkgutil --expand-full "${archive}" "${expanded}"
    cp "${expanded}/Payload/hugo" "${HUGO_BIN}"
  else
    tar -C "${BIN_DIR}" -xzf "${archive}" hugo
  fi
  chmod 0755 "${HUGO_BIN}"
}

if [[ ! -x "${HUGO_BIN}" ]] || [[ "$("${HUGO_BIN}" version 2>/dev/null)" != *"v${HUGO_VERSION}"* ]]; then
  install_hugo
fi

"${HUGO_BIN}" version
python3 -m tools.validate_publish
python3 -m tools.postprocess_publish
"${HUGO_BIN}" --gc --minify --cleanDestinationDir "$@"
