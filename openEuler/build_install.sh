#!/bin/bash

pkg_name=kylin-usb-creator
version=1.0.0

echo "安装依赖环境"
pwd
yum-builddep $pkg_name.spec
cp $pkg_name.spec /root/rpmbuild/SPECS/
cd ../../
echo "压缩源码"
pwd
cp -r $pkg_name-fork/ $pkg_name-$version/
tar -zcvf $pkg_name-$version.tar.gz $pkg_name-$version/
cp $pkg_name-$version.tar.gz /root/rpmbuild/SOURCES/
rm -rf $pkg_name-$version/
mv $pkg_name-$version.tar.gz $pkg_name-fork/openEuler
echo "编译源码包"
cd /root/rpmbuild/RPMS/x86_64/
rm $pkg_name*.x86_64.rpm
cd /root/rpmbuild/SPECS/
rpmbuild -ba $pkg_name.spec
echo "安装rpm包"
cd /root/rpmbuild/RPMS/x86_64/
rpm -ivh --replacefiles --force --nodeps $pkg_name*.x86_64.rpm
