%global pkgname roboto
%global srcname %{pkgname}-unhinted
%global fontname google-roboto
%global fontconf 64-%{fontname}

Name: fonts-ttf-roboto
Version: 2.138
Release: 6
Summary: Google Roboto fonts
# Only the metainfo.xml files are CC0
License: ASL 2.0 and CC0
URL: https://github.com/googlefonts/roboto
Source0: https://github.com/googlefonts/roboto/releases/download/v%{version}/%{srcname}.zip#/%{srcname}-%{version}.zip
Source1: %{fontconf}-condensed-fontconfig.conf
Source2: %{fontconf}-fontconfig.conf
Source3: %{fontname}-condensed.metainfo.xml
Source4: %{fontname}.metainfo.xml
BuildArch: noarch
%rename google-roboto-fonts

%description
Roboto is a sans-serif typeface family introduced with Android Ice Cream
Sandwich operating system. Google describes the font as "modern, yet
approachable" and "emotional".

%package condensed
Summary: Google Roboto condensed fonts
%rename google-roboto-condensed-fonts

%description condensed
Google Roboto condensed fonts.

%prep
%autosetup -c -n %{srcname}

%build

%install
# install fonts
install -m 0755 -d %{buildroot}%{_datadir}/fonts/TTF/roboto
install -m 0644 -p Roboto*.ttf %{buildroot}%{_datadir}/fonts/TTF/roboto

# install fontconfig files
install -m 0755 -d %{buildroot}%{_datadir}/fontconfig/conf.avail \
                   %{buildroot}%{_sysconfdir}/fonts/conf.d
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/fontconfig/conf.avail/%{fontconf}.conf
install -m 0644 -p %{SOURCE1} %{buildroot}%{_datadir}/fontconfig/conf.avail/%{fontconf}-condensed.conf
for fconf in %{fontconf}.conf %{fontconf}-condensed.conf; do
  ln -s %{_datadir}/fontconfig/conf.avail/$fconf %{buildroot}%{_sysconfdir}/fonts/conf.d/$fconf
done

# install appdata
install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE3} %{SOURCE4} %{buildroot}%{_datadir}/appdata

%files
%{_datadir}/fonts/TTF/roboto/Roboto-*.ttf
%{_datadir}/fontconfig/conf.avail/%{fontconf}.conf
%{_sysconfdir}/fonts/conf.d/%{fontconf}.conf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%license LICENSE

%files condensed
%{_datadir}/fonts/TTF/roboto/RobotoCondensed-*.ttf
%{_datadir}/fontconfig/conf.avail/%{fontconf}-condensed.conf
%{_sysconfdir}/fonts/conf.d/%{fontconf}-condensed.conf
%{_datadir}/appdata/%{fontname}-condensed.metainfo.xml
%license LICENSE
