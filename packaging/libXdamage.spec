%bcond_with x

Name:           libXdamage
Version:        1.1.4
Release:        3
License:        MIT
Summary:        X Damage extension library
Url:            http://www.x.org
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXdamage.manifest

BuildRequires:  pkgconfig(damageproto) >= 1.1.0
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros)

%if !%{with x}
ExclusiveArch:
%endif

%description
X.Org X11 libXdamage runtime library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X.Org X11 libXdamage development package.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen --disable-static
make %{?_smp_mflags}

%install
%make_install
%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXdamage.so.1
%{_libdir}/libXdamage.so.1.1.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xdamage.h
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc
