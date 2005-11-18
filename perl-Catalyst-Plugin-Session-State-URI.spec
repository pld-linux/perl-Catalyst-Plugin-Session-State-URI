#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Session-State-URI
Summary:	Catalyst::Plugin::Session::State::URI - Saves session IDs by rewriting URIs
#Summary(pl):	
Name:		perl-Catalyst-Plugin-Session-State-URI
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dd716fc598bed7e202b2632e92d08e5d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst-Plugin-Session >= 0.01
BuildRequires:	perl-Test-MockObject >= 1.01
BuildRequires:	perl-URI-Escape
BuildRequires:	perl-URI-Find >= 0.13
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In order for Catalyst::Plugin::Session to work the session ID needs to be
stored on the client, and the session data needs to be stored on the server.

This plugin cheats and instead of storing the session id on the client, it
simply embeds the session id into every URI sent to the user.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Catalyst/Plugin/Session/State/*.pm
%{perl_vendorlib}/Catalyst/Plugin/Session/State/URI
%{_mandir}/man3/*
