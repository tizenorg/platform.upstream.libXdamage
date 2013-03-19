Name:           libXdamage
Version:        1.1.3
Release:        3
License:        MIT
Summary:        X Damage extension library
Url:            http://www.x.org
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(damageproto) >= 1.1.0
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros)

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

%build
%configure --disable-static 
make %{?_smp_mflags}

%install
%make_install
%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXdamage.so.1
%{_libdir}/libXdamage.so.1.1.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xdamage.h
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc
