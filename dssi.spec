Summary:	Disposable Soft Synth Interface specification
Summary(pl.UTF-8):	Specyfikacja Disposable Soft Synth Interface
Name:		dssi
Version:	1.1.0
Release:	1
License:	LGPL v2.1
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/dssi/%{name}-%{version}.tar.gz
# Source0-md5:	dfc850e66fae94e7ec08aebb43d07848
Patch0:		%{name}-lib64.patch
URL:		http://dssi.sourceforge.net/
BuildRequires:	QtGui-devel >= 4.0.1
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel >= 1.0
BuildRequires:	liblo-devel >= 0.12
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DSSI (pronounced "dizzy") is an API for audio plugins, with particular
application for software synthesis plugins with native user
interfaces. DSSI is an open specification developed for use in Linux
audio applications, although portable to other platforms. It may be
thought of as LADSPA-for-instruments, or something comparable to VSTi.

DSSI consists of a C language API for use by plugins and hosts, based
on the LADSPA API, and an OSC (Open Sound Control) API for use in user
interface to host communications. The DSSI specification consists of
an RFC which describes the background for the proposal and defines the
OSC part of the specification, and a documented header file which
defines the C API.

%description -l pl.UTF-8
DSSI (wymawiane "dizzy") to API dla wtyczek dźwiękowych z
zastosowaniem szczególnie dla wtyczek syntezy programowej z natywnymi
interfejsami użytkownika. DSSI to otwarta specyfikacja stworzona do
używania w linuksowych aplikacjach dźwiękowych, ale przenośna na inne
platformy. Można ją określić jako LADSPA dla instrumentów lub coś
porównywalnego do VSTi.

DSSI składa się z API języka C do użytku przez wtyczki i hosty, oparte
o API LADSPA oraz API OSC (Open Sound Control) do użytku w
interfejsach użytkownika do komunikacji z hostem. Specyfikacja DSSI
składa się z RFC opisującego tło propozycji i definiującego część OSC
specyfikacji oraz udokumentowanego pliku nagłówkowego definiującego
API C.

%package devel
Summary:	DSSI development files
Summary(pl.UTF-8):	Pliki nagłówkowe DSSI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib-devel >= 0.9
Requires:	ladspa-devel >= 1.0
Obsoletes:	dssi < 1.0.0

%description devel
DSSI development files.

%description devel -l pl.UTF-8
Pliki nagłówkowe DSSI.

%package host-jack
Summary:	A simple JACK/ALSA-sequencer plugin host
Summary(pl.UTF-8):	Prosty host wtyczek sekwencera JACK/ALSA
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	liblo >= 0.12

%description host-jack
A simple JACK/ALSA-sequencer plugin host.

%description host-jack -l pl.UTF-8
Prosty host wtyczek sekwencera JACK/ALSA.

%package examples
Summary:	Example DSSI plugins
Summary(pl.UTF-8):	Przykładowe wtyczki DSSI
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description examples
Example DSSI plugins.

%description examples -l pl.UTF-8
Przykładowe wtyczki DSSI

%prep
%setup -q
%if "%{_lib}" == "lib64"
%patch0 -p1
%endif

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/dssi/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/TODO doc/*.txt
%attr(755,root,root) %{_bindir}/dssi_analyse_plugin
%attr(755,root,root) %{_bindir}/dssi_list_plugins
%attr(755,root,root) %{_bindir}/dssi_osc_send
%attr(755,root,root) %{_bindir}/dssi_osc_update
%dir %{_libdir}/dssi
%{_mandir}/man1/dssi*.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/dssi.h
%{_pkgconfigdir}/dssi.pc

%files host-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jack-dssi-host
%{_mandir}/man1/jack-dssi-host.1*

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karplong
%attr(755,root,root) %{_bindir}/less_trivial_synth
%attr(755,root,root) %{_bindir}/trivial_sampler
%attr(755,root,root) %{_bindir}/trivial_synth
%attr(755,root,root) %{_libdir}/dssi/*.so
%dir %{_libdir}/dssi/less_trivial_synth
%attr(755,root,root) %{_libdir}/dssi/less_trivial_synth/*_qt
%dir %{_libdir}/dssi/trivial_sampler
%attr(755,root,root) %{_libdir}/dssi/trivial_sampler/*_qt
