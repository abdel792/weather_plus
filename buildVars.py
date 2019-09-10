
# -*- coding: UTF-8 -*-
# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
import os.path
from datetime import datetime
now =datetime.now()
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "Weather_Plus",
	# Add-on summary, usually the user visible name of the addon.
	"addon_summary" : "Weather_Plus",
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : [
	_("Adds local temperature and forecast 24 ours and prediction up to 9 days.\n"),
	_("NVDA+w for the current bulletin.\n"),
	_("NVDA+shift+w for the prediction in the current 24 hours and prediction up to 9 days.\n"),
	_("NVDA+shift+control+w for quickly enter a temporary city.\n"),
	_("NVDA + shift + control + alt + w for open the Weather Plus settings.\n"),
	_("NVDA+alt+w announces the date of the last update of the weather report.\n"),
	_("Shift+control+w alternates between Fahrenheit, Celsius and Kelvin.\n"),
	_("For other instructions, you can also press Add-on Help button in Add-ons manager."),
	],
	# version
	"addon_version" : "7.1",
	# Author(s)
	"addon_author" : "Adriano Barbieri <adrianobarb@yahoo.it>",
	# URL for the add-on documentation support
	"addon_url" : "http://www.nvda.it/weather-plus/",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2012.2.1")
	"addon_minimumNVDAVersion" : "2017.3.0",
	# Last NVDA version supported/tested (e.g. "2018.4", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2019.3.0",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}
# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "*.py"),
os.path.join("addon", "globalPlugins", "Weather_Plus", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = ["hmac.py", "platform.py", "pybass.py", "oauth.pyc", "oauth.pyo"]
