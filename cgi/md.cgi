#!/bin/zsh

echo "Content-Type: text/html; charset=UTF-8"
echo

local file="/home/eliot/press${PATH_INFO}"

echo $(pwd:top)

if [[ "${file}" == "/home/eliot/press/" ]]; then
   file="/home/eliot/press/README.md"
fi
echo "File: ${file}"

if ! /home/eliot/flowshell/commands/file:exists "${file}"; then
   echo "Bad Path"
   exit
fi

if /home/eliot/flowshell/commands/path:root:above "/home/eliot/press" "${file}"; then
   echo "Bad Path"
   exit
else 
   echo "<html>"
   echo "<body>"
   echo "${file}" 
   pandoc "${file}" 
   echo "</body>"
   echo "</html>"
fi
