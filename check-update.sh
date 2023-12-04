#!/bin/sh
git ls-remote --tags https://github.com/googlefonts/roboto |grep -v '\^{}' |awk '{ print $2; }' |tail -n1 |sed -e 's,refs/tags/v,,'
