Summary:	GTK Guitar Effects Processor
Summary(pl):	Procesor efektów gitarowych
Name:		gtkgep
Version:	0.2.3
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://www.macio.risp.pl/%{name}/files/%{name}-%{version}.tar.gz
# Source0-md5:	3405e30d600edc9885b27951792358dc
Source1:	%{name}.desktop
Patch0:		%{name}-paths.patch
URL:		http://gtkgep.prv.pl/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkGEP turns your computer into a realtime effects processor. You can
plug your guitar into the computer and play with cool distortion
effects, for example. It has a modular plugin structure, with standard
plugins including distortion, overdrive, delay, reverb, equalizers,
and a flanger. It works in 16-bit resolution, in mono mode, and with
frequencies from 11khz to 44khz. The sound quality is very good.

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*.so
%{_desktopdir}/%{name}.desktop
