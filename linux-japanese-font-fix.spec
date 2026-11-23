%global baserelease 7

Name:           linux-japanese-font-fix
Version:        1.0.0
Release:        %{baserelease}%{?dist}
Summary:        Fontconfig configuration to fix Japanese font rendering on Fedora

License:        MIT
URL:            https://github.com/nogunix/linux-japanese-font-fix
# Each release is tagged v<Version>-<Release> (e.g. v1.0.0-7).
Source0:        %{url}/archive/refs/tags/v%{version}-%{baserelease}.tar.gz#/%{name}-%{version}-%{baserelease}.tar.gz

BuildArch:      noarch

Requires:       fontconfig
Requires:       google-noto-sans-cjk-vf-fonts
Requires:       google-noto-serif-cjk-vf-fonts
Requires:       google-noto-sans-mono-fonts
Requires:       google-noto-sans-mono-cjk-vf-fonts

%description
A robust Fontconfig setting to fix common Japanese font rendering issues (e.g.,
the "Chinese font problem") on Fedora systems, particularly when using a
non-Japanese locale.

This configuration (`50-user-jp-fonts.conf`) forces the system to use the
high-quality Noto CJK JP fonts for Japanese rendering.

%prep
%autosetup -n %{name}-%{version}-%{baserelease}

%build
# Nothing to build, just copy files

%install
mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d/
install -m 0644 50-user-jp-fonts.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/

%files
%license LICENSE
%doc README.md README.ja.md
%{_sysconfdir}/fonts/conf.d/50-user-jp-fonts.conf

%post
/usr/bin/fc-cache -f >/dev/null || :

%postun
/usr/bin/fc-cache -f >/dev/null || :

%changelog
* Mon Nov 23 2026 Nogunix <nogunix@gmail.com> - 1.0.0-7
- Fix monospace rule: use <string> instead of <family> inside <edit>,
  which fontconfig silently ignored
- Point Source0 at the per-release tag (v1.0.0-7) so downloaded sources
  contain the fix

* Wed Nov 11 2026 Nogunix <nogunix@gmail.com> - 1.0.0-6
- Add aarch64 chroots to Copr

* Sun Nov 08 2026 Nogunix <nogunix@gmail.com> - 1.0.0-5
- Add support for Fedora 45
- Drop EOL Fedora 41 and 42 chroots from Copr

* Mon Apr 27 2026 Nogunix <nogunix@gmail.com> - 1.0.0-4
- Add support for Fedora 43 and 44

* Sun Nov 02 2025 Nogunix <nogunix@gmail.com> - 1.0.0-3
- Switch to GitHub source tarball

