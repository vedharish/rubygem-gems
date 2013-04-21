# Generated from barista-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gemname barista

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Simple, transparent coffeescript integration for Rails and Rack applications
Name: rubygem-%{gemname}
Version: 1.3.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/Sutto/barista
Source0: %{gemname}-%{version}.gem
Source1: spec.tar.gz
Requires: ruby(rubygems) 
Requires: rubygem(coffee-script) => 2.2
Requires: rubygem(coffee-script) < 3
BuildRequires: ruby(rubygems) 
BuildRequires: ruby
BuildRequires: rubygem-rspec
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Barista provides simple, integrated support for CoffeeScript in Rack and Rails
applications.
Much like Compass does for Sass, It also provides Frameworks (bundleable code
which can be shared via Gems).
Lastly, it also provides a Rack Application (which can be used to server
compiled code), a around_filter-style precompiler (as Rack middleware) and
simple helpers for rails and Haml.
For more details, please see the the README file bundled with it.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}
tar -xzf %{SOURCE1}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/

%check
cp -pr spec/ ./%{geminstdir}
pushd ./%{geminstdir}
rspec -Ilib spec
rm -rf spec
popd

%files
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%{geminstdir}/.document
%{geminstdir}/.rspec
%{geminstdir}/.rvmrc.example
%{geminstdir}/DESCRIPTION
%{geminstdir}/Gemfile
%{geminstdir}/Gemfile.lock
%{geminstdir}/Rakefile
%{geminstdir}/barista.gemspec
%{geminstdir}/rubygem-barista.spec.template
%{geminstdir}/spec.tar.gz

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md


%changelog
* Sat Apr 20 2013 Harish Ved - 1.3.0-1
- Initial package
