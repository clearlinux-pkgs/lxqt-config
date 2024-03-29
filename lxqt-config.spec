#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE793007AD22DF7E (tsujan2000@gmail.com)
#
Name     : lxqt-config
Version  : 1.2.0
Release  : 17
URL      : https://github.com/lxqt/lxqt-config/releases/download/1.2.0/lxqt-config-1.2.0.tar.xz
Source0  : https://github.com/lxqt/lxqt-config/releases/download/1.2.0/lxqt-config-1.2.0.tar.xz
Source1  : https://github.com/lxqt/lxqt-config/releases/download/1.2.0/lxqt-config-1.2.0.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: lxqt-config-bin = %{version}-%{release}
Requires: lxqt-config-data = %{version}-%{release}
Requires: lxqt-config-lib = %{version}-%{release}
Requires: lxqt-config-license = %{version}-%{release}
Requires: lxqt-config-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libkscreen-dev
BuildRequires : liblxqt-dev
BuildRequires : lxqt-build-tools
BuildRequires : pkg-config
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xorg-libinput)
BuildRequires : qtbase-dev
BuildRequires : qtsvg-dev
BuildRequires : qttools-dev
BuildRequires : qtx11extras-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# lxqt-config
## Overview
This repository is providing several tools involved in the configuration of both
LXQt and the underlying operating system.

%package bin
Summary: bin components for the lxqt-config package.
Group: Binaries
Requires: lxqt-config-data = %{version}-%{release}
Requires: lxqt-config-license = %{version}-%{release}

%description bin
bin components for the lxqt-config package.


%package data
Summary: data components for the lxqt-config package.
Group: Data

%description data
data components for the lxqt-config package.


%package lib
Summary: lib components for the lxqt-config package.
Group: Libraries
Requires: lxqt-config-data = %{version}-%{release}
Requires: lxqt-config-license = %{version}-%{release}

%description lib
lib components for the lxqt-config package.


%package license
Summary: license components for the lxqt-config package.
Group: Default

%description license
license components for the lxqt-config package.


%package man
Summary: man components for the lxqt-config package.
Group: Default

%description man
man components for the lxqt-config package.


%prep
%setup -q -n lxqt-config-1.2.0
cd %{_builddir}/lxqt-config-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676929620
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake .. -DWITH_MONITOR=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676929620
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-config
cp %{_builddir}/lxqt-config-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/lxqt-config/7fab4cd4eb7f499d60fe183607f046484acd6e2d || :
cp %{_builddir}/lxqt-config-%{version}/lxqt-config-monitor/LICENSE %{buildroot}/usr/share/package-licenses/lxqt-config/f0aaeb9183bca4511d21c13a39052e24f3774645 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-config
/usr/bin/lxqt-config-appearance
/usr/bin/lxqt-config-brightness
/usr/bin/lxqt-config-file-associations
/usr/bin/lxqt-config-input
/usr/bin/lxqt-config-locale

%files data
%defattr(-,root,root,-)
/usr/share/applications/lxqt-config-appearance.desktop
/usr/share/applications/lxqt-config-brightness.desktop
/usr/share/applications/lxqt-config-file-associations.desktop
/usr/share/applications/lxqt-config-input.desktop
/usr/share/applications/lxqt-config-locale.desktop
/usr/share/applications/lxqt-config.desktop
/usr/share/desktop-directories/lxqt-settings-lxqt.directory
/usr/share/desktop-directories/lxqt-settings-other.directory
/usr/share/desktop-directories/lxqt-settings-system.directory
/usr/share/icons/hicolor/48x48/apps/brightnesssettings.svg
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_ar.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_arn.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_ast.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_bg.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_ca.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_cs.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_cy.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_da.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_de.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_el.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_en_GB.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_eo.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_es.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_es_VE.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_et.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_eu.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_fa.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_fi.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_fr.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_gl.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_he.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_hi.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_hr.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_hu.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_ia.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_id.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_it.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_ja.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_ko.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_lt.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_nl.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_oc.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_pl.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_pt.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_pt_BR.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_ro_RO.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_ru.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_si.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_sk.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_sl.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_sr@latin.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_sr_BA.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_sr_RS.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_th_TH.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_tr.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_uk.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_vi.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_zh_CN.qm
/usr/share/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_zh_TW.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_ar.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_arn.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_ast.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_bg.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_ca.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_cs.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_cy.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_da.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_de.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_el.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_en_GB.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_es.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_et.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_fi.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_fr.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_gl.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_he.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_hr.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_hu.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_id.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_it.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_ja.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_ko.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_lt.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_lv.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_nl.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_pl.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_pt.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_pt_BR.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_ru.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_si.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_sk_SK.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_sl.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_tr.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_uk.qm
/usr/share/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_zh_CN.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_ar.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_arn.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_ast.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_bg.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_ca.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_cs.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_cy.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_da.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_de.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_el.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_en_GB.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_eo.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_es.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_es_VE.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_et.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_eu.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_fi.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_fr.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_gl.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_he.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_hi.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_hr.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_hu.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_id.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_it.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_ja.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_ko.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_lt.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_lv.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_nl.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_pl.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_pt.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_pt_BR.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_ro_RO.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_ru.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_si.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_sk_SK.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_sl.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_sv.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_th_TH.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_tr.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_uk.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_zh_CN.qm
/usr/share/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_zh_TW.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_ar.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_arn.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_ast.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_bg.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_ca.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_cs.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_cy.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_da.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_de.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_el.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_en_GB.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_es.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_et.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_fr.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_gl.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_he.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_hr.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_hu.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_id.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_it.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_ja.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_ko.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_lt.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_lv.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_nl.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_pl.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_pt.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_ru.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_si.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_sk_SK.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_sl.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_tr.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_uk.qm
/usr/share/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_zh_CN.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_af.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_ar.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_arn.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_ast.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_bg.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_bn.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_bn_IN.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_ca.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_cs.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_cy.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_da.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_de.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_el.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_en_GB.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_es.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_et.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_eu.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_fi.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_fr.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_gl.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_he.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_hr.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_hu.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_id.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_is.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_it.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_ja.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_ko.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_lt.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_nl.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_oc.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_pa.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_pl.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_pt.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_pt_BR.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_ru.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_si.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_sk_SK.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_sv.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_tr.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_uk.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_zh_CN.qm
/usr/share/lxqt/translations/lxqt-config-input/lxqt-config-input_zh_TW.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_ar.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_arn.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_ast.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_bg.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_ca.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_cs.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_cy.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_da.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_de.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_el.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_en_GB.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_es.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_et.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_fr.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_gl.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_he.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_hi.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_hr.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_hu.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_id.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_it.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_ja.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_ko.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_lt.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_lv.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_nl.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_oc.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_pl.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_pt.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_pt_BR.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_ru.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_si.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_sk_SK.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_sl.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_sv.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_tr.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_uk.qm
/usr/share/lxqt/translations/lxqt-config-locale/lxqt-config-locale_zh_CN.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_ar.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_arn.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_ast.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_bg.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_ca.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_cs.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_cy.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_da.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_de.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_el.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_en_GB.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_es.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_es_VE.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_et.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_eu.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_fa.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_fi.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_fr.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_gl.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_he.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_hr.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_hu.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_id.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_it.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_ja.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_ko.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_lt.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_lv.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_nl.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_oc.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_pl.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_pt.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_pt_BR.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_ro_RO.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_ru.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_si.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_sk_SK.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_sl.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_th_TH.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_tr.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_uk.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_vi.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_zh_CN.qm
/usr/share/lxqt/translations/lxqt-config/lxqt-config_zh_TW.qm

%files lib
%defattr(-,root,root,-)
/usr/lib64/lxqt-config/liblxqt-config-cursor.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxqt-config/7fab4cd4eb7f499d60fe183607f046484acd6e2d
/usr/share/package-licenses/lxqt-config/f0aaeb9183bca4511d21c13a39052e24f3774645

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lxqt-config-appearance.1
/usr/share/man/man1/lxqt-config-mouse.1
/usr/share/man/man1/lxqt-config.1
