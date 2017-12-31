# Jenkins Utilities
Some utility methods for getting information from Jenkins using the Jenkins Python API

## Setup

1. Clone Repository
2. In the root, run `pip3 install -r requirements.txt`
3. Update JenkinsConfiguration.py with your jenkins server URL, and your credentials
4. Run `python3 JenkinsUtils.py <command>`

## Available Commands

* `nodeNames`:  This prints a list of all the nodes on the Jenkins Server
* `offlineNodes`: This prints a list of all the offline nodes on the Jenkins Server
* `allJobs`: This prints a list of all jobs on the Jenkins Server (NOTE: This can take a very, very, very long time)
* `plugins`: Prints all plugins installed in Jenkins (Note: Requires administrator credentials)
* `enabledPlugins`: Prints all enabled plugins
* `disabledPlugins`: Prints all disabled plugins
* `pluginVersions`: Prints the plugin name along with the currently installed version
* `pluginUrl`: Prints plugin name along with the plugin URL
