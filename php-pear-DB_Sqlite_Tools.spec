%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	Sqlite
%define		_ssclass	Tools
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_%{_ssclass}

Summary:	%{_pearname} - OO interface designed to effectively manage and backup Sqlite databases
Summary(pl):	%{_pearname} - zorientowany obiektowo interfejs do efektywnego zarz±dzania bazami Sqlite
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	53273574b1ab5a153feda07ba56b0154
URL:		http://pear.php.net/package/DB_Sqlite_Tools/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_Sqlite_Tools is extends the native PHP-sqlite function by providing
a comprehensive solution for database backup, live replication, export
in XML format, performance optmization and more. It is designed for
the maintenance and optimisation of several sqlite databases.

In PEAR status of this package is: %{_status}.

%description -l pl
DB_Sqlite_Tools rozszerza natywne funkcje PHP do obs³ugi sqlite
dostarczaj±c kompletnego rozwi±zania do tworzenia kopii zapasowych baz
danych, replikacji "na ¿ywo", eksportowania danych do formatu XML,
optymalizacji szybko¶ci. Klasa ta zosta³a zaprojektowana do obs³ugi
wielu baz danych sqlite.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/%{_ssclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_ssclass}*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/%{_ssclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/%{_subclass}
