Name:		stress-ng
Version:	0.15.00
Release:	1%{?dist}
Summary:	Stress test a computer system in various ways

License:	GPLv2+
URL:		https://github.com/ColinIanKing/%{name}/tarball
Source0:	https://github.com/ColinIanKing/%{name}/tarball/%{name}-%{version}.tar.xz

# Work around for ld.gold error
%undefine _package_note_flags

BuildRequires: make
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: kernel-headers
BuildRequires: keyutils-libs-devel
BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: lksctp-tools-devel
BuildRequires: libatomic
BuildRequires: zlib-devel
BuildRequires: Judy-devel

# Patches
Patch1: 0001-stress-sysfs-check-for-zero-sysfs-entries-after-prun.patch
Patch2: 0002-stress-shm-skip-stressor-if-dev-shm-is-not-mounted-w.patch
Patch3: 0003-stress-shm-move-dev-shm-check-to-earlier-in-the-setu.patch

%description
Stress test a computer system in various ways. It was designed to exercise
various physical subsystems of a computer as well as the various operating
system kernel interfaces.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build V=

%install
install -p -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -p -m 644 -D %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -pm 644 bash-completion/%{name} \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%changelog
* Mon Nov 21 2022 John Kacur <jkacur@redhat.com> - 0.15.00-1
- Rebase to upstream V0.15.00
- Add the following upstream patches
- stress-shm: move /dev/shm check to earlier in the setup phase
- stress-shm: skip stressor if /dev/shm is not mounted with tmpfs on linux
- stress-sysfs: check for zero sysfs entries after pruning the directory
Resolves: rhbz#2144070

* Tue Oct 18 2022 John Kacur <jkacur@redhat.com> - 0.14.06-1
- Rebase to upstream V0.14.06
Resolves: rhbz#2119871

* Fri Apr 22 2022 John Kacur <jkacur@redhat.com> - 0.14.00-2
- Add a local rpminspect.yaml file and disable badfuncs test
Resolves: rhbz#2077925

* Wed Apr 20 2022 John Kacur <jkacur@redhat.com> - 0.14.00-1
- Rebase to upstream V0.14.00
- Update Source URLs
Resolves: rhbz#2067588

* Fri Jan 14 2022 John Kacur <jkacur@redhat.com> - 0.13.10-1
- Rebase to upstres V0.13.10
Resolves; rhbz#2018597

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.13.00-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Aug 03 2021 John Kacur <jkacur@redhat.com> - 0.13.00-1
- Rebase to stress-ng-0.13.00 to get fix for build break with glibc-2.34
Resolves: rhbz#1984800

* Tue Jun 15 2021 John Kacur <jkacur@redhat.com> - 0.12.04-3
- Bump release number
Resolves: rhbz#1846033

* Tue Jun 15 2021 John Kacur <jkacur@redhat.com> - 0.12.04-2
- Revert to  0.12.04 and just build without libbsd
Resolves: rhbz#1846033

* Wed May 26 2021 John Kacur <jkacur@redhat.com> - 0.12.09-1
- Rebase to 0.12.09 upstream, and build without libbsd
Resolves: rhbz#1846033

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.12.04-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Mar 1 2021 Chris Brown <chris.brown@redhat.com> - 0.12.04-1
- Update to 0.12.04

* Wed Feb 24 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 0.12.03-2
- Enable ppc64le

* Mon Feb 15 2021 Chris Brown <chris.brown@redhat.com> - 0.12.03-1
- Update to 0.12.03

* Sun Feb 7 2021 Chris Brown <chris.brown@redhat.com> - 0.12.02-1
- Bump to 0.12.02

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Chris Brown <chris.brown@redhat.com> - 0.12.01-1
- Bump to 0.12.01

* Tue Dec 8 2020 Chris Brown <chris.brown@redhat.com> - 0.12.00-1
- Bump to 0.12.00

* Tue Dec 1 2020 Chris Brown <chris.brown@redhat.com> - 0.11.24-1
- Bump to 0.11.24

* Tue Nov 10 2020 Chris Brown <chris.brown@redhat.com> - 0.11.23-1
- Bump to 0.11.23
- Drop EPEL 8 Judy conditional

* Wed Sep 30 2020 Chris Brown <chris.brown@redhat.com> - 0.11.21-1
- Bump to 0.11.21

* Thu Sep 03 2020 Chris Brown <chris.brown@redhat.com> - 0.11.19-1
- Bump to 0.11.19

* Tue Aug 18 2020 Chris Brown <chris.brown@redhat.com> - 0.11.14-6
- Add Judy conditional for EPEL 8

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.14-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11.14-3
- Fix bash completion path

* Mon Jul 06 2020 Chris Brown <chris.brown@redhat.com> - 0.11.14-2
- Add bash completion
- Enable Judy, libatomic and libgcrypt
- Switch source and URL to https

* Fri Jul 03 2020 Chris Brown <chris.brown@redhat.com> - 0.11.14-1
- Bump to 0.11.14

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.07.29-8
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.07.29-5
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Fedora <sspreitz@redhat.com> - 0.07.29-2
- exclude ppc64 and ppc64le archs

* Tue Apr 18 2017 Fedora <sspreitz@redhat.com> - 0.07.29-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.07.05-3
- License is GPLv2+

* Sun Nov 20 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.07.05-2
- enhance building

* Sun Nov 20 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.07.05-1
- new version

* Mon Nov 14 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.07.04-1
- new version

* Mon Jun 13 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.06.06-1
- new version

* Fri Apr 29 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.05.25-1
- initial spec file

