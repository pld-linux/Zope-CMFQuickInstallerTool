%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFQuickInstallerTool
Summary:	CMFQuickInstallerTool - a Zope product independent from the former CMFQuickInstaller
Summary(pl):	CMFQuickInstallerTool - dodatek do Zope niezale¿ny od poprzedniego CMFQuickInstallera
Name:		Zope-%{zope_subname}
Version:	1.3
Release:	1
License:	GNU
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}_%{version}.tgz
# Source0-md5:	60fff6fd03d1ab586479940561d17985
URL:		http://cvs.bluedynamics.org/viewcvs/CMFQuickInstallerTool/
%pyrequires_eq	python-modules
Requires:	CMF
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
CMFQuickInstallerTool is a Zope product independent from the former
CMFQuickInstaller. The main difference to CMFQuickInstaller the
tracking of what a product creates during install.

%description -l pl
CMFQuickInstallerTool jest dodatkiem do Zope niezale¿nym od
poprzedniego CMFQuickInstallera. G³ówna ró¿nica w stosunku do
CMFQuickInstallera to mo¿liwo¶æ ¶ledzenia, co tworzy dany produkt w
czasie instalacji.

%prep
%setup -q -c %{zope_subname}-%{version}

%build
cd %{zope_subname}
rm -rf `find . -type d -name CVS`
rm -rf {.cvsignore,debian}
mkdir docs
mv -f AUTHORS README.txt docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}

cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/docs/*
%{product_dir}/%{zope_subname}
