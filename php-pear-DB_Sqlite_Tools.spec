%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	Sqlite
%define		_ssclass	Tools
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_%{_ssclass}

Summary:	%{_pearname} - OO interface designed to effectively manage and backup Sqlite databases
Summary(pl):	%{_pearname} - zorientowany obiektowo interfejs do efektywnego zarz�dzania bazami Sqlite
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	4
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	53273574b1ab5a153feda07ba56b0154
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/DB_Sqlite_Tools/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:5.0.0
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
DB_Sqlite_Tools rozszerza natywne funkcje PHP do obs�ugi sqlite
dostarczaj�c kompletnego rozwi�zania do tworzenia kopii zapasowych baz
danych, replikacji "na �ywo", eksportowania danych do formatu XML,
optymalizacji szybko�ci. Klasa ta zosta�a zaprojektowana do obs�ugi
wielu baz danych sqlite.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}/%{_subclass}
%patch0 -p2

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
%{php_pear_dir}/%{_class}/%{_subclass}
