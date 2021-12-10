RED="\e[31m"
CYAN="\e[36m"
END="\e[0m"

log_info() {
  echo
  echo -e "${CYAN}${@}${END}"
}

die() {
  echo -e "${RED}ERROR:${END} ${@}"
  exit 1
}
