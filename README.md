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
* `pluginUrl`: Prints plugin name along with the plugin URLp
* `jenkinsVersion`: Prints current version of Jenkins
* `possibleLabels`: Prints a list of all the possible labels you can use (NOTE: This is very, very slow. Use sparingly)
* `runningJobs`: Prints all jobs that are running. (NOTE: This is very, very slow. Use sparingly)
* `queue`: Prints list of jobs waiting in the build queue.
* `queueLength`: Prints number of jobs in the queue



## DockerFiles

### Python Testing

To build a Docker image with the JenkinsAPI project in, run:

 `docker build -f PythonDockerfile .`

To run:
 `docker run --net host <image>`

### Jenkins Testing

To have a mock Jenkins instance with jobs, nodes and plugins installed, use:

`cd Jenkins; docker build -f JenkinsDockerfile .`

To view the jenkins instance, run the container while opening port 8080.

`docker run -p 8080:8080 <jenkinsDockerfileImage>`