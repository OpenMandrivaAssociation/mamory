%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A Rom Management CLI
Name:		mamory
Version:	0.2.25
Release:	4
License:	GPL
Group:		Emulators
Source:		http://prdownloads.sourceforge.net/mamory/%{name}-%{version}.tar.bz2
URL:		http://mamory.sourceforge.net/
BuildRequires:	expat-devel

%package -n %{libname}
Summary:	A Rom Management Library
Group:		Emulators

%package -n %{develname}
Summary:	Devel package for libmamory
Group:		Emulators
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description
The Mamory CLI
This should be the part that most people will be looking for, at least 
until libmamory is used through the graphical user interface of a generic 
roms management application.

Use the Mamory CLI in order to manage a set of roms corresponding 
to any kind of emulators.

%description -n %{libname}
Mamory is a rom management library.
It allows developpers of emulation related projects to access useful 
functions in order to maintain roms sets.
It's based on the comparison on CRC32, size and name of the roms.
Therefore, it needs a source of informations that describes the roms set 
to maintain.

To demonstrate the functionalities offered by libmamory, Mamory 
is distributed with a command line interface (CLI) called "mamory".

%description -n %{develname}
Devel package for libmamory

%prep
%setup -q

%build
%configure2_5x
%make OPTFLAGS="%{optflags} -fPIC" CPPFLAGS="%{optflags} -fPIC"

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/%{name}

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%doc README
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/*

