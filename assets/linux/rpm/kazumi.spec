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
# 此文件由外部脚本负责将文件复制到 BUILDROOT, 因此 %install 阶段不做任何操作。
:

%post
# 安装后创建软链接并赋予执行权限
ln -sf /opt/Kazumi/kazumi /usr/bin/kazumi
chmod +x /usr/bin/kazumi

%postun
# 卸载后清理软链接
rm -f /usr/bin/kazumi

%files
/opt/Kazumi
/opt/Kazumi/*
/usr/share/applications/io.github.Predidit.Kazumi.desktop
/usr/share/icons/hicolor/512x512/apps/io.github.Predidit.Kazumi.png
