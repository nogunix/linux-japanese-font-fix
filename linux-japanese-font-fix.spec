Name:           linux-japanese-font-fix
Version:        1.0.0
Release:        3%{?dist}
Summary:        Fontconfig configuration to fix Japanese font rendering on Fedora

License:        MIT
URL:            https://github.com/nogunix/linux-japanese-font-fix
Source0:        https://github.com/nogunix/linux-japanese-font-fix/archive/refs/tags/v%{version}.tar.gz

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
%autosetup -n %{name}-%{version}

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
* Sun Nov 02 2025 Nogunix <nogunix@gmail.com> - 1.0-3
- Switch to GitHub source tarball

