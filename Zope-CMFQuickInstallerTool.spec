%include	/usr/lib/rpm/macros.python

%define		zope_subname	CMFQuickInstallerTool

Summary:	CMFQuickInstallerTool is a Zope product independent from the former CMFQuickInstaller
Summary(pl):	CMFQuickInstallerToolL jest dodatkiem do Zope niezale¿nym od formy CMFQuickInstaller
Name:		Zope-%{zope_subname}
Version:	1.0
Release:	1
License:	GNU
Group:		Development/Tools
Source0:	http://switch.dl.sourceforge.net/sourceforge/collective/%{zope_subname}_%{version}.tgz
# Source0-md5:	dfcb8b48682a8164b0b955235113ec7b
URL:		http://cvs.bluedynamics.org/viewcvs/CMFQuickInstallerTool/
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	CMF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
CMFQuickInstallerTool is a Zope product independent from the former
CMFQuickInstaller. The main difference to CMFQuickInstaller the
tracking of what a product creates during install.

%description -l pl
CMFQuickInstallerToolL jest dodatkiem do Zope niezale¿nym od formy
CMFQuickInstaller. Dodatek w stosunku do CMFQuickInstaller umo¿liwa
¶ledzenie zmian produktów podczas tworzenia instalacji.

%prep
%setup -q -c %{zope_subname}-%{version}

%build
cd %{zope_subname}
mkdir docs
mv -f AUTHORS README.txt docs/
rm -rf .cvsignore

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}
cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%preun

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/docs/*
%{product_dir}/%{zope_subname}
