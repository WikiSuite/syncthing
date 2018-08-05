Name:		syncthing
Version:	0.14.49
Release:	0%{?dist}
Summary:	Open, trustworthy and decentralized sync
# Set to amd64 or 386
%define arch	amd64

Group:		Applications/System
License:	MPLv2
URL:		https://github.com/syncthing/syncthing
Source0:	https://github.com/syncthing/syncthing/releases/download/v%{version}/syncthing-linux-%{arch}-v%{version}.tar.gz

Requires:	policycoreutils-python

%description
Syncthing replaces proprietary sync and cloud services with something open,
trustworthy and decentralized. Your data is your data alone and you deserve
to choose where it is stored, if it is shared with some third party and how
it's transmitted over the Internet.

%prep
tar -zxf %{SOURCE0}
cd syncthing-linux-%{arch}-v%{version}/

%install
mkdir -p %{buildroot}/usr/bin/
cd syncthing-linux-%{arch}-v%{version}/
cp syncthing %{buildroot}/usr/bin/

mkdir -p %{buildroot}/etc/systemd/system/
cp etc/linux-systemd/system/syncthing\@.service  %{buildroot}/etc/systemd/system/
cp etc/linux-systemd/system/syncthing-resume.service  %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}/etc/systemd/user/
cp etc/linux-systemd/user/syncthing.service %{buildroot}/etc/systemd/user/


%files
%defattr(-,root,root)
/usr/bin/syncthing
/etc/systemd/system/syncthing@.service
/etc/systemd/system/syncthing-resume.service
/etc/systemd/user/syncthing.service

%changelog
* Sat Aug 04 2018 Serge Kishiko <s.kishiko@itotafrica.com>
- Bump synthing version 0.14.47 -> 0.14.49
* Thu Dec 14 2017 Benjamin Chambers <benjamin@egloo.ca>
- Bump synthing version 0.14.26 -> 0.14.41
* Mon Apr 03 2017 Benjamin Chambers <benjamin@egloo.ca>
- Bump synthing version 0.14.13 -> 0.14.26
* Wed Nov 30 2016 Benjamin Chambers <benjamin@egloo.ca>
- Bump synthing version 0.14.9 -> 0.14.13
* Mon Oct 24 2016 Benjamin Chambers <benjamin@egloo.ca>
- Bump synthing version 0.13.1 -> 0.14.7
* Thu Sep 22 2016 Logan Owen <logan@s1network.com>
- Bump synthing version 0.13.1 -> 0.14.7

* Mon Feb 08 2016 Martin Lazarov <martin@lazarov.bg>
- Initial spec version
