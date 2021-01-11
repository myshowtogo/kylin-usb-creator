%define debug_package %{nil}
Name:           kylin-usb-creator
Version:        1.0.0
Release:        1
Summary:        kylin-usb-creator
License:        GPL-3+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qtchooser
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconf
BuildRequires:  gsettings-qt-devel

# Requires: NetworkManager

%description
 kylin-usb-creator

%prep
%setup -q

%build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  kylin-usb-creator.pro
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}/etc/bin/
mkdir -p %{buildroot}/usr/share/doc/kylin-usb-creator/
mkdir -p %{buildroot}/usr/share/man/man1/
cp debian/copyright  %{buildroot}/usr/share/doc/kylin-usb-creator/
gzip -c debian/changelog > %{buildroot}/usr/share/doc/kylin-usb-creator/changelog.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/kylin-usb-creator
%{_datadir}/applications/kylin-usb-creator.desktop
%{_datadir}/doc/kylin-usb-creator/changelog.gz
%{_datadir}/doc/kylin-usb-creator/copyright
%{_datadir}/pixmaps/kylin-usb-creator.png

%changelog
* Tue Dec 15 2020 lvhan <lvhan@kylinos.cn> - 1.0.0-1
- update to upstream version 1.0.0-26kord
