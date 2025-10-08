Name:		stress-ng
Version:	0.18.06
Release:	10%{?dist}
Summary:	Stress test a computer system in various ways

License:	GPL-2.0-or-later
URL:		https://github.com/ColinIanKing/stress-ng
Source0:	https://github.com/ColinIanKing/stress-ng/archive/V%{version}/%{name}-%{version}.tar.xz

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	glibc-devel
BuildRequires:	kernel-headers
BuildRequires:	keyutils-libs-devel
BuildRequires:	libaio-devel
BuildRequires:	libattr-devel
%if %{undefined rhel}
BuildRequires:	libbsd-devel
%endif
BuildRequires:	libcap-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	lksctp-tools-devel
BuildRequires:	libatomic
BuildRequires:	zlib-devel
BuildRequires:	Judy-devel

# Patches
Patch1: core-stress-fflush-opened-writable-files.patch
Patch2: stress-fp-error-remove-duplicated-sqrt.patch
Patch3: README.md-add-another-kernel-commit-to-the-2024-kern.patch
Patch4: core-shim-add-shim-to-ppoll-and-workaround-fortifica.patch
Patch5: core-shim-use-shim-d-types-for-shim_poll-args.patch
Patch6: core-shim-limit-_FORTIFY_SOURCE-to-2-for-ALT-linux-g.patch
Patch7: core-target-clones-add-more-power9-10-11-target-clon.patch
Patch8: stress-brk-ensure-the-failure-sbrk-errno-is-being-ch.patch
Patch9: stress-ng-Add-fPIC-to-Makefile.patch

%description
Stress test a computer system in various ways. It was designed to exercise
various physical subsystems of a computer as well as the various operating
system kernel interfaces.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

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
* Fri Feb 14 2025 John Kacur <jkacur@redhat.com> - 0.18.06-10
- Change the rpminspect.yaml with instructions from David Cantrell
Resolves: RHEL-33521

* Tue Feb 11 2025 John Kacur <jkacur@redhat.com> - 0.18.06-9
- Add -fPIC flag to improve annocheck results
Resolves: RHEL-33521

* Thu Jan 30 2025 John Kacur <jkacur@redhat.com> - 0.18.06-8
- Moving the annocheck rules back from gating.yaml to rpminspect.yaml
Resolves: RHEL-33521

* Thu Jan 30 2025 John Kacur <jkacur@redhat.com> - 0.18.06-7
- Adding annocheck rules to gating.yaml
Resolves: RHEL-33521

* Fri Jan 24 2025 John Kacur <jkacur@redhat.com> - 0.18.06-6
- Due to the special nature of stress-ng, it's not even possible to compile
  with -fpic or -fPIC, so turning annocheck off
Resolves: RHEL-33521

* Thu Jan 23 2025 John Kacur <jkacur@redhat.com> - 0.18.06-05
- Adding --skip-dynamic-tags to exceptions in rpminspect.yaml
Resolves: RHEL-33521

* Wed Nov 20 2024 John Kacur <jkacur@redhat.com> - 0.18.06-04
- Adding some annocheck exception changes to rpminspect
Resolves: RHEL-33521

* Wed Nov 06 2024 John Kacur <jkacur@redhat.com> - 0.18.06-3
- Remove the revert patch and replace it with an upstream fix for power
- Include all of the stress-ng patches available past 0.18.06
Resolves:RHEL-65475

* Tue Nov 05 2024 John Kacur <jkacur@redhat.com> - 0.18.06-2
- Revert a patch to use that creates a gcc flags mismatch on power
- Remove duplicate sqrt function
Resolves:RHEL-65475

* Fri Nov 01 2024 John Kacur <jkacur@redhat.com> - 0.18.06-1
- Rebase to stress-ng to V0.18.06
- Add single upstream patch
Resolves:RHEL-65475

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 0.17.08-8
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Thu Aug 01 2024 John Kacur <jkacur@redhat.com> - 0.17.08-7
- Turn off annocheck optimization, cf-protection and property-note checks
Resolves: RHEL-33521

* Tue Jul 16 2024 John Kacur <jkacur@redhat.com> - 0.17.08-6
- Add mising tests directory for gating
Resolves: RHEL-48237

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 0.17.08-5
- Bump release for June 2024 mass rebuild

* Mon Jun 17 2024 Anubhav <ashelat@redhat.com> - 0.17.08-4
- Use rhel-10 in gating.yaml instead of rhel-9
Resolves: RHEL-42975

* Thu May 23 2024 John Kacur <jkacur@redhat.com> - 0.17.08-3
- Rebase to V0.17.08 Upstream
- ARM: Don't declare inlined yield helper if yield not available
Resolves: RHEL-33305

* Tue Mar 26 2024 John Kacur <jkacur@redhat.com> - 0.17.03-3
- Added gating.yaml
- Added rpminspect.yam
- Added tests dir
Resolves: RHEL-30434

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 17 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.17.03-1
- Update to 0.17.03
- Fixes rhbz#2253639

* Mon Dec 04 2023 John Kacur <jkacur@redhat.com> - 0.17.01-2
- Update the License field to the SPDX format using the tools
  license-fedora2spdx and verified by license-validate

* Sat Nov 11 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.17.01-1
- Update to 0.17.01
- Fixes rhbz#2242847

* Wed Oct 11 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.17.00-1
- Update to 0.17.00
- Fixes rhbz#2242847

* Sun Oct 01 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.16.05-1
- Update to 0.16.05
- Fixes rhbz#2237812

* Mon Aug 14 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.16.04-1
- Update to 0.16.04
- Fixes rhbz#2231634

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.16.02-1
- Update to 0.16.02
- Fixes rhbz#2222484

* Sat Jul 08 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.16.00-1
- Update to 0.16.00
- Fixes rhbz#2221348

* Sat Jun 17 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.15.10-1
- Update to 0.15.10
- Fixes rhbz#2186552

* Mon Jun 05 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.15.06-2
- Disable libbsd dependency in RHEL builds

* Sat Mar 25 2023 Fabio Alessandro Locati <fale@fedoraproject.ora> - 0.15.06-1
- Update to 0.15.06
- Fixes rhbz#2179538

* Sat Mar 11 2023 Fabio Alessandro Locati <fale@fedoraproject.ora> - 0.15.05-1
- Update to 0.15.05
- Fixes rhbz#2130476

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Florian Weimer <fweimer@redhat.com> - 0.15.00-2
- Improve compatibility with strict(er) C99 compilers

* Wed Dec 07 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.15.00-1
- Update to 0.15.00

* Sat Sep 17 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.14.05-1
- Update to 0.14.05

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.14.02-1
- Update to 0.14.02

* Wed Feb 02 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.13.11-1
- Update to 0.13.11
- move source to github since the author changed company
- clean the build process

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Chris Brown <chris.brown@redhat.com> - 0.13.00-1
- Update to 0.13.00

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Chris Brown <chris.brown@redhat.com> - 0.12.10-1
- Update to 0.12.10

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

