Summary:	GTK+ Guitar Effects Processor
Summary(pl.UTF-8):   Procesor efektów gitarowych oparty na GTK+
Name:		gtkgep
Version:	0.2.3
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://www.macio.risp.pl/%{name}/files/%{name}-%{version}.tar.gz
# Source0-md5:	3405e30d600edc9885b27951792358dc
Source1:	%{name}.desktop
Patch0:		%{name}-paths.patch
URL:		http://gtkgep.prv.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkGEP turns your computer into a realtime effects processor. You can
plug your guitar into the computer and play with cool distortion
effects, for example. It has a modular plugin structure, with standard
plugins including distortion, overdrive, delay, reverb, equalizers,
and a flanger. It works in 16-bit resolution, in mono mode, and with
frequencies from 11kHz to 44kHz. The sound quality is very good.

%description -l pl.UTF-8
GtkGEP zamienia komputer w procesor efektów działający w czasie
rzeczywistym. Można podłączyć gitarę do komputera i grać z efektem np.
przesteru. Program ma modularną strukturę wtyczek. Załączone
standardowe wtyczki zawierają przester (distortion), overdrive,
opóźnienie (delay), pogłos (reverb), equalizery i flanger. Procesor
działa z rozdzielczością 16-bitową, w trybie monofonicznym oraz z
częstotliwościami próbkowania od 11kHz do 44kHz. Jakość dźwięku jest
bardzo dobra.

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
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%{_desktopdir}/%{name}.desktop
