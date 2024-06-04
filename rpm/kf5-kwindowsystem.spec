%global kf5_version 5.108.0

Name: opt-kf5-kwindowsystem
Version: 5.108.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 1 integration module with classes for windows management

License: LGPLv2+ and MIT
URL:     https://invent.kde.org/frameworks/kwindowsystem

Source0: %{name}-%{version}.tar.bz2

# filter plugin provides
%{?opt_kf5_default_filter}

BuildRequires: make
BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros >= %{kf5_version}
#BuildRequires:  pkgconfig(x11)
#BuildRequires:  pkgconfig(xcb)
#BuildRequires:  pkgconfig(xcb-icccm)
#BuildRequires:  pkgconfig(xcb-keysyms)
#BuildRequires:  pkgconfig(xfixes)
#BuildRequires:  pkgconfig(xrender)
BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qttools-devel
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui


%description
KDE Frameworks Tier 1 integration module that provides classes for managing and
working with windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang_kf5 kwindowsystem5_qt


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/kwindowsystem.*
%{_opt_kf5_libdir}/libKF5WindowSystem.so.*
#dir #{_opt_kf5_plugindir}/kwindowsystem/
#{_kf5_plugindir}/kwindowsystem/KF5WindowSystemWaylandPlugin.so
%{_opt_kf5_datadir}/locale/

%files devel
%{_opt_kf5_includedir}/KF5/KWindowSystem/
%{_opt_kf5_libdir}/libKF5WindowSystem.so
%{_opt_kf5_libdir}/cmake/KF5WindowSystem/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KWindowSystem.pri

