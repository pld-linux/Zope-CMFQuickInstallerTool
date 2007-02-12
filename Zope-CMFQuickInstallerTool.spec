%define		zope_subname	CMFQuickInstallerTool
Summary:	A Zope product independent from the former CMFQuickInstaller
Summary(pl.UTF-8):   Dodatek do Zope niezależny od poprzedniego CMFQuickInstallera
Name:		Zope-%{zope_subname}
Version:	1.5.7
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://plone.org/products/cmfquickinstallertool/releases/%{version}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	1f662098e304c11167a2c5e8ed46eb14
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
Requires:	Zope-CMF
Conflicts:	CMF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
CMFQuickInstallerTool is a Zope product independent from the former
CMFQuickInstaller. The main difference to CMFQuickInstaller the
tracking of what a product creates during install.

%description -l pl.UTF-8
CMFQuickInstallerTool jest dodatkiem do Zope niezależnym od
poprzedniego CMFQuickInstallera. Główna różnica w stosunku do
CMFQuickInstallera to możliwość śledzenia, co tworzy dany produkt w
czasie instalacji.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,forms,interfaces,tests,*.py,*.gif,version.txt,actions,properties} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS README.txt ChangeLog DEPENDS HISTORY.txt PLIP.TXT READMEPATCH.TXT
%{_datadir}/%{name}
