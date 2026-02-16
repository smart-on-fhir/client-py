#!/bin/bash
#
# Generate FHIR model classes for a specific version.
#
# Usage:
#   ./generate_models.sh           # Generate R4 models (default, backward compat)
#   ./generate_models.sh R4        # Generate R4 models
#   ./generate_models.sh STU3      # Generate STU-3 models
#   ./generate_models.sh all       # Generate all supported versions
#
# To add a new FHIR version (e.g., R5):
#   1. Create fhir-parser-resources/settings_R5.py
#   2. Create fhirclient/models/R5/__init__.py (with register_version call)
#   3. Run: ./generate_models.sh R5

set -e

VERSION="${1:-R4}"

if [ ! -e fhir-parser ]; then
	git submodule update --init --recursive
fi

generate_version() {
	local ver="$1"
	local settings_file="fhir-parser-resources/settings_${ver}.py"

	# Fall back to settings.py for backward compatibility (legacy R4)
	if [ ! -f "$settings_file" ]; then
		if [ "$ver" = "R4" ] && [ -f "fhir-parser-resources/settings.py" ]; then
			settings_file="fhir-parser-resources/settings.py"
		else
			echo "Error: Settings file not found: $settings_file"
			exit 1
		fi
	fi

	echo "Generating FHIR $ver models using $settings_file..."
	cp "$settings_file" fhir-parser/settings.py
	cd fhir-parser
	./generate.py "$2"
	cd ..
	echo "Done generating $ver models."
}

if [ "$VERSION" = "all" ]; then
	generate_version "R4"
	# Uncomment as versions are added:
	# generate_version "STU3"
	# generate_version "R5"
else
	generate_version "$VERSION" "$2"
fi
