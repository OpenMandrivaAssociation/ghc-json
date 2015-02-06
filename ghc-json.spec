%global debug_package %{nil}

%global module json

Summary:	Haskell JSON library
Name:		ghc-json
Version:	0.7
Release:	3
License:	BSD
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	ghc-mtl
BuildRequires:	ghc-text
BuildRequires:	haddock
BuildRequires:	haskell-macros
Requires(post,preun):	ghc

%description
A JSON library for Haskell.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

