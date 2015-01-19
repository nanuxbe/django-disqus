#!/bin/bash
version=`ls dist -1|grep -o "[0-9]\+\(\.[0-9]\+\)\+" |sort --version-sort |tail -n 1`
curl -X POST -F sdist=@dist/levit_admin-${version}.tar.gz http://legacy.home:8080/uploadpackage/
curl -X POST -F sdist=@dist/levit_admin-${version}.tar.gz http://vc.vlan:9000/uploadpackage/
