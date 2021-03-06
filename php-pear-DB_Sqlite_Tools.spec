%define		_status		alpha
%define		_pearname	DB_Sqlite_Tools
Summary:	%{_pearname} - OO interface designed to effectively manage and backup Sqlite databases
Summary(pl.UTF-8):	%{_pearname} - zorientowany obiektowo interfejs do efektywnego zarządzania bazami Sqlite
Name:		php-pear-%{_pearname}
Version:	0.1.7
Release:	3
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	299ccb57141801b5db7edaca54b6862d
URL:		http://pear.php.net/package/DB_Sqlite_Tools/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_Sqlite_Tools is extends the native PHP-sqlite function by providing
a comprehensive solution for database backup, live replication, export
in XML format, performance optmization and more. It is designed for
the maintenance and optimisation of several sqlite databases.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
DB_Sqlite_Tools rozszerza natywne funkcje PHP do obsługi sqlite
dostarczając kompletnego rozwiązania do tworzenia kopii zapasowych baz
danych, replikacji "na żywo", eksportowania danych do formatu XML,
optymalizacji szybkości. Klasa ta została zaprojektowana do obsługi
wielu baz danych sqlite.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# package build script
rm .%{php_pear_dir}/generate_package_xml.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/DB/Sqlite
%{php_pear_dir}/DB/Sqlite/Tools.php
%{php_pear_dir}/DB/Sqlite/Tools
