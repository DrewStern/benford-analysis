#!/bin/bash

# install poetry and update to latest version if needed
pip install --user poetry
poetry_command="poetry self update"
poetry_command_result=$(${poetry_command})
poetry_version_message="You are using the latest version"
if [[ ${poetry_command_result} == ${poetry_version_message} ]]; then
  echo ${poetry_command}": ALREADY UP TO DATE"
else
  echo ${poetry_command}": UPDATING"
  # TODO: need more details here?
  echo ${poetry_command}": UPDATED"
fi
