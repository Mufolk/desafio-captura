import pip

installed_packages = pip.get_installed_distributions()

flat_installed_packages = [package.project_name for package in installed_packages]

print flat_installed_packages