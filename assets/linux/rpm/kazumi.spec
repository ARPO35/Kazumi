#  Kazumi RPM spec 文件
#  用法: rpmbuild --define 'version X.Y.Z' -bb kazumi.spec

Name:           kazumi
Version:        %{version}
Release:        1%{?dist}
Summary:        一款好用的追番软件
License:        GPL-3.0
URL:            https://github.com/Predidit/Kazumi

# 禁用源代码打包, 因为二进制已经由 Flutter 构建流程生成
AutoReqProv:    no
Requires:       libayatana-appindicator
Requires:       webkit2gtk4.1

%description
Kazumi 是一款使用 Flutter 开发的动漫观看软件, 支持在线观看与弹幕功能。

%install
# rpmbuild 会在执行 %install 前清空 BUILDROOT, 因此必须在此阶段安装文件。
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/Kazumi
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/icons/hicolor/512x512/apps

cp -a %{_sourcedir}/bundle/. %{buildroot}/opt/Kazumi/
install -Dm0644 %{_sourcedir}/io.github.Predidit.Kazumi.desktop %{buildroot}/usr/share/applications/io.github.Predidit.Kazumi.desktop
install -Dm0644 %{_sourcedir}/io.github.Predidit.Kazumi.png %{buildroot}/usr/share/icons/hicolor/512x512/apps/io.github.Predidit.Kazumi.png
ln -sf ../../opt/Kazumi/kazumi %{buildroot}/usr/bin/kazumi

%files
%dir /opt/Kazumi
/opt/Kazumi/*
/usr/bin/kazumi
/usr/share/applications/io.github.Predidit.Kazumi.desktop
/usr/share/icons/hicolor/512x512/apps/io.github.Predidit.Kazumi.png
