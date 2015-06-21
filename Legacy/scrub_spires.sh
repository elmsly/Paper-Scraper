#!/bin/bash

[ $# -eq 0 ] && { echo "Usage: $0 preprint-number"; exit 1; }

while getopts ":d" opt; do
    case $opt in
          d)
              doiflag=true;
              shift;
              ;;
          \?)
            echo "Invalid option: -$OPTARG" >&2
          ;;
    esac
done

if [ $doiflag ]
then
  curl -s "http://inspirehep.net/search?ln=en&ln=en&p=find+doi+$1&of=hx&action_search=Search&sf=earliestdate&so=d&rm=&rg=25&sc=0" | awk 'BEGIN{flag=0} /pre/{flag=1-flag;first=1} flag&&(!first){print} first{first=0} '
else
  curl -s "http://inspirehep.net/search?ln=en&ln=en&p=find+eprint+$1&of=hx&action_search=Search&sf=earliestdate&so=d&rm=&rg=25&sc=0" | awk 'BEGIN{flag=0} /pre/{flag=1-flag;first=1} flag&&(!first){print} first{first=0} '
fi
