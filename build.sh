#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "${ROOT}"

HUGO_VERSION=0.163.3
CACHE_DIR="${ROOT}/.cache/hugo-${HUGO_VERSION}"
BIN_DIR="${CACHE_DIR}/bin"
HUGO_BIN="${BIN_DIR}/hugo"
PUBLIC_DIR="${PUBLIC_DIR:-public}"

install_hugo() {
  local os arch asset expected archive actual expanded
  os=$(uname -s)
  arch=$(uname -m)
  mkdir -p "${BIN_DIR}"
  archive="${CACHE_DIR}/archive"

  case "${os}:${arch}" in
    Linux:x86_64)
      asset="hugo_${HUGO_VERSION}_linux-amd64.tar.gz"
      expected="ec422258f9a4ffc241de8707297e32311cd86fcc9b2813632617ff4d44935d91"
      ;;
    Linux:aarch64|Linux:arm64)
      asset="hugo_${HUGO_VERSION}_linux-arm64.tar.gz"
      expected="a4185cf0308ff3a61a2828563f70f476fcef30d02e9b00fb562eb1bd085195a5"
      ;;
    Darwin:arm64|Darwin:x86_64)
      asset="hugo_${HUGO_VERSION}_darwin-universal.pkg"
      expected="a59f749a6dbf613da9ec9c51ab670add0ca72b7eed6590bbff779a6fd6b70f0c"
      ;;
    *) echo "Unsupported build platform: ${os} ${arch}" >&2; exit 1 ;;
  esac

  curl -fsSL -o "${archive}" "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${asset}"
  actual=$(shasum -a 256 "${archive}" | cut -d ' ' -f 1)
  if [[ "${actual}" != "${expected}" ]]; then
    echo "Checksum mismatch for ${asset}: ${actual} != ${expected}" >&2
    exit 1
  fi
  echo "Verified ${asset}: ${actual}"

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
python3 scripts/prepare-overview-projections.py
python3 scripts/prepare-wiki-content.py
python3 scripts/prepare-overview-projections.py --check
python3 scripts/prepare-wiki-content.py --check
"${HUGO_BIN}" --gc --minify --cleanDestinationDir --destination "${PUBLIC_DIR}" "$@"
python3 scripts/verify_pages_output.py "${PUBLIC_DIR}"
